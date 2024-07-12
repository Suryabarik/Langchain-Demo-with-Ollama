import requests
import streamlit as st

def get_ollama_response(endpoint, input_text):
    response = requests.post(f"http://localhost:8000/{endpoint}/invoke",
                             json={'input': {'topic': input_text}})
    
    # Print the response to debug
    print(response.json())
    
    response_data = response.json()
    
    # Check if 'output' key exists
    if isinstance(response_data, dict):
        if 'output' in response_data:
            return response_data['output']
        else:
            st.error(f"Unexpected response format: {response_data}")
            return None
    else:
        st.error(f"Response is not a dictionary: {response_data}")
        return None

st.title('Langchain Demo With Gamma API')

# Separate inputs for essay and poem
essay_topic = st.text_input("Write an essay on")
poem_topic = st.text_input("Write a poem on")

if essay_topic:
    st.write("Essay:")
    essay_response = get_ollama_response("essay", essay_topic)
    if essay_response:
        if isinstance(essay_response, str):
            st.write(essay_response)
        else:
            st.error("Unexpected essay response format.")
            
if poem_topic:
    st.write("Poem:")
    poem_response = get_ollama_response("poem", poem_topic)
    if poem_response:
        if isinstance(poem_response, str):
            st.write(poem_response)
        else:
            st.error("Unexpected poem response format.")
