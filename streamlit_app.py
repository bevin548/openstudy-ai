import streamlit as st
import anthropic

st.set_page_config(
    page_title="OpenStudy AI",
    page_icon="📚"
)

st.title("📚 OpenStudy AI")
st.write("Your open-source Claude-powered study assistant")

api_key = st.secrets.get("ANTHROPIC_API_KEY")

if not api_key:
    st.warning("Claude API key is not configured yet.")
    st.info("Add ANTHROPIC_API_KEY to Streamlit Secrets to enable AI features.")
    st.stop()

client = anthropic.Anthropic(api_key=api_key)

topic = st.text_input(
    "What do you want to study?",
    placeholder="Example: Python, Mathematics, Biology..."
)

if st.button("Ask Claude"):
    if topic:
        with st.spinner("Claude is creating your study guide..."):
            response = client.messages.create(
                model="claude-sonnet-5",
                max_tokens=1500,
                messages=[
                    {
                        "role": "user",
                        "content": f"""
Create a helpful study guide for: {topic}

Include:
1. Simple explanation
2. Key concepts
3. Three practice questions
4. A short revision plan

Explain everything clearly for a student.
"""
                    }
                ]
            )

        answer = next(
            block.text
            for block in response.content
            if block.type == "text"
        )

        st.markdown(answer)
    else:
        st.warning("Please enter a topic first.")
