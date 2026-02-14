from langgraph.graph import StateGraph, END
from .state import ResearchState
from .agents.planner import PlannerAgent
from .agents.retriever import RetrieverAgent
from .agents.synthesizer import SynthesizerAgent
from .agents.editor import EditorAgent
from .agents.critical_analysis import CriticalAnalysisAgent
from .agents.debunker import DeBunkerAgent
from .agents.insight import InsightAgent
from .config import Config

def increment_loop(state: ResearchState) -> dict:
    current_loop = state.get("loop_count", 0)
    print(f"--- LOOP INCREMENT ({current_loop + 1}) ---")
    return {"loop_count": current_loop + 1}

def check_contradiction(state):
    loop_count = state.get("loop_count", 0)
    max_loops = state.get("max_loops", 2)
    top_contradiction = state.get("top_contradiction")
    
    # If we have a critical contradiction and haven't hit max loops
    if top_contradiction and loop_count < max_loops:
        print(f"Contradiction found. Entering loop {loop_count + 1}")
        return "increment_loop"
    
    print("No critical contradiction or max loops reached. Proceeding to De-Bunker.")
    return "debunker"

def create_graph():
    # Initialize agents
    planner = PlannerAgent()
    retriever = RetrieverAgent()
    synthesizer = SynthesizerAgent()
    critical_analysis = CriticalAnalysisAgent()
    debunker = DeBunkerAgent()
    insight = InsightAgent()
    editor = EditorAgent()

    # Create graph
    workflow = StateGraph(ResearchState)

    # Add nodes
    workflow.add_node("planner", planner.run)
    workflow.add_node("retriever", retriever.run)
    workflow.add_node("synthesizer", synthesizer.run)
    workflow.add_node("critical_analysis", critical_analysis.run)
    workflow.add_node("increment_loop", increment_loop)
    workflow.add_node("debunker", debunker.run)
    workflow.add_node("insight", insight.run)
    workflow.add_node("editor", editor.run)

    # Define edges
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "retriever")
    workflow.add_edge("retriever", "synthesizer")
    workflow.add_edge("synthesizer", "critical_analysis")
    
    # Conditional logic
    workflow.add_conditional_edges(
        "critical_analysis",
        check_contradiction,
        {
            "increment_loop": "increment_loop",
            "debunker": "debunker"
        }
    )
    
    workflow.add_edge("increment_loop", "planner")
    workflow.add_edge("debunker", "insight")
    workflow.add_edge("insight", "editor")
    workflow.add_edge("editor", END)

    # Compile
    app = workflow.compile()
    return app
