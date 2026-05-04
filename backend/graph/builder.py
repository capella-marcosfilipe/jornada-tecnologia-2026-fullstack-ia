from langgraph.graph import StateGraph, END
from langgraph.graph.state import CompiledStateGraph
from backend.graph.state import AgentState
from backend.graph.nodes.vision_node import VisionNode
from backend.graph.nodes.reasoning_node import ReasoningNode


# Inicialização de Nós
reasoning_node = ReasoningNode()
vision_node = VisionNode()


def build_graph() -> CompiledStateGraph:
    # Montagem do Grafo
    graph = StateGraph(AgentState)

    graph.add_node("vision", vision_node.execute)
    graph.add_node("reasoning", reasoning_node.execute)

    graph.set_entry_point("vision")
    graph.add_edge("vision", "reasoning")
    graph.add_edge("reasoning", END)

    # Compilação (Pronto para uso)
    app_graph = graph.compile()
    
    return app_graph