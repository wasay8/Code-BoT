import requests
import json
import streamlit as st

# API URL
url = "http://localhost:11434/api/generate"

# Headers for the API request
headers = {
    'Content-Type': 'application/json'
}

# History list to maintain prompts
history = []

# Function to generate a response from the API
def generate_response(prompt):
    # Add the new prompt to the history
    history.append(prompt)
    # Create a final prompt by joining history with newlines
    final_prompt = "\n".join(history)

    # Data payload for the API request
    data = {
        "model": "codebot",
        "prompt": final_prompt,
        "stream": False
    }

    # Make a POST request to the API
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # If the response is successful, return the response from the API
    if response.status_code == 200:
        data = response.json()
        actual_response = data['response']
        return actual_response
    else:
        st.error(f"Error: {response.text}")
        return None

# Streamlit app
st.set_page_config(page_title="Coding Bot", page_icon="🦜")
st.title("Coding Bot : Generating programs")

# Text area input for the prompt
prompt = st.text_area("Enter your Prompt", height=200)

# Button to trigger the response generation
if st.button("Generate Response"):
    with st.spinner("generating"):
        if prompt:
            # Call the function to generate a response
            response = generate_response(prompt)
            
            
            # Display the response if it's not None
            if response:
                st.write("Response:")
                st.write(response)
        else:
            st.warning("Please enter a prompt.")
