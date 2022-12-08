# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

prompt = """
{contract}

Given the contract above, find all the ways to interact with it. For each way you find, return the "method name" and "method description" in the following format:

    tools = [
        Tool(name = "method name",
             func = lambda _x: contract_caller.call("method name", account_object),
             description = "method description",
             ),
]

Begin!
"""

PROMPT = PromptTemplate(
    input_variables=["contract"], template=prompt
)
