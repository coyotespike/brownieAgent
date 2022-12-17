MODULE_PATH = "/Users/timothy/Documents/1Projects/ML/langchain/langchain/__init__.py"
MODULE_NAME = "langchain"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


# Import the built-in `open` function to open a file
from builtins import open

# from .base import ContractSummaryChain
import base

from langchain.llms import OpenAI
from langchain.agents import Tool

import dotenv

dotenv.load_dotenv()

llm = OpenAI(temperature=0)
text = """
//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

contract Counter {
    using SafeMath for uint256;
    uint256 public count;

    function increment() public {
        count.add(1);
    }

    function decrement() public {
        count.sub(1);
    }

    function reset() public {
        count = 0;
    }

    function getCount() public view returns (uint256) {
        return count;
    }

    function setCount(uint256 _count) public {
        count = _count;
    }
}
"""
# Specify the filepath
filepath = '/Users/timothy/Documents/1Projects/Solidity/brownie-counter/contracts/Counter.sol'

# Open the file in read-only mode
with open(filepath, 'r') as file:
    # Read in the entire contents of the file
    file_contents = file.read()
    # Print the contents of the file
    print(file_contents)
    text = file_contents


bash_chain = base.ContractSummaryChain(llm=llm, verbose=True)
output = bash_chain.run({'contract': text})
tools = eval(output)
print(tools)
