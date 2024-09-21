import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
#from llama_index.llms.openrouter import OpenRouter
from CalculatorTool import calculate, code, requirement

developmentProjectSubTask = [
    """Create a web page for a device management app. The page should maintain different devices in a web page. 
             The device management app should maintain the following data per device:
             ·        Device Name (String)
             ·        DeviceType (Allowed types: Smartphone, Tablet, Camera)
             ·        Owner Name (String)
             ·        Battery Status (0…100%)
             List existing devices of the app in a table.
             Add the possibility to create new devices with a screen to input the data.
             Your solution should be one HTML page with all components, styles and JavaScript code in this file.""",
   "Add the possibility to update a settings of a selected device in one screen or delete existing devices.\n\r",
   "When a device was added decrease the per device given Battery Status every second by 1% until it reaches 0%.\n\r"
   "Make sure to update battery status every second in the table.\n\r"
   "Add a colored visualization (e.g. Progress bar) of the battery status to the device table.\n\r",
   "Use unicode icons for the device types Smartphone, Tablet, Camera.\n\r",
   "Mark an empty device in red and a device with power in green. Make sure it will stay red when 0% are reached.\n\r",
   "Provide the possibility to order the device table by Device Name, DeviceType, Owner Name, Battery Status.\n\r",
   "Add to the existing devices types: Laptop, Car, Powerbank. Provide a matching icon\n\r",
   ""
]

#    "Store the device settings in the local browser store. Load the devices from the browser store with the page. Make sure it will work when the store is empty and nothing was created (e.g. first start).\n\r",

print("## Starting CrewAI Framwork")
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

#os.environ["OPENAI_API_BASE"] = 'http://100.126.56.111:11434/v1'
#os.environ["OPENAI_MODEL_NAME"] ='llama3.1:latest'  # Adjust based on available model
#os.environ["OPENAI_API_KEY"] =os.getenv("OPENROUTER_API_KEY")

# llama31 = ChatOpenAI(model="meta-llama/llama-3-8b-instruct:extended", base_url="https://openrouter.ai/api/v1", os.getenv("OPENROUTER_API_KEY"))
# llama31 = ChatOpenAI(model="o1-preview", base_url="https://openrouter.ai/api/v1", os.getenv("OPENROUTER_API_KEY"))

#llama31 = ChatOpenAI(
#  model="o1-preview",
#  openai_api_key = os.getenv("OPENROUTER_API_KEY"),
#  openai_api_base = 'https://openrouter.ai/api/v1',
#  default_headers = {
#    "HTTP-Referer": "https://www.ai-server.org/",
#    "X-Title": "My SCRUM Crew"
#  },
#  temperature=0.3,
#  streaming=True
#)


llama31 = Ollama(model="llama3.1", base_url="http://100.126.56.111:11434")
#llama31 = Ollama(model="llama3.1", base_url="https://openrouter.ai/api/v1")
#codestral = Ollama(model="codestral:latest", base_url="http://100.126.56.111:11434")
#mistral = Ollama(model="mistral-nemo:latest", base_url="http://100.126.56.111:11434")
#commandr = Ollama(model="command-r:latest", base_url="http://100.126.56.111:11434")

# Provide the project requirement
developmentProject=""


# Static code which does not need to be changed for the different tasks in the defined environment
manager = Agent(
    role="Manager for a software development team",
    goal="You will get tasks and requirements for a software development project. If exist check the current rerfence implementation. You will read the task and implementation to split it into sub tasks for the development for not yet implemenented features. ",
    backstory="You know the complexity of software development and break down complex tasks into several individual implementation steps",
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    #llm=llama31,
    allow_delegation=False,
    verbose=True
)

codeing_agent = Agent(
    role="Professional web coding agent",
    goal="From the manager you get the list of tasks. Start with the first task to solve it. You will create the HTML web page with all the needed components. Allways provide the full code. Don't use place holders or references to existing code. The code needs allways to be complete with all implementations which have been made. You will output the needed sourcecode for the web page.",
    backstory="You are professional web developer for HTML, JS, and CSS",
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    #llm=llama31,
    allow_delegation=False,
    #allow_code_execution=True,
    #tools=[requirement],
    verbose=True
)


codereview_agent = Agent(
    role="Code reviewer",
    goal="Check the given code and provide one suggestion to make the code more stable, robust or professional. Never suggest to extract JavaScript or CSS to an external file.",
    backstory="""You are a professional web developer. You think about code quality, coding style, architecture, naming, error handling
    """,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    #llm=llama31,
    allow_delegation=False,
    #tools=[requirement],
    verbose=True
)

uiux_agent = Agent(
    role="Frontend designer for UI/UX",
    goal="Check the given code and provide one suggestion to improve the design, layout, usability or look&feel. ",
    backstory="""You are a professional designer with focus on UI/UX. You think about user interaction and a clean logic and consitent frontend""",
    #llm=llama31,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    allow_delegation=False,
    #tools=[requirement],
    verbose=True
)

