import os
import yaml
from crewai import Agent, LLM
from helper_tools import BrowsingTool
from typing import Dict

class AgentFactory:
    """Factory class for creating and managing AI agents."""
    
    def __init__(self, config_path: str = 'config/agents.yaml'):
        """
        Initialize the AgentFactory.
        
        Args:
            config_path: Path to the agents configuration YAML file
        """
        self.agents_config = self._load_config(config_path)
        self.llm = self._setup_llm()
        self.agents = self._create_agents()
        
    def _load_config(self, config_path: str) -> dict:
        """Load agent configurations from YAML file."""
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            print("## Agents configuration loaded")
            return config
        except Exception as e:
            print(f"Error loading agent configurations: {str(e)}")
            raise
            
    def _setup_llm(self) -> Dict[str, LLM]:
        """Setup LLM configurations."""
        llm = LLM(
            model="openrouter/anthropic/claude-3.5-haiku",
            temperature=0,
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
        
        return {
            'default': llm,
            'coding': llm  # You could use different LLMs for different purposes
        }
        
    def _create_agents(self) -> Dict[str, Agent]:
        """Create all required agents."""
        agents = {}
        
        # Manager Agent
        agents['manager'] = Agent(
            role=self.agents_config['manager']['role'],
            goal=self.agents_config['manager']['goal'],
            backstory=self.agents_config['manager']['backstory'],
            llm=self.llm['default'],
            allow_delegation=False,
            verbose=True
        )
        
        # Coding Agent
        agents['coding'] = Agent(
            role=self.agents_config['codeing_agent']['role'],
            goal=self.agents_config['codeing_agent']['goal'],
            backstory=self.agents_config['codeing_agent']['backstory'],
            llm=self.llm['coding'],
            allow_delegation=False,
            verbose=True
        )
        
        # Code Review Agent
        agents['review'] = Agent(
            role=self.agents_config['codereview_agent']['role'],
            goal=self.agents_config['codereview_agent']['goal'],
            backstory=self.agents_config['codereview_agent']['backstory'],
            llm=self.llm['default'],
            allow_delegation=False,
            verbose=True
        )
        
        # UI/UX Agent
        agents['uiux'] = Agent(
            role=self.agents_config['uiux_agent']['role'],
            goal=self.agents_config['uiux_agent']['goal'],
            backstory=self.agents_config['uiux_agent']['backstory'],
            llm=self.llm['default'],
            allow_delegation=False,
            verbose=True
        )
        
        # Documentation Agent
        agents['documentation'] = Agent(
            role=self.agents_config['documentation_agent']['role'],
            goal=self.agents_config['documentation_agent']['goal'],
            backstory=self.agents_config['documentation_agent']['backstory'],
            llm=self.llm['default'],
            allow_delegation=False,
            verbose=True
        )
        
        # Test Agent
        agents['test'] = Agent(
            role=self.agents_config['test_agent']['role'],
            goal=self.agents_config['test_agent']['goal'],
            backstory=self.agents_config['test_agent']['backstory'],
            llm=self.llm['default'],
            allow_delegation=False,
            verbose=True
        )
        
        # Browsing Agent
        agents['browsing'] = Agent(
            role=self.agents_config['browsing_agent']['role'],
            goal=self.agents_config['browsing_agent']['goal'],
            backstory=self.agents_config['browsing_agent']['backstory'],
            tools=[BrowsingTool()],
            llm=self.llm['default'],
            verbose=True
        )
        
        return agents
    
    def get_agent(self, agent_name: str) -> Agent:
        """
        Get an agent by name.
        
        Args:
            agent_name: Name of the agent to retrieve
            
        Returns:
            The requested Agent instance
        """
        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}")
        return self.agents[agent_name]
    
    def get_all_agents(self) -> list:
        """
        Get list of all agents in the order they should be used.
        
        Returns:
            List of Agent instances in the correct order
        """
        return [
            self.agents['manager'],
            self.agents['coding'],
            self.agents['review'],
            self.agents['uiux'],
            self.agents['documentation'],
            self.agents['test'],
            self.agents['browsing']
        ]
