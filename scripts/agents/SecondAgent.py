from .prompt import PREFIX, SUFFIX, FORMAT_INSTRUCTIONS
from .ZeroShotAgent import ZeroShotAgent
from langchain import LLMChain, OpenAI
from langchain.agents import Tool
from brownie import *

import dotenv

dotenv.load_dotenv()

from .ContractCaller import ContractCaller


def SecondAgent():
    contract_caller = ContractCaller("Counter", "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87", {"inc": "increment", "dec": "decrement", "get": "getCount"})
    account_object = {'from': accounts[0]}
    tools = [
        Tool(name = "inc",
             func = lambda _x: contract_caller.call("inc", account_object),
             description = "Increment the counter",
             ),
        Tool(name = "dec",
             func = lambda _x: contract_caller.call("dec", account_object),
             description = "Decrement the counter",
             ),
        Tool(name = "get",
             func = lambda _x: contract_caller.call("get"),
             description = "Get the counter value",
             ),
    ]
    prompt = ZeroShotAgent.create_prompt(
        tools,
        prefix=PREFIX,
        suffix=SUFFIX,
        format_instructions=FORMAT_INSTRUCTIONS,
        input_variables=["input"],
    )

    llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)


    agent.run("Check the current value of the counter. If it is ever 0 or 25, you don't need to do anything. If it is not 0 or 25, increment it until it is 25. Check your work at the end. If it is ever 0, you can also stop.")


def main():
    SecondAgent()
