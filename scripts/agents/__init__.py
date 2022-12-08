# This enables local development of agents
# Must be initialized before importing any agents

MODULE_PATH = "/Users/timothy/Documents/1Projects/ML/langchain/langchain/__init__.py"
MODULE_NAME = "langchain"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

from .FirstAgent import FirstAgent
from .SecondAgent import SecondAgent

__all__ = [
    "FirstAgent",
    "SecondAgent",
]
