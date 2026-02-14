import streamlit as st
import asyncio
import os
import time
from dotenv import load_dotenv
from src.graph import create_graph
from src.config import Config
from src.state import ResearchState
from langchain_community.callbacks import get_openai_callback

# Load environment
load_dotenv(".env")
load_dotenv("config.env", override=True)

st.set_page_config(page_title="Agentic Researcher", layout="wide")

st.title("🕵️‍♂️ Agentic Research Engine")


# Session State Initialization
if "is_running" not in st.session_state:
    st.session_state.is_running = False

def stop_research():
    st.session_state.is_running = False

def format_time(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}m {remaining_seconds}s"

# Sidebar
with st.sidebar:
    st.header("Configuration")
    model = st.selectbox("LLM Model", [Config.LLM_MODEL, "gpt-4o", "gpt-3.5-turbo"])
    st.info(f"Using: {model}")
    
    st.divider()
    st.header("Controls")
    if st.button("🛑 Stop Research", on_click=stop_research, type="secondary"):
        st.warning("Stopping research...")

    st.divider()
    st.header("📊 Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        metric_time = st.empty()
    with col2:
        metric_tokens = st.empty()
    
    st.divider()
    st.subheader("Tool Usage")
    col4, col5, col6 = st.columns(3)
    with col4:
        metric_tavily = st.empty()
    with col5:
        metric_wiki = st.empty()
    with col6:
        metric_arxiv = st.empty()
    
    # Initialize placeholders with 0
    metric_time.metric("⏱️ Time", "0s")
    metric_tokens.metric("🪙 Tokens", "0")
    metric_tavily.metric("🌐 Tavily", "0")
    metric_wiki.metric("📖 Wiki", "0")
    metric_arxiv.metric("📜 Arxiv", "0")

query = st.text_input("Enter your research question:", placeholder="e.g., Is coffee good for you?")
start_btn = st.button("Start Research", type="primary")

# Main Content Area
main_placeholder = st.empty()

async def run_research(user_query):
    st.session_state.is_running = True
    graph = create_graph()
    initial_state = {
        "query": user_query,
        "claims": [],
        "context": [],
        "contradictions": [],
        "insights": [],
        "hallucination_flags": [],
        "loop_count": 0,
        "max_loops": Config.MAX_LOOPS,
        "logs": [],
        "tool_usage": {"tavily": 0, "wikipedia": 0, "arxiv": 0}
    }
    
    # Use the main placeholder for all output
    with main_placeholder.container():
        status_text = st.empty()
        status_bar = st.progress(0)
        log_area = st.empty()
        
        accumulated_state = initial_state.copy()
        start_time = time.time()
        
        with get_openai_callback() as cb:
            status_text.text("Initializing workflow...")
            full_logs = []
            
            async for output in graph.astream(initial_state):
                # STOP CHECK
                if not st.session_state.is_running:
                     full_logs.append("🛑 Research Stopped by User.")
                     status_text.text("Stopped.")
                     log_area.code("\n".join(full_logs))
                     return accumulated_state

                # Update Time
                elapsed = time.time() - start_time
                metric_time.metric("⏱️ Time", format_time(elapsed))
                
                # Update Tokens
                metric_tokens.metric("🪙 Tokens", cb.total_tokens)
                
                for node_name, state_update in output.items():
                    accumulated_state.update(state_update)
                    
                    # Update Tool Metrics
                    usage = accumulated_state.get("tool_usage", {})
                    metric_tavily.metric("🌐 Tavily", usage.get("tavily", 0))
                    metric_wiki.metric("📖 Wiki", usage.get("wikipedia", 0))
                    metric_arxiv.metric("📜 Arxiv", usage.get("arxiv", 0))
                    
                    # Capture Logs
                    new_logs = state_update.get("logs", [])
                    
                    if node_name == "planner":
                        msg = "✅ Planner: Strategy generated."
                        full_logs.append(msg)
                        status_bar.progress(10)
                        
                    elif node_name == "retriever":
                        docs = state_update.get("documents", [])
                        count = len(docs)
                        msg = f"✅ Retriever: Fetched {count} documents."
                        full_logs.append(msg)
                        status_bar.progress(30)
                        
                    elif node_name == "synthesizer":
                        msg = f"✅ Synthesizer: Processed claims."
                        full_logs.append(msg)
                        for l in new_logs:
                            full_logs.append(f"   - {l}")
                        status_bar.progress(50)
                        
                    elif node_name == "critical_analysis":
                        contras = state_update.get("contradictions", [])
                        msg = f"✅ Analyst: Found {len(contras)} contradictions."
                        full_logs.append(msg)
                        status_bar.progress(70)
                        
                        if state_update.get("top_contradiction"):
                                full_logs.append("⚠️ Loop: Contradiction too high, researching again...")

                    elif node_name == "debunker":
                        flags = state_update.get("hallucination_flags", [])
                        msg = f"✅ De-Bunker: {len(flags)} hallucinations flagged."
                        full_logs.append(msg)
                        for l in new_logs:
                            full_logs.append(f"   - {l}")
                        status_bar.progress(85)

                    elif node_name == "insight":
                        msg = "✅ Insight Agent: Synthesis complete."
                        full_logs.append(msg)
                        status_bar.progress(90)

                    elif node_name == "editor":
                        msg = "✅ Editor: Report generated."
                        full_logs.append(msg)
                        status_bar.progress(95)
                        accumulated_state["report"] = state_update.get("report")
                    
                    if full_logs:
                        status_text.text(full_logs[-1])
                    log_text = "\n".join(full_logs)
                    log_area.code(log_text)

            status_bar.progress(100)
            return accumulated_state

if start_btn and query:
    main_placeholder.empty() # Clear previous results
    st.session_state.is_running = True # Set running flag
    
    with st.spinner("Researching..."):
        try:
            final_state = asyncio.run(run_research(query))
        except RuntimeError:
             loop = asyncio.new_event_loop()
             asyncio.set_event_loop(loop)
             final_state = loop.run_until_complete(run_research(query))
        
        st.session_state.is_running = False # Reset flag when done
        
        if final_state:
            with main_placeholder.container():
                if final_state.get("report"):
                    st.success("Analysis Complete")
                else:
                    st.warning("Analysis Stopped / Incomplete")
                
                tab1, tab2, tab3 = st.tabs(["📄 Final Report", "🔍 Claims", "⚠️ Contradictions"])
                
                with tab1:
                    st.markdown(final_state.get("report", "No report generated."))
                
                with tab2:
                    claims = final_state.get("claims", [])
                    st.subheader(f"Extracted {len(claims)} Claims")
                    for i, c in enumerate(claims):
                        with st.expander(f"{i+1}. {c.get('claim_text')[:80]}..."):
                            st.write(f"**Full Claim:** {c.get('claim_text')}")
                            st.write(f"**Source:** {c.get('source')}")
                            st.write(f"**Confidence:** {c.get('confidence')}")

                with tab3:
                    contras = final_state.get("contradictions", [])
                    st.subheader(f"Identified {len(contras)} Contradictions")
                    if not contras:
                        st.info("No contradictions found.")
                    for i, c in enumerate(contras):
                        st.error(f"**Conflict:** {c.get('claim_1')} vs {c.get('claim_2')}")
                        st.write(f"**Reasoning:** {c.get('reasoning')}")

else:
    with main_placeholder.container():
        st.info("Ready to research. Enter a query and click Start.")
