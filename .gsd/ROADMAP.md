# ROADMAP.md

> **Current Phase**: Not started
> **Milestone**: v1.0

## Must-Haves (from SPEC)
- [ ] Multi-agent orchestration state machine (LangGraph)
- [ ] Vector retrieval (Tavily + Chroma/FAISS)
- [ ] Contradiction detection agent
- [ ] De-Bunker (Fact-Check) agent
- [ ] Structured report generation
- [ ] Transparent reasoning logs 

## Phases

### Phase 1: Core System Architecture (Foundation)
**Status**: ✅ Done
**Objective**: Build the orchestration engine and basic agent structure.
**Requirements**: 
- Implement LangGraph state machine.
- Define `GlobalState` model.
- Implement Planner Agent (Query breakdown).
- Implement Lead Investigative Researcher Agent (Tavily + Vector DB).
- Implement Data Integration Specialist Agent (Claims extraction).
- Technical Editor Agent (Basic report).
- Logging infrastructure for transparency.

### Phase 2: Intelligence & Contradiction Loop (Agent Expansion)
**Status**: ✅ Done
**Objective**: Enhance reasoning depth and handling of complex queries.
**Requirements**: 
- Implement Critical Analysis Agent (Claim comparison).
- Implement Contradiction Loop Logic (Re-search trigger).
- Implement De-Bunker Agent (Fact-checking).
- Implement Insight Generation Agent.
- UI Layer (Streamlit/Graphviz/Mermaid).

### Phase 3: Optimizations & Tool Integration
**Status**: ✅ Done
**Objective**: Improve efficiency and reduce API costs.
**Requirements**: 
- Smart Looping (Query Refinement).
- Integrate Wikipedia & Arxiv Tools.
- Rate Limit & Cost Optimization.

### Phase 4: Targeted Logic Refactor (User Request)
**Status**: ✅ Done
**Objective**: "Narrow and Deep" architecture for maximum cost efficiency.
**Requirements**: 
- Refactor Planner: 1 Tavily Search -> 5 Sub-questions.
- Refactor Retriever: 5 Searches -> 25 results + summaries.
- Refactor Synthesizer: Limit to Top 20 confident claims.
- Refactor Loop Logic: Single-threaded contradiction resolution.

### Phase 5: Advanced Reasoning (Optional)
**Status**: ⬜ Not Started
**Objective**: "Secret Sauce" / Advanced critical thinking.
**Requirements**: 
- Devil's Advocate Mode (Insight Agent toggle).
