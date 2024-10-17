import google.generativeai as genai
import os
import re
import json
from dotenv import load_dotenv
from models.Document import DocumentResponse

load_dotenv()


def configurar_api():
    genai.configure(api_key=os.getenv('API_KEY'))
    return genai.GenerativeModel('gemini-1.5-flash')


def gerar_conteudo(model, file_path):
    sample_file = genai.upload_file(path=file_path)
    print(f"Upload '{sample_file.display_name}' as: {sample_file.uri}")

    file = genai.get_file(name=sample_file.name)
    print(f"Download file '{file.display_name}' as: {file.uri}")

    response = model.generate_content([
        file,
        "Search for the title of this file, try to simplify this document into 5 tags, "
        "find the name of the person who signed the document, and summarize what the "
        "document discusses, translate to portugues-brazil and return in json format"
    ])

    markdown_json_pattern = r"```json\n(.*?)\n```"
    match = re.search(markdown_json_pattern, response.text, re.DOTALL)

    json_content = match.group(1) if match else response.text
    response_dict = json.loads(json_content)
    return DocumentResponse(**response_dict)
