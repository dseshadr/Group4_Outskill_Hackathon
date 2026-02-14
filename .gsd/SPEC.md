# SPEC.md — Project Specification

> **Status**: `FINALIZED`

## Vision
Build a multi-agent AI research engine capable of performing multi-hop, multi-source investigations with transparent reasoning, contradiction detection, and structured reporting. This system will serve as a production-grade research orchestration platform, prioritizing clarity, transparency, and stability over complexity.

## Goals
1.  **Multi-Agent Orchestration**: Implement a LangGraph-based state machine coordinating specialized agents (Planner, Retriever, Synthesizer, Analyst, De-Bunker, Insight, Editor).
2.  **Transparent Reasoning**: Ensure all agent actions, routing decisions, and contradiction resolutions involve structured state updates and logs visible to the user.
3.  **Contradiction Management**: Detect, graph, and attempt to resolve contradictions through targeted re-searching and loop logic.
4.  **Retrieval-Augmented Logic**: Base all claims on retrieved documents (Tavily) stored in a vector database (Chroma/FAISS) with source metadata.
5.  **Structured Output**: Generate comprehensive reports with citations, confidence scores, and identified limitations.

## Non-Goals (Out of Scope for Stage 1)
-   **Opaque LLM-only Generation**: No "magic" outputs without reasoning traces.
-   **Complex UI (Stage 1)**: Focus on backend logic and simple visualization first.
-   **Long-term Memory (Stage 1)**: Focusing on session-based research context initially.
-   **Overengineering**: Avoid unnecessary APIs or microservices; keep it modular but monolithic in execution flow.

## Users
-   **Researchers**: Needing deep, multi-perspective investigations.
-   **Judges/Evaluators**: validatig the system's transparency and reasoning capabilities.
-   **Developers**: Extending the modular agent system.

## Constraints
-   **Hackathon-Optimized**: Must be stable for demos.
-   **Deterministic State**: All agent transitions must be creating predictable state updates.
-   **Token Efficiency**: Prevent infinite loops and manage context windows.

## Success Criteria
- [ ] Answer multi-hop questions with retrieved evidence.
- [ ] Identify and graph contradictions in controversial topics.
- [ ] Trigger deep dive loops automatically upon low confidence.
- [ ] Validate claims against source documents (De-Bunker).
- [ ] Expose reasoning chain and agent state transparently.
- [ ] Produce structured, traceable reports.
