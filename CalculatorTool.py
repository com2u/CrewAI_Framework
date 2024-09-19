from langchain_community.tools import tool


@tool("Calculate")
def calculate(sourcecode: str):
    """ the sourcecode for the coding task """

    return eval(sourcecode)

@tool("Requirement")
def requirement(tasklist: str) -> str:
    """ the sourcecode for the coding task """

    return tasklist

@tool("Code")
def code(sourcecode: str) -> str:
    """ the sourcecode for the coding task """

    return sourcecode