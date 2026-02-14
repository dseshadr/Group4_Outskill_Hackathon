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
**Status**: ⬜ Not Started
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
**Status**: ⬜ Not Started
**Objective**: Enhance reasoning depth and handling of complex queries.
**Requirements**: 
- Implement Critical Analysis Agent (Claim comparison).
- Implement Contradiction Loop Logic (Re-search trigger).
- Implement De-Bunker Agent (Fact-checking).
- Implement Insight Generation Agent.
- UI Layer (Streamlit/Graphviz/Mermaid).

### Phase 3: Performance & Scale
**Status**: ⬜ Not Started
**Objective**: Optimize for speed, cost, and reliability.
**Requirements**: 
- Parallelize retrieval and processing.
- Token optimization (compression, deduplication).
- Observability Dashboard (Latency, Costs).
- Failure resilience (Retries, Fallbacks).

### Phase 4: Platform Maturity
**Status**: ⬜ Not Started
**Objective**: Refine UX and add platform features.
**Requirements**: 
- Research controls (Breadth/Depth, Filters).
- Report export (PDF/MD/JSON).
- Persistent Knowledge Base (Optional).
- UI Polish (Dark theme, transitions).

### Phase 5: Advanced Reasoning (Optional)
**Status**: ⬜ Not Started
**Objective**: "Secret Sauce" / Advanced critical thinking.
**Requirements**: 
- Devil's Advocate Mode (Insight Agent toggle).
