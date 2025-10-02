# Deployment Guide

## Local Deployment
1. Clone repository
2. Install Python 3.8+
3. Run: `pip install -r requirements.txt`
4. Set BOT_TOKEN in config.py
5. Run: `python main.py`

## Server Deployment
### Using Heroku
1. Fork this repository
2. Create Heroku account
3. Connect GitHub repository
4. Set BOT_TOKEN in Config Vars
5. Deploy

### Using VPS
1. SSH into your VPS
2. Clone repository
3. Install dependencies
4. Setup process manager (pm2)
5. Start bot

## Environment Variables
- BOT_TOKEN=your_bot_token_here