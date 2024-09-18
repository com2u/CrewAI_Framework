import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from llama_index.llms.openrouter import OpenRouter

print("## Starting CrewAI Framwork")
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

#os.environ["OPENAI_API_BASE"] = 'http://100.126.56.111:11434/v1'
#os.environ["OPENAI_MODEL_NAME"] ='llama3.1:latest'  # Adjust based on available model
#os.environ["OPENAI_API_KEY"] =os.getenv("OPENROUTER_API_KEY")

# llama31 = ChatOpenAI(model="o1-preview", base_url="https://openrouter.ai/api/v1", os.getenv("OPENROUTER_API_KEY"))


#llama31 = OpenRouter(
#    api_key=os.getenv("OPENROUTER_API_KEY"),
#    max_tokens=256,
#    context_window=4096,
#    model="openai/o1-preview",
#)

llama31 = ChatOpenAI(
  model="openai/o1-preview",
  openai_api_key = os.getenv("OPENROUTER_API_KEY"),
  openai_api_base = 'https://openrouter.ai/api/v1',
  default_headers = {
    "HTTP-Referer": "https://www.ai-server.org/",
    "X-Title": "My SCRUM Crew"
  },
  temperature=0.3,
  streaming=True
)

# llama31 = Ollama(model="llama3.1:latest", base_url="http://100.126.56.111:11434/v1")
# codestral = Ollama(model="codestral:latest", base_url="http://100.126.56.111:11434/v1")
# llama31 = Ollama(model="llama3.1:latest", base_url="http://100.126.56.111:3000/v1")
# codestral = Ollama(model="codestral:latest", base_url="http://100.126.56.111:3000/v1")
# llm = ChatOpenAI(model = "crewai-llama3", base_url = "http://100.126.56.111:11434/v1")

# Provide the project requirement
developmentProject="""Create a web page for a device management app. The page should maintain different devices in a web page. 
         The device management app should maintain the following data per device:
         ·        Device Name (String)
         ·        DeviceType (Allowed types: Smartphone, Tablet, Camera)
         ·        Owner Name (String)
         ·        Battery Status (0…100%)
         List existing devices of the app
         Add the possibility to update all device settings or delete existing devices.
         Add the possibility to create new devices with a screen to input the data.
         When a device was added decrease the per device given Battery Status every second by 1% until it reaches 0%.
         Store the device data be be persistent."""


# Static code which does not need to be changed for the different tasks in the defined environment
manager = Agent(
    role="Manager for a software development team",
    goal="You will get tasks and requirements for a software development project. You will read the task and split it into sub tasks for the development.",
    backstory="You know the complexity of software development and break down complex tasks into several individual implementation steps",
    #llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    llm=llama31,
    allow_delegation=False,
    verbose=True
)

codeing_agent = Agent(
    role="Professional web coding agent",
    goal="From the manager you get the list of tasks. Start with the first task to solve it. You will create the HTML web page with all the needed components. You will output the needed sourcecode",
    backstory="You are professional web developer for HTML, JS, and CSS",
    #llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    llm=llama31,
    allow_delegation=False,
    #allow_code_execution=True,
    verbose=True
)

codereview_agent = Agent(
    role="Code reviewer",
    goal="check the given code and provide one suggestion to make the code more stable, robust or professional",
    backstory="""You are a professional web developer. You think about code quality, coding style, architecture, naming, error handling
    """,
    llm=llama31,
    allow_delegation=False,
    verbose=True
)

uiux_agent = Agent(
    role="Frontend designer for UI/UX",
    goal="Check the given code and provide one suggestion to improve the design, layout, usability or look&feel",
    backstory="""You are a professional designer with focus on UI/UX. You think about user interaction and a clean logic and consitent frontend""",
    llm=llama31,
    allow_delegation=False,
    verbose=True
)

documentation_agent = Agent(
    role="Development software documentation",
    goal="Provide a Readme.md to document the technical software documentation and how to use it. Describe what the user can do with the software and how to use the frontend and its components.",
    backstory="""You are an expert for professional software documentation. You think about structure of the documentation. All documentation should be logic, clean and easy to read. """,
    llm=llama31,
    allow_delegation=False,
    verbose=True
)

test_agent = Agent(
    role="Software tester",
    goal="You will check that the code contains all requirements. Provide a test.md to document the check results. Generate a list of all requirements you can check.",
    backstory="""You are an professional tester by reading the requirements and comparing them with the implementation """,
    llm=llama31,
    allow_delegation=False,
    verbose=True
)

managementTask = Task(
    description=developmentProject,
    expected_output="Provide a list of tasks to complete the software development project",
    #human_input=True,
    agent=codeing_agent
)

codingTask1 = Task(
    description=f"Start implementing the first task from task list created by the manager",
    expected_output="Just provide the full code without any explanation as index.html to be opened with a browser",
    output_file="public/index1.html",
    agent=codeing_agent
)

codingTask2 = Task(
    description=f"Start implementing the second task from task list created by the manager",
    expected_output="Just provide the full code without any explanation as index.html to be opened with a browser",
    output_file="public/index2.html",
    agent=codeing_agent
)

codingTask3 = Task(
    description=f"Start implementing the next task from task list created by the manager",
    expected_output="Just provide the full code without any explanation as index.html to be opened with a browser",
    output_file="public/index.html",
    agent=codeing_agent
)

reviewTask = Task(
    description="do a proper code review from the coding agent results and share your suggestion to improve the code",
    expected_output="""Explain one most important suggestion to improve the code in markdown format""",
    output_file="markdown/review.md",
    agent=codereview_agent
)

designerTask = Task(
    description="Think about optimising the design. Provide one suggestion to improve design, layout or usability of the frontend",
    expected_output="""Explain one most important suggestion to improve the code in markdown format""",
    output_file="markdown/uiux.md",
    agent=uiux_agent
)

documentationTask = Task(
    description="Think about what is needed to be documented. Be specific with naming. Guide the user how to use the software. Provide nessescary hints for the user he needs to be aware of",
    expected_output="""Provide the documentation in typical Readme.md markdown format""",
    output_file="markdown/readme.md",
    agent=documentation_agent
)

testTask = Task(
    description="Generate a list af all needed features based on the requirements. Check for everything in your list if you will find a proper implementation in the code. Provide a checkmark for each completed featuren, a cross for missing and a questionmak if you are not sure",
    expected_output="""Provide the test check list in markdown format""",
    output_file="markdown/test.md",
    agent=test_agent
)

crew = Crew(
    agents=[manager, codeing_agent, codereview_agent, uiux_agent],
    tasks=[managementTask, codingTask1, reviewTask, codingTask2, designerTask, codingTask3, documentationTask, testTask],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print(result)







