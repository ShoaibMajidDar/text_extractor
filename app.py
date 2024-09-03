import asyncio
import streamlit as st

from controller.response_from_llm import get_response_from_llm
from controller.upload_pdf import get_text_from_pdf

async def main():

    if 'response' not in st.session_state:
        st.session_state.response = None

    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    if uploaded_file is not None:
        pdf_text = get_text_from_pdf(uploaded_file)

        if st.button("Save PDF Text to File"):
            with open("text_file.txt", "w", encoding="utf-8") as text_file:
                text_file.write(pdf_text)
            st.success("PDF text saved to 'pdf_text.txt'.")
        
        model = st.selectbox(
                                "Select a model",
                                ("gpt-4o-mini", "gpt-3.5-turbo-0125", "gpt-4-turbo"),
                            )

        prompt = st.text_input("Enter the prompt")

        if model and prompt:
            st.write(await get_response_from_llm(pdf_text, model, prompt))

if __name__ == "__main__":
    asyncio.run(main())
