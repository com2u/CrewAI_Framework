import yaml
from crewai import Task
from typing import Dict, List
from agents import AgentFactory

class TaskFactory:
    """Factory class for creating and managing AI tasks."""
    
    def __init__(self, config_path: str = 'config/tasks.yaml', agent_factory: AgentFactory = None):
        """
        Initialize the TaskFactory.
        
        Args:
            config_path: Path to the tasks configuration YAML file
            agent_factory: AgentFactory instance for getting agents
        """
        self.tasks_config = self._load_config(config_path)
        self.agent_factory = agent_factory or AgentFactory()
        self.tasks = self._create_tasks()
        
    def _load_config(self, config_path: str) -> dict:
        """Load task configurations from YAML file."""
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            print("## Tasks configuration loaded")
            return config
        except Exception as e:
            print(f"Error loading task configurations: {str(e)}")
            raise
            
    def _create_tasks(self) -> Dict[str, Task]:
        """Create all required tasks."""
        tasks = {}
        
        # Management Task
        tasks['management'] = Task(
            description=self.tasks_config['management_task']['description'],
            expected_output=self.tasks_config['management_task']['expected_output'],
            agent=self.agent_factory.get_agent('manager')
        )
        
        # Coding Task
        tasks['coding'] = Task(
            description=self.tasks_config['coding_task']['description'],
            expected_output=self.tasks_config['coding_task']['expected_output'],
            output_file="public/index.html",
            context=[tasks['management']],
            agent=self.agent_factory.get_agent('coding')
        )
        
        # Review Task
        tasks['review'] = Task(
            description=self.tasks_config['review_task']['description'],
            expected_output=self.tasks_config['review_task']['expected_output'],
            output_file="markdown/review.md",
            context=[tasks['coding']],
            agent=self.agent_factory.get_agent('review')
        )
        
        # Designer Task
        tasks['designer'] = Task(
            description=self.tasks_config['designer_task']['description'],
            expected_output=self.tasks_config['designer_task']['expected_output'],
            output_file="markdown/uiux.md",
            context=[tasks['coding']],
            agent=self.agent_factory.get_agent('uiux')
        )
        
        # Documentation Task
        tasks['documentation'] = Task(
            description=self.tasks_config['documentation_task']['description'],
            expected_output=self.tasks_config['documentation_task']['expected_output'],
            output_file="markdown/readme.md",
            context=[tasks['coding']],
            agent=self.agent_factory.get_agent('documentation')
        )
        
        # Test Task
        tasks['test'] = Task(
            description=self.tasks_config['test_task']['description'],
            expected_output=self.tasks_config['test_task']['expected_output'],
            output_file="markdown/test.md",
            context=[tasks['coding']],
            agent=self.agent_factory.get_agent('test')
        )
        
        # Browsing Task
        tasks['browsing'] = Task(
            description=self.tasks_config['browsing_task']['description'],
            expected_output=self.tasks_config['browsing_task']['expected_output'],
            output_file="markdown/browsing.md",
            agent=self.agent_factory.get_agent('browsing')
        )
        
        return tasks
    
    def get_task(self, task_name: str) -> Task:
        """
        Get a task by name.
        
        Args:
            task_name: Name of the task to retrieve
            
        Returns:
            The requested Task instance
        """
        if task_name not in self.tasks:
            raise ValueError(f"Unknown task: {task_name}")
        return self.tasks[task_name]
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get list of all tasks in the order they should be executed.
        
        Returns:
            List of Task instances in the correct order
        """
        return [
            self.tasks['management'],
            self.tasks['coding'],
            self.tasks['review'],
            self.tasks['designer'],
            self.tasks['documentation'],
            self.tasks['test'],
            self.tasks['browsing']
        ]
        
    def update_task_description(self, task_name: str, description: str):
        """
        Update a task's description.
        
        Args:
            task_name: Name of the task to update
            description: New description for the task
        """
        if task_name not in self.tasks:
            raise ValueError(f"Unknown task: {task_name}")
        self.tasks[task_name].description = description
