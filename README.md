## CrewAI Framework
### Overview
The CrewAI Framework is an example designed to automate tasks using AI agents with the integration of various large language models (LLMs) such as OpenAI's GPT and others. The framework enables you to manage, configure, and process complex AI-driven workflows, utilizing APIs and environment configurations to interact with external LLM providers.

This document provides a guide on how to set up and use the framework, explaining the core components and their functionality.

### Features
Integrate multiple AI models (OpenAI, Llama, etc.) through API-based connections.
Set up and configure tasks for AI agents using a simple and flexible interface.
Extendable with tools like CalculatorTool for added computational capabilities.
Environment-variable-driven configuration for easier setup and deployment.
Requirements
Python 3.8+
Dependencies as listed in requirements.txt
Environment variables for API keys (OpenAI, etc.)
Environment Variables
Make sure the following environment variables are set up in your .env file:

OPENAI_API_KEY: The API key for accessing OpenAI's models.
OPENAI_MODEL_NAME: The model name to use from OpenAI.
Other environment variables may be required depending on the specific models used.

### Installation
Clone the repository.

```bash
git clone https://github.com/com2u/CrewAI_Framework
cd CrewAI_Framework
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```
Set up the .env file with your API keys:


```bash
cp .env.example .env
```

# Fill in the required API keys in the .env file
### Usage
Running the Framework
To start the CrewAI framework, simply execute the main.py script:


```bash
python main.py
```
Components
1. Agents
The Agent class represents individual AI agents responsible for executing tasks. Each agent is configured to interact with a specific LLM model. You can customize the models and behaviors using environment variables.

2. Task
Tasks are discrete units of work that agents will perform. They are defined programmatically in the framework and can range from simple text processing to more complex operations using external tools like CalculatorTool.

3. Crew
A crew is a collection of agents working together to perform larger workflows or complex tasks. The framework orchestrates multiple agents to collaborate on achieving a goal.

4. Process
The Process class manages task execution, directing agents to work on specific tasks as required.

### Example Task Execution
An example of executing a task might look like this:

```Python
from crewai import Agent, Task

# Define a task
task = Task(description="Calculate something complex")

# Create an agent and assign the task
agent = Agent(model="gpt-3.5-turbo")
agent.assign_task(task)
agent.execute()
```

This will use the specified model (gpt-3.5-turbo) to execute the task.

Extending the Framework
The framework is designed to be extendable. You can add new models, tools, or tasks by modifying the relevant classes in the codebase.

For example, if you want to integrate a new LLM model, add it to the configuration and modify the Agent class to support it.

Frontend Components (if applicable)
Although this project does not include a frontend interface out of the box, it can easily be integrated with one. If you choose to implement a frontend, you can build a UI that allows users to:

Select AI models and configure agents.
Input tasks and view results.
Monitor and manage task execution across multiple agents.
Frontend Example (Optional)
You can use modern frameworks like React or Vue.js to build an interface for the CrewAI framework. An example of a simple frontend interaction:

A form for inputting tasks (description, type).
A dashboard displaying agents and their current tasks.
A results section showing completed task outputs.
Error Handling
The framework includes basic error handling in the execution process. When configuring new agents or tasks, ensure that appropriate exception handling is implemented to manage API failures, model errors, or timeouts.

License
This project is licensed under the MIT License. See the LICENSE file for details.