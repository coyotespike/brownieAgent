MODULE_PATH = "/Users/timothy/Documents/1Projects/ML/langchain/langchain/__init__.py"
MODULE_NAME = "langchain"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


from .base import ContractSummaryChain

from langchain.llms import OpenAI

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

bash_chain = ContractSummaryChain(llm=llm, verbose=True)
bash_chain.run({'contract': text})

