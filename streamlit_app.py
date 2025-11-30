import streamlit as st
import os
from openai import OpenAI

# Page config
st.set_page_config(page_title="LLM Council", page_icon="🏛️", layout="wide")

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

# Council members configuration
COUNCIL_MEMBERS = [
    {"name": "Optimist", "model": "anthropic/claude-3.5-sonnet", "color": "#4CAF50"},
    {"name": "Pessimist", "model": "anthropic/claude-3.5-sonnet", "color": "#F44336"},
    {"name": "Realist", "model": "anthropic/claude-3.5-sonnet", "color": "#2196F3"},
    {"name": "Creative", "model": "anthropic/claude-3.5-sonnet", "color": "#9C27B0"},
]

def get_council_response(question, member):
    """Get response from a council member"""
    system_prompts = {
        "Optimist": "You are an optimistic advisor. Focus on opportunities, positive outcomes, and encouraging perspectives.",
        "Pessimist": "You are a pessimistic advisor. Focus on risks, potential problems, and cautionary perspectives.",
        "Realist": "You are a realistic advisor. Focus on practical considerations, balanced views, and factual analysis.",
        "Creative": "You are a creative advisor. Focus on innovative ideas, unconventional approaches, and imaginative solutions.",
    }
    
    try:
        response = client.chat.completions.create(
            model=member["model"],
            messages=[
                {"role": "system", "content": system_prompts[member["name"]]},
                {"role": "user", "content": question}
            ],
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# UI
st.title("🏛️ LLM Council")
st.markdown("Ask a question and get perspectives from different council members")

# Question input
question = st.text_area("Enter your question:", height=100, placeholder="e.g., Should I start a new business?")

if st.button("Ask the Council", type="primary"):
    if question:
        with st.spinner("Consulting the council..."):
            cols = st.columns(len(COUNCIL_MEMBERS))
            
            for idx, member in enumerate(COUNCIL_MEMBERS):
                with cols[idx]:
                    st.markdown(f"### {member['name']}")
                    response = get_council_response(question, member)
                    st.markdown(f"<div style='background-color: {member['color']}22; padding: 15px; border-radius: 10px; border-left: 4px solid {member['color']};'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question first!")
