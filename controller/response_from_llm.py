import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai

load_dotenv()
api_key = os.getenv("api_key")

aclient = openai.AsyncOpenAI(api_key=os.getenv("api_key"))
# def get_response_from_llm(pdf_text, model, prompt):

#     llm = ChatOpenAI(
#     temperature=0, model=model, api_key=api_key
#     )
#     template = """
    # Instructions:
    # Task: Extract specific details from the provided text based on the user's query.
    # Answer strictly according to the user's question.
    # Do not infer or fabricate information. If the requested detail is not found in the text, state that it is not present.
    # Adhere to any specific format the user requests for the response.
# ==============================================
#     User Query: {prompt}
# ==============================================
#     Source Text: {pdf_text}
#     """
#     prompt = ChatPromptTemplate.from_template(template)

#     chain = prompt | llm | StrOutputParser()

#     res = chain.invoke({"prompt": prompt, "pdf_text": pdf_text})
#     print(template)
#     return res


async def get_response_from_llm(pdf_text, model, prompt):
    
    # template = """Instructions:
    # Task: Extract specific details from the provided text based on the user's query.
    # Answer strictly according to the user's question.
    # Do not infer or fabricate information. If the requested detail is not found in the text, state that it is not present.
    # Adhere to any specific format the user requests for the response."""

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": pdf_text}
    ]

    response = await aclient.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content 