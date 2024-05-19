# StreamlitChatbot
![image](https://github.com/wytan12/StreamlitChatbot/assets/102575826/6a8ffccc-54f3-41e5-b2d1-27bdf3d84fee)

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:

   ```bash
   https://github.com/wytan12/StreamlitChatbot.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Obtain an API key from AzureChatOpenAI and add it to the .streamlit/secrets.toml file under the project directory:
   ```bash
   [AZURE_OPENAI]
   AZURE_OPENAI_API_VERSION = "XXXXXXXXX"
   AZURE_OPENAI_ENDPOINT="XXXXXXXXX"
   AZURE_OPENAI_APIKEY="XXXXXXXXX" 
   DEPLOYMENT_NAME = "XXXXXXXXX"
   ```

### Running the application
Run the app.py file using the Streamlit CLI:
   ```bash
   streamlit run app.py
   ```
