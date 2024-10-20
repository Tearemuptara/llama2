# Taking a note of example script format for tool binding

def tool_fun():
    """
    If (conditions = true) then use this tool.
    """
print("Tool used!")

def tool_not_fun():
    """
    If (conditions = false) then use this tool.
    """
print("Tool NOT used!")

tools = [tool_fun, tool_not_fun]