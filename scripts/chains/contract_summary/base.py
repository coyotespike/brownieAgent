from typing import Dict, List

from pydantic import BaseModel, Extra

from langchain.chains.base import Chain
from langchain.chains.llm import LLMChain
from langchain.input import print_text
from langchain.llms.base import LLM
from langchain.utilities.bash import BashProcess

import prompt


class ContractSummaryChain(Chain, BaseModel):
    """Chain that interprets a prompt and executes bash code to perform bash operations.

    Example:
        .. code-block:: python

            from langchain import LLMBashChain, OpenAI
            llm_bash = LLMBashChain(llm=OpenAI())
    """

    llm: LLM
    """LLM wrapper to use."""
    input_key: str = "contract"  #: :meta private:
    output_key: str = "answer"  #: :meta private:

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid
        arbitrary_types_allowed = True

    @property
    def input_keys(self) -> List[str]:
        """Expect input key.

        :meta private:
        """
        return [self.input_key]

    @property
    def output_keys(self) -> List[str]:
        """Expect output key.

        :meta private:
        """
        return [self.output_key]

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        llm_executor = LLMChain(prompt=prompt.PROMPT, llm=self.llm)
        bash_executor = BashProcess()
        if self.verbose:
            print_text(inputs[self.input_key])

        summary = llm_executor.predict(contract=inputs[self.input_key])
        if self.verbose:
            print_text("\nAnswer: ")
            print_text(summary, color="green")

        else:
            raise ValueError(f"unknown format from LLM: {summary}")
        return {self.output_key: summary}

