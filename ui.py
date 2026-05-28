import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Analyzer", 
    layout="centered"
    )

st.title("AI YouTube Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("Enter YouTube video URL:")   
button= st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing video..."):
        try:
            analysis = agent.run(video_url)
            st.markdown("### Analysis Results:")
            st.markdown(analysis.content)
        except Exception as e:
            st.error(f"Error analyzing video: {e}")