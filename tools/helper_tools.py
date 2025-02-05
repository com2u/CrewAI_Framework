from langchain_openai import ChatOpenAI
from browser_use import Agent
from langchain_community.callbacks import get_openai_callback
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from pydantic import BaseModel
from browser_use.agent.views import ActionModel, ActionResult
from browser_use.browser.browser import Browser as Browser
from langchain_core.tools import tool 
from browser_use.agent.service import Agent as BrowseAgent
from crewai.tools import BaseTool
from pydantic import Field
from browser_use.agent.service import Agent as BrowseAgent
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from pydantic import Field, ConfigDict
import os
import asyncio

import yaml 

# with open("creds.yml", "r") as file:
#    config = yaml.safe_load(file)

#OPENROUTER_API_KEY = config["OPENROUTER_API_KEY"]["api_key"]
load_dotenv()
try:
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
    os.environ["OPENROUTER_MODEL_NAME"] = os.getenv("OPENROUTER_MODEL_NAME")
    os.environ["OPENROUTER_BASE_URL"] = os.getenv("OPENROUTER_BASE_URL")
    print("## API Keys loaded")
except KeyError:
    print("Error: Data not found in environment variables. (.env)")
    

LLM = ChatOpenAI(model=os.getenv("OPENROUTER_MODEL_NAME"), api_key=os.getenv("OPENROUTER_API_KEY"), base_url=os.getenv("OPENROUTER_BASE_URL"))


# Initialize controller first
controller = Controller()

# Define parameters for dropdown selection
class SelectDropdownAction(BaseModel):
    index: int  # Index from selector_map
    option_value: str  # The value/label to select

async def _select_dropdown_by_xpath(xpath: str, option_value: str, browser):
    """Gets the Dropdowns"""
    page = await browser.get_current_page()
    try:
        dropdown = await page.wait_for_selector(f'xpath={xpath}', timeout=5000, state='visible')
        await dropdown.select_option(value=option_value)  # Always use value
    except Exception as e:
        raise Exception(f'Failed to select dropdown with xpath {xpath}. Error: {str(e)}')

@controller.action('Select dropdowns', param_model=SelectDropdownAction)
async def select_dropdown(params: SelectDropdownAction, browser: Browser):
    session = await browser.get_session()
    state = session.cached_state

    # Validate the index
    if params.index not in state.selector_map:
        raise Exception(
            f'Element with index {params.index} does not exist - retry or use alternative actions'
        )

    # Get the corresponding XPath or handle DOMElementNode
    element = state.selector_map[params.index]
    if isinstance(element, str):
        xpath = element  # Already a string
    elif hasattr(element, 'xpath'):
        xpath = element.xpath  # Extract XPath from the DOMElementNode
    else:
        raise Exception(f'Unexpected type for selector_map[{params.index}]: {type(element)}')

    print(f"Resolved XPath: {xpath}")

    # Call the `_select_dropdown_by_xpath` function
    try:
        await _select_dropdown_by_xpath(xpath, params.option_value, browser)
        return ActionResult(extracted_content=f'✅ Selected option {params.option_value} from dropdown {params.index}: {xpath}')
    except Exception as e:
        raise Exception(f'Failed to select option {params.option_value} from dropdown {params.index}. Error: {str(e)}')


import asyncio
from crewai import Agent, Task, Crew
import nest_asyncio
from pydantic import ConfigDict, Field

# Modify the BrowsingTool to use async-compatible method
class BrowsingTool(BaseTool):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        protected_namespaces=()
    )

    name: str = "WebBrowsing"
    description: str = "Browse and scrape the internet based on given instructions."
    
    async def _arun(self, instructions: str) -> str:
        """
        Async method for running the browsing agent
        """
        try:
            # Create a new agent with the specific instructions
            current_agent = BrowseAgent(
                task=instructions,
                llm=LLM,
                controller=controller
            )

            # Run the agent
            result = await current_agent.run()
            
            return str(result)
        except Exception as e:
            return f"Error performing web browsing: {str(e)}"

    def _run(self, instructions: str) -> str:
        """
        Sync fallback method that should work in most environments
        """
        async def run_async():
            return await self._arun(instructions)
        
        # Check if there's a running event loop
        try:
            loop = asyncio.get_running_loop()
            return loop.run_until_complete(run_async())
        except RuntimeError:
            # No running event loop, use asyncio.run()
            return asyncio.run(run_async())
