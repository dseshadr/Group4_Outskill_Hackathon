# DECISIONS.md

## ADR-001: Orchestration Engine
- **Decision**: Use LangGraph.
- **Context**: Need a state machine for multi-agent coordination with deterministic state updates.
- **Consequences**: Requires structured state definitions and graph-based workflow design.

## ADR-002: Vector Database
- **Decision**: Chroma or FAISS.
- **Context**: Hackathon-optimized, quick deployment or local persistence.
- **Consequences**: Lightweight setup, sufficient for session-based research.

## ADR-003: Search Provider
- **Decision**: Tavily.
- **Context**: Optimized for LLM agents, reliable search results.
- **Consequences**: Dependency on Tavily API.
