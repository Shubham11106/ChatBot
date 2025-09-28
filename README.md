# NLP ChatBot Project using Deepseek  API


 


## Telebot on Telegrom Accoun Used Model Deepseek Chat

 


 

A powerful Telegram chatbot powered by DeepSeek AI, built with Python and aiogram. This bot provides intelligent responses using DeepSeek's advanced language model.

 
## Technologies Used

- **Python 3.7+**
- **aiogram** - Async Telegram Bot Framework
- **DeepSeek AI** - Language Model API
- **python-dotenv** - Environment management
- **OpenAI SDK** - For DeepSeek API compatibility

##  Prerequisites

- Python 3.7 or higher
- Telegram account
- DeepSeek API key
- Git

## Installation & Setup

 

### 2. Create Virtual Environment
```bash
# Using conda
conda create -n telebot python=3.7
conda activate telebot

 

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:
```env
# Telegram Bot Token from @BotFather
TOKEN=your_telegram_bot_token_here

# DeepSeek API Key from https://platform.deepseek.com/
Deepseek_API_KEY=your_deepseek_api_key_here
```

### 5. Get Your API Keys

#### Telegram Bot Token:
1. Message `@BotFather` on Telegram
2. Send `/newbot`
3. Follow instructions and copy the token

#### DeepSeek API Key:
1. Visit [DeepSeek Platform](https://platform.deepseek.com/)
2. Sign up/Login to your account
3. Navigate to API Keys section
4. Create a new API key

## Usage

### Running the Bot
```bash
python telebot.py
```

### Bot Commands
- `/start` - Initialize the bot and welcome message
- `/help` - Show available commands and usage
- `/clear` - Clear conversation history and context

### Example Conversation
```
User: /start
Bot: Hi! I'm Tele Bot! Powered by DeepSeek AI. How can I assist you?

User: What's the capital of France?
Bot: The capital of France is Paris...

User: /clear
Bot: I've cleared the past conversation and context.
```

##  Project Structure

```
telegram-deepseek-bot/
│
├── telebot.py                 # Main bot application
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (create this)
├── .gitignore                # Git ignore file
└── README.md                 # Project documentation
```

##  Configuration

### Environment Variables
- `TOKEN`: Your Telegram bot token
- `Deepseek_API_KEY`: Your DeepSeek API key

### Model Configuration
The bot uses `deepseek-chat` model by default. You can modify this in the code:
```python
MODEL_NAME = "deepseek-chat"   
```

##  Troubleshooting

### Common Issues

1. **Module Not Found Errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **API Key Errors**
   - Verify your DeepSeek API key is correct
   - Check if API key has sufficient credits

3. **Telegram Token Issues**
   - Ensure bot token is correct
   - Check if bot is started with BotFather

4. **OpenAI SDK Version Issues**
   ```bash
   # If using old syntax, downgrade:
   pip install openai==0.28
   
   
 

  comprehensive documentation  