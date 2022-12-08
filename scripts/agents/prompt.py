# flake8: noqa
PREFIX = """Perform the following tasks as best you can. You have access to the following tools:"""
FORMAT_INSTRUCTIONS = """Use the following format:

Task: the input task you must accomplish
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I have now completed the task
Final Answer: the result that you have achieved"""
SUFFIX = """Begin!

Task: {input}"""
