import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import openai

load_dotenv()
api_key = os.getenv("api_key")

aclient = openai.AsyncOpenAI(api_key=os.getenv("api_key"))

async def get_response_from_llm(pdf_text, model, prompt):
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": pdf_text}
    ]

    response = await aclient.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content 