import operator
from typing import List, TypedDict, Annotated, Optional, Any

class ResearchState(TypedDict):
    query: str
    sub_questions: Annotated[List[str], operator.add]
    current_sub_questions: List[str] # Non-accumulating list for current loop
    documents: Annotated[List[dict], operator.add]  # content, metadata, source
    claims: Annotated[List[dict], operator.add]     # claim_text, confidence, sources
    contradictions: List[dict]
    top_contradiction: Optional[dict] # Logic Refactor: Single targeted resolution
    contradiction_confidence: float
    loop_count: int
    max_loops: int
    insights: List[str]
    hallucination_flags: List[dict]
    report: str
    stage: str
    logs: Annotated[List[str], operator.add]
    tool_usage: Annotated[dict, lambda a, b: {k: a.get(k, 0) + b.get(k, 0) for k in set(a) | set(b)}]
