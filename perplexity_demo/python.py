"""
The python node is responsible for executing python code.
"""

from langchain_core.runnables import RunnableConfig

from perplexity_demo.state import AgentState

async def python_node(state: AgentState, config: RunnableConfig): # pylint: disable=unused-argument
    """
    The python node is responsible for executing python code.
    """

