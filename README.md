# CrewAI Framework

## Overview
The CrewAI Framework is an innovative development automation system that orchestrates multiple AI agents to collaboratively develop software projects. Unlike traditional AI frameworks that use a single agent, this framework implements a "crew" of specialized AI agents, each with distinct roles and responsibilities in the development process.

## Key Features
- **Multi-Agent Collaboration**: Implements a crew of specialized AI agents working together:
  - Manager Agent: Oversees project requirements and coordinates development
  - Coding Agent: Implements the actual code
  - Code Review Agent: Reviews and suggests improvements
  - UI/UX Agent: Focuses on user interface and experience
  - Documentation Agent: Handles documentation
  - Test Agent: Manages testing
  - Browsing Agent: Validates implementations

- **Sequential Process Workflow**: Automated development cycle where each agent contributes their expertise in a coordinated sequence
- **Iterative Development**: Supports multiple development cycles with automatic file versioning and backups
- **Configuration-Driven**: Easy setup through YAML configuration files for agents and tasks
- **OpenRouter Integration**: Uses advanced language models through OpenRouter API
- **Automated Code Management**: Handles code cleanup, backup creation, and file management

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`
- OpenRouter API key for accessing AI models

## Installation

1. Clone the repository:
```bash
git clone https://github.com/com2u/CrewAI_Framework
cd CrewAI_Framework
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

## Creating Projects with CrewAI

### 1. Define Requirements
Create or modify `config/requirements.yaml` to define your development tasks:
```yaml
development_tasks:
  - "Task 1 description"
  - "Task 2 description"
  # Add more tasks as needed
```

### 2. Configure Agents
Adjust `config/agents.yaml` to customize agent behaviors:
```yaml
manager:
  role: "Project Manager"
  goal: "Ensure project requirements are met"
  backstory: "Experienced in overseeing software projects"

codeing_agent:
  role: "Senior Software Developer"
  goal: "Write efficient and maintainable code"
  # ... configure other agents similarly
```

### 3. Run the Framework
Execute the main script to start the development process:
```bash
python WebCrewBrowsing.py
```

The framework will:
1. Load your requirements
2. Initialize the AI agent crew
3. Execute development tasks sequentially
4. Generate and manage code files
5. Create backups for each development iteration

## Project Structure
```
CrewAI_Framework/
├── config/                 # Configuration files
│   ├── agents.yaml        # Agent definitions
│   ├── requirements.yaml  # Project requirements
│   └── tasks.yaml        # Task configurations
├── markdown/              # Development artifacts
├── public/               # Generated code output
├── tools/                # Custom tools
└── WebCrewBrowsing.py    # Main execution script
```

## Development Cycle
1. **Requirement Analysis**: Manager Agent processes the requirements
2. **Implementation**: Coding Agent writes the code
3. **Code Review**: Review Agent analyzes the implementation
4. **UI/UX Review**: UI/UX Agent evaluates the interface
5. **Documentation**: Documentation Agent updates documentation
6. **Testing**: Test Agent verifies functionality
7. **Validation**: Browsing Agent checks the implementation

Each cycle creates backups and maintains versions of the implementation, allowing for iterative improvements.

## Extending the Framework

### Adding New Agents
Extend the `AgentFactory` class in `agents.py` to add new specialized agents:
```python
agents['new_agent'] = Agent(
    role="New Role",
    goal="Specific Goal",
    backstory="Agent Backstory",
    llm=self.llm['default'],
    allow_delegation=False,
    verbose=True
)
```

### Custom Tools
Create new tools in the `tools/` directory to add capabilities:
```python
class CustomTool(BaseTool):
    def execute(self, *args, **kwargs):
        # Tool implementation
        pass
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
