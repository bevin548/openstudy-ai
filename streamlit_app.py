import streamlit as st

st.set_page_config(
    page_title="OpenStudy AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 OpenStudy AI")
st.write("Your open-source AI study assistant")

st.divider()

topic = st.text_input(
    "What topic do you want to study?",
    placeholder="Example: Python, Mathematics, Biology..."
)

if st.button("Create Study Guide"):
    if topic:
        st.subheader(f"📖 Study Guide: {topic}")

        st.write("### 1. Learn the basics")
        st.write(f"Start by understanding the fundamental concepts of {topic}.")

        st.write("### 2. Practice")
        st.write(f"Create practice questions about {topic}.")

        st.write("### 3. Review")
        st.write(f"Review the important points you learned about {topic}.")

        st.success("Study guide created!")
    else:
        st.warning("Please enter a topic first.")
