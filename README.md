# StreamlitChatbot
![image](https://github.com/wytan12/StreamlitChatbot/assets/102575826/db904e3b-c90a-4667-aeae-b35cd39bb7ce)

## Why Streamlit?
- Ease of Use: Highlight how Streamlit's straightforward syntax and powerful built-in functions allow developers to build interactive UIs quickly without the need for complex web development skills.
- Real-Time Update: Streamlit ensures the chatbot interface updates instantly as users interact, providing a seamless, dynamic conversation experience.
- Interactive Widgets: Streamlit includes easy-to-integrate widgets such as text inputs and buttons, enhancing user engagement and interactivity in chatbots.

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
## References
- [Streamlit Documentation](https://docs.streamlit.io/develop/api-reference)
- [Streamlit Emoji Shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)

