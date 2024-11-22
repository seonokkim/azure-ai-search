import os
import requests
import gradio as gr

# Azure OpenAI configuration - replace with your environment variables or config file
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT', 'https://your-endpoint.openai.azure.com')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY', 'your-api-key')
DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME', 'your-deployment-name')

# Global variable to store conversation history
history = []

def chatgpt_response(prompt):
    global history  # Use the global history variable
    headers = {
        'Content-Type': 'application/json',
        'api-key': AZURE_OPENAI_API_KEY,
    }
    
    # Prepare the conversation history
    messages = []

    # Add the system message
    messages.append({
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
    })

    # Add user messages and assistant replies from history (if any)
    for user_msg, assistant_msg in history:
        messages.append({
            "role": "user",
            "content": user_msg
        })
        messages.append({
            "role": "assistant",
            "content": assistant_msg
        })

    # Add the current user prompt
    messages.append({
        "role": "user",
        "content": prompt
    })

    # Payload for the API request
    payload = {
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 4096
    }

    # Send the request to the Azure OpenAI service
    try:
        response = requests.post(
            f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-08-01-preview",
            headers=headers,
            json=payload
        )

        # Parse the API response
        response.raise_for_status()
        result = response.json()
        bot_response = result['choices'][0]['message']['content'].strip()
        history.append((prompt, bot_response))  # Add the current conversation to history
        return bot_response, history
    except Exception as e:
        return f"Error: {e}", history

def reset_chat():
    """Clear the conversation history."""
    global history
    history = []  # Clear the global history
    return None

# Gradio interface setup
with gr.Blocks() as demo:
    gr.Markdown("<h1 align='center'>ChatGPT Demo</h1>")
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(show_label=False, placeholder="Type your message here...", scale=3)
    submit_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear")

    def handle_user_input(prompt):
        bot_response, updated_history = chatgpt_response(prompt)
        return updated_history, None

    # Button click events
    submit_btn.click(handle_user_input, [user_input], [chatbot, user_input])
    clear_btn.click(reset_chat, outputs=[chatbot])

demo.launch()
