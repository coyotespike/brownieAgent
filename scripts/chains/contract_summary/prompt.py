# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

prompt = """
{contract}

Given the contract above, find all the ways to interact with it. For each way you find, return the "method name" and "method description" in the following format:

[ ["method_name_1", "method_name_2"],
  [
      Tool(name = "method name_1",
           func = lambda _x: contract_caller.call("method name_1", account_object),
           description = "method description 1",
           ),
      Tool(name = "method name",
           func = lambda _x: contract_caller.call("method name_2", account_object),
           description = "method description 2",
           )]]

Remember to close the Python list with the closing square brackets.

Begin!
"""

PROMPT = PromptTemplate(
    input_variables=["contract"], template=prompt
)
