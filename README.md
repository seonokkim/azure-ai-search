# Azure AI Search

This repository showcases the integration of **Azure OpenAI** services with **Gradio** to create interactive web applications for text and image processing.

## Features
- **Gradio**: Provides an easy-to-use UI for deploying AI models.
- **Azure OpenAI**: Powers the backend with advanced text and image generation capabilities.
- **Web Application Example**: Interactive chatbot using Azure OpenAI.


## Dataset Source
The dataset on Namhae-gun's tourist attractions (2022) is provided by **Namhae-gun, Gyeongsangnam-do** via the [Korea Open Government Data Portal](https://www.data.go.kr/data/15110855/fileData.do?recommendDataYn=Y). It includes multilingual information such as names, addresses, coordinates, and contact details.


## Project Structure
   ```bash
   ├── dataset/           # Contains example datasets used in the project
   ├── demo/              # Includes media for showcasing the project
   │   └── demo.png       # Screenshot of the Gradio-based chatbot
   ├── gradio-chatbot.py  # Main script for running the Gradio application
   ```

## Demo
Below is a preview of the chatbot UI built using Gradio and Azure AI:

![Demo Screenshot](demo/demo.png)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/azure-ai-search.git
   cd azure-ai-search
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
    
3. Set up your Azure OpenAI credentials:
- Obtain an API key and endpoint from your Azure OpenAI subscription.
   ```bash
   AZURE_OPENAI_KEY=your_azure_openai_api_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   ```
4. Run the Gradio application:
   ```bash
   python gradio-chatbot.py
   ```

## License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the license terms.

## Acknowledgments
- [OpenAI](https://openai.com/) for their cutting-edge AI models.
- [Gradio](https://gradio.app/) for the intuitive UI framework.
- [Azure](https://azure.microsoft.com/) for hosting and API support.

