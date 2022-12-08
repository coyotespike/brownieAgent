from .agents import ( FirstAgent, SecondAgent )
from threading import Thread


def main():
    competitionThreads = [
        Thread(target=FirstAgent),
        Thread(target=SecondAgent)
    ]

    for thread in competitionThreads:
        thread.start()

    for thread in competitionThreads:
        thread.join()
