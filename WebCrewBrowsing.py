import os
import yaml
from crewai import Crew, Process
from dotenv import load_dotenv
import asyncio
import nest_asyncio
import argparse

from agents import AgentFactory
from tasks import TaskFactory

class WebCrewBrowsing:
    """Main class for managing the web crew browsing process."""
    
    def __init__(self):
        """Initialize the WebCrewBrowsing instance."""
        print("## Starting CrewAI Framework")
        
        # Initialize environment
        load_dotenv()
        nest_asyncio.apply()
        print("## Environment loaded")
        
        # Initialize components
        self.development_tasks = self._load_requirements()
        self.agent_factory = AgentFactory()
        self.task_factory = TaskFactory(agent_factory=self.agent_factory)
        print("## Agents and Tasks initialized")
        
        # Create crew
        self.crew = Crew(
            agents=self.agent_factory.get_all_agents(),
            tasks=self.task_factory.get_all_tasks(),
            process=Process.sequential,
            verbose=True
        )
        print("## Crew created")
        
    def _load_requirements(self) -> list:
        """Load requirements configuration from YAML file."""
        try:
            with open('config/requirements.yaml', 'r') as f:
                requirements_config = yaml.safe_load(f)
            print("## Requirements configuration loaded")
            return requirements_config['development_tasks']
        except Exception as e:
            print("Error loading requirements configuration:", str(e))
            raise
            
    async def async_crew_execution(self):
        """Execute crew tasks asynchronously."""
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self.run_crew)
        return result
        
    def read_and_backup_file(self, file_path: str, loop: int = None, make_backup: bool = True) -> str:
        """
        Read a file and optionally create a backup with loop number.
        
        Args:
            file_path: Path to the file to read
            loop: Current loop number for backup file naming
            make_backup: Whether to create a backup file
            
        Returns:
            Content of the file or empty string if file doesn't exist
        """
        content = ""
        try:
            with open(file_path, "r") as f:
                content = f.read()
                print(f"Read from {file_path}:")
                print(content)
                
            if make_backup and loop is not None:
                # Create backup with loop number
                backup_path = f"{file_path.rsplit('.', 1)[0]}{loop}.{file_path.rsplit('.', 1)[1]}"
                with open(backup_path, "w+") as f:
                    f.write(content)
                    
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return content

    def write_file(self, file_path: str, content: str):
        """
        Write content to a file.
        
        Args:
            file_path: Path to write the file to
            content: Content to write to the file
        """
        try:
            with open(file_path, "w+") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")

    def cleanup_source_code(self, loop: int):
        """
        Clean up the source code by removing markdown and unnecessary text,
        then save both the cleaned file and a backup.
        
        Args:
            loop: Current loop number for backup file naming
        """
        # Read the source file
        implementation = self.read_and_backup_file("public/index.html", None, False)
        
        if implementation:
            # Clean up the content
            cleaned_content = implementation.replace("```html", "").replace("```", "").replace("my best complete final answer to the task.", "")
            print("File cleanup start:")
            print(cleaned_content)
            
            # Write cleaned content to main file
            self.write_file("public/index.html", cleaned_content)
            
            # Write backup with loop number
            self.write_file(f"public/index{loop}.html", cleaned_content)
            
            print("File cleanup done")

    def run(self):
        """Main execution method."""
        development_project = ""
        result = ""
        loop = 0
        
        for subtask in self.development_tasks:
            loop = loop + 1
            development_project = development_project + subtask
            
            # Write requirement
            self.write_file(f"markdown/requirement{loop}.md", development_project)
            
            # Read all necessary files
            implementation = self.read_and_backup_file("public/index.html", None, False)  # Don't backup index.html here
            readme = self.read_and_backup_file("markdown/readme.md", loop)
            test = self.read_and_backup_file("markdown/test.md", loop)
            browsing = self.read_and_backup_file("markdown/browsing.md", loop)
            review = self.read_and_backup_file("markdown/review.md", loop)
            uiux = self.read_and_backup_file("markdown/uiux.md", loop)

            # Update task descriptions
            management_description = f"""Use and always stick with the following requirements: 
            
            ### Requirement
            {development_project}
            
            ### Reference implementation README.md:
            {readme} 
            
            ### Current implementation CODE:
            {implementation}
            """
            self.task_factory.update_task_description('management', management_description)

            coding_description = f"""Start implementing the task bases on the existing feedback of manager, reviewer and desigener.  
            Update the Current CODE implementation 
            Output only the complete source code - nothing else.
            
            {management_description}
            
            ### Code Review:
            {review}

            ### Code Review:
            {test}

            ### Design UI/UX Review:
            {uiux}

            ### Browsing the page review:
            {browsing}
            """
            self.task_factory.update_task_description('coding', coding_description)

            # Write coding task description
            self.write_file(f"markdown/CodingTask{loop}.md", coding_description)
            
            # Execute crew tasks
            result = self.crew.kickoff()
            implementation = ""
            self.cleanup_source_code(loop)
            print(" = = = = = = = = C Y C L E = = = = = E N D = = = = = = = = ")

        return result

def main():
    """Main entry point."""
    web_crew = WebCrewBrowsing()
    result = web_crew.run()
    print(result)

if __name__ == "__main__":
    main()
