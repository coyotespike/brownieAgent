# Brownie Agent

Run `brownie run scripts/Competition.py`

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

