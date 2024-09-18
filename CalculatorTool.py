from langchain_community.tools import tool


@tool("Calculate")
def calculate(sourcecode):
    """ the sourcecode for the coding task """

    return eval(sourcecode)

@tool("Requirement")
def requirement(tasklist):
    """ the sourcecode for the coding task """

    return eval(tasklist)