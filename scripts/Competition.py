from .agents import ( FirstAgent, SecondAgent )
from threading import Thread


def main():
    # FirstAgent()
    contract_address = '0x6951b5Bd815043E3F842c1b026b0Fa888Cc2DD85'
    competitionThreads = [
        Thread(target=FirstAgent, args=(contract_address,)),
        Thread(target=SecondAgent, args=(contract_address,))
    ]

    for thread in competitionThreads:
        thread.start()

    for thread in competitionThreads:
        thread.join()
