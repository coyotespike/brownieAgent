from typing import Dict
from brownie import *
import sys

class ContractCaller:
    methods: Dict[str, str]
    contract: Contract

    def __init__(self, contract_name, contract_address, methods):
        self.methods = methods

        # Using only the contract name as a string, we can get the contract class
        contract_class = getattr(sys.modules[__name__], contract_name)
        try:
            # If the contract is already deployed, we can get it by address
            self.contract = contract_class.at(contract_address)
        except:
            # If the contract is not deployed, we deploy it
            tx = contract_class.deploy({'from': accounts[0]})
            print(f"Deployed {contract_name} to {tx.address}")

            self.contract = contract_class.at(tx)


    def call(self, method_name, *args):
        method = self.methods[method_name]
        # using the method name, we can get the method from the contract
        # and call it with the given arguments
        return getattr(self.contract, method)(*args)

