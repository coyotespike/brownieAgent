#!/usr/bin/python3

from brownie import *
import sys

from .ContractChain import ContractCaller

def main():
    try:
        while True:
            command = input("Enter command: ")
            # print(network.show_active())

            # contract_class = getattr(sys.modules[__name__], "Counter")
            # counter = contract_class.at("0x6951b5Bd815043E3F842c1b026b0Fa888Cc2DD85")
            # if command == "get":
            #     print(counter.getCount())
            # elif command == "inc":
            #     counter.increment({'from': accounts[0]})
            # elif command == "dec":
            #     counter.decrement({'from': accounts[0]})
            # elif command == "exit":
            #     print("Exiting...")
            #     exit(0)

            tx = Counter.deploy({'from': accounts[0]})
            print(tx)

            # contract_caller = ContractCaller("Counter", "", {"inc": "increment", "dec": "decrement", "get": "getCount"})

            # if command == "get":
            #     print(contract_caller.call("get"))
            # elif command == "inc":
            #     contract_caller.call("inc", {'from': accounts[0]})
            # elif command == "dec":
            #     contract_caller.call("dec", {'from': accounts[0]})
            # elif command == "exit":
            #     print("Exiting...")
            #     exit(0)



    except KeyboardInterrupt:
        print("\n[!] Ctrl+C detected, exiting gracefully.")
        exit(0)