documentation_agent = Agent(
    role="Development software documentation",
    goal="Provide a Readme.md to document the technical software documentation and how to use it. Describe what the user can do with the software and how to use the frontend and its components.",
    backstory="""You are an expert for professional software documentation. You think about structure of the documentation. All documentation should be logic, clean and easy to read. """,
    #llm=llama31,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    allow_delegation=False,
    #tools=[requirement],
    verbose=True
)

test_agent = Agent(
    role="Software tester",
    goal="You will check that the code contains all requirements. Provide a test.md to document the check results. Generate a list of all requirements you can check.",
    backstory="""You are an professional tester by reading the requirements and comparing them with the implementation """,
    #llm=llama31,
    llm=ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    allow_delegation=False,
    #tools=[requirement],
    verbose=True
)

managementTask = Task(
    description=developmentProject,
    expected_output="Provide a list of tasks to complete the software development project",
    #human_input=True,
    agent=codeing_agent
)

codingTask = Task(
    description=f"Start implementing the task bases on the existing feedback of manager, reviewer and designer. ",
    expected_output="Just provide the full code without any explanation as index.html to be opened with a browser. ONLY SOURCE CODE NO ADDITIONAL MARKS, TEXT OR COMMENTS",
    output_file="public/index.html",
    agent=codeing_agent
)


reviewTask = Task(
    description="Do a proper code review from the coding agent results and share your suggestion to improve the code",
    expected_output="""Explain one most important suggestion to improve the code in markdown format""",
    output_file="markdown/review.md",
    context=[codingTask],
    agent=codereview_agent
)


designerTask = Task(
    description="Think about optimising the design. Provide one suggestion to improve design, layout or usability of the frontend",
    expected_output="""Explain one most important suggestion to improve the code in markdown format""",
    output_file="markdown/uiux.md",
    context=[codingTask],
    agent=uiux_agent
)


documentationTask = Task(
    description="Think about what is needed to be documented. Be specific with naming. Guide the user how to use the software. Provide nessescary hints for the user he needs to be aware of",
    expected_output="""Provide the documentation in typical Readme.md markdown format""",
    output_file="markdown/readme.md",
    context=[codingTask],
    agent=documentation_agent
)

testTask = Task(
    description="Generate a list af all needed features based on the requirements. Check for everything in your list if you will find a proper implementation in the code. Provide a checkmark for each completed featuren, a cross for missing and a questionmak if you are not sure",
    expected_output="""Provide the test check list in markdown format""",
    output_file="markdown/test.md",
    context=[codingTask],
    agent=test_agent
)

crew = Crew(
    agents=[manager, codeing_agent, codereview_agent, uiux_agent],
    tasks=[managementTask, codingTask,  reviewTask, designerTask,  documentationTask, testTask],
    #tasks=[managementTask, codingTask1],
    process=Process.sequential,
    verbose=True
)


def crewLoop(developmentProject, managementTask, codingTask, crew):
    result = ""
    loop = 0
    for subtask in developmentProjectSubTask:
        loop = loop +1
        implementation = ""
        developmentProject = developmentProject+subtask
        f_out1 = open(f"markdown/requirement{loop}.md", "w+")
        f_out1.write(developmentProject)
        f_out1.close()

        try: 
            f = open("public/index.html", "r") 
            implementation = f.read()
            print(implementation)
        except Exception as e: 
            print(e)

        readme = ""
        try: 
            f = open(f"markdown/Readme{loop}.md", "r")
            readme = f.read()
            print(readme)
        except Exception as e: 
            print(e)

        review = ""
        try: 
            f = open(f"markdown/review{loop}.md", "r")
            review = f.read()
            print(review)
        except Exception as e: 
            print(e)

        uiux = ""
        try: 
            f = open(f"markdown/uiux{loop}.md", "r")
            uiux = f.read()
            print(uiux)
        except Exception as e: 
            print(e)

        managementTask.description = f"""Use and always stick with the following requirements: 
        ### Requirement
        {developmentProject}
        ### Reference implementation README.md:
        {readme} 
        ### Reference implementation CODE:
        {implementation}
        """

        codingTask.description=f"""Start implementing the task bases on the existing feedback of manager, reviewer and desigener. 
        {managementTask.description}
        ### Code Review:
        {review}
        ### Design UI/UX Review:
        {uiux}
        """
        result = crew.kickoff()
        implementation = ""
        cleanupSourceCode(loop)

    return result


def cleanupSourceCode(loop):
    try:
        f_in = open("public/index.html", "r")
        implementation = f_in.read()
        print("File cleanup start:")
        print(implementation)
        implementation = implementation.replace("```html", "")
        implementation = implementation.replace("```", "")
        implementation = implementation.replace("my best complete final answer to the task.", "")
        f_out1 = open("public/index.html", "w+")
        f_out2 = open(f"public/index{loop}.html", "w+")
        f_out1.write(implementation)
        f_out1.close()
        f_out2.write(implementation)
        f_out2.close()
        print("File cleanup done:")
        print(implementation)

    except Exception as e:
        print(e)


result = crewLoop(developmentProject, managementTask, codingTask, crew)
print(result)







