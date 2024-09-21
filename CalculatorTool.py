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

cleanupSourceCode(1)