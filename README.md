# Brownie Agent

It helps to run `brownie console`

Run `brownie run scripts/Competition.py`. It is a race condition between two agents to interact with a contract.

As you can see, currently, we manually build a ContractCaller for the agents.

To move to higher-level strategy, an agent should figure out its own commands.

Agent: EmailWriter
Task: Draft an email.

You have learned there is a smart contract named Counter, which holds a counter variable. You would like to find the current value of the counter, and if it is not 10 you would like to make the current value 10.

Goal: the goal you must accomplish
Thought: you should always think about what to do
Agent: the agent to task, should be one of [{agent_names}]
Agent Task:


When will this approach cease progressing toward the Diplomacy example?
And how will it incorporate, say, a day trading agent?
I need more complex contracts to figure it out.

Yeah, I'm not very motivated to make a higher-order agent to make the first agents interact with the contract.


# Thoughts
1. How to build my first utility or chain to interact with a contract?
2. Given a contract, output the methods to interact with it.
3. Then what? maybe it should be a simple chain like ReACT.
4. Or should it be like an agent with tools?

Is there too little value to a chain that takes in natural language and calls a contract method?
Like, I have to tell it which method to call!
How would that compose with another chain or agent that is thinking about strategy?

Read this file. List methods you can take.

method: get Tools

If you cannot finish the task, report that as your final answer.

Should I have a layer that decides to increment n times?
And then another layer which is called to figure out how to increment?

Or, do I tell it directly "here are your contract methods"?
Let's start there.
And then have it get-tools.

Part of problem is a conceptual confusion between agents and chains.

ReactAgent is using utilities directly.
MRKL uses chains, which use utilities.

Could ReactAgent be a chain then?

I will start as an agent. With hard-coded tools.
Then, a chain or an agent to get the tools. And the agent will have to figure out how to run the contract, maybe.

Yeah, MRKLChain uses only chains. And I don't want to hard-code a chain per contract.

Ideally, I can initialize an agent with the contract address and name, and some instructions.

It will figure out how to interact with the contract from there.

# Packages installed
conda install brownie (or maybe it was pipx??)
conda install python-dotenv
conda install -c conda-forge openai

# Technical Notes
If you run with `python` then relative paths do not work. They only work with brownie. No idea why.
