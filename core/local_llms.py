import requests, json
from llama_index.schema import TextNode
from llama_index import  SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
from llama_index.node_parser.text.sentence import SentenceSplitter


def llm_request(prompt, url:str='http://localhost:11434/api/generate', model:str='mistral'):

    # Gửi yêu cầu POST đến API
    response = requests.post(url, json={"model": model, "prompt": prompt})

    # Chuyển đổi byte thành list của dictionaries
    sub_responses = [json.loads(res) for res in response.text.strip().split('\n')]

    # Lặp qua tất cả các phản hồi và nối các phần "response" (nếu có)
    text_response = "".join(item["response"] for item in sub_responses if "response" in item)
    
    return text_response

# Function to perform the query and accumulate results


def prompt_generator(hints, user_query):
    _hints = ""
    for hint in hints:
        _hints += hint + "\n\n"  # Directly concatenate each string in hints
    prompt = f"""
    You are an AI assistant designed by the Vietnam Petroleum Institute. Answer the given question based on the context below. If the context doesn't have enough information, please reply "I don't have enough information"
    Context:
    {_hints}
    Question:
    {user_query}
    Assistant:
    """
    return prompt


def print_out_ans(user_query, final_ans, hints):
    _print_out = f"""
    Question: {user_query}
    Answer: {final_ans}
    """
    return _print_out