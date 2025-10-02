import os

class Config:
    # Bot Token (Get from @BotFather)
    BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
    
    # Developer Info
    DEVELOPER = "@PRIME_X_ARMY"
    GITHUB_URL = "https://github.com/your-username/cloudways-bot"
    
    # Channel Links
    CHANNEL_LINK = "https://t.me/+2si64yQHduUyNmY1"
    SUPPORT_GROUP = "https://t.me/your_support_group"
    
    # Bot Settings
    DEFAULT_CREDITS = 10
    REFERRAL_CREDITS = 5
    VERSION = "2.0 GitHub Edition"
    
    # Database
    DATABASE_NAME = "bot_data.db"