# Facebook-to-Telegram-Bot
Telegram bot which scrapes posts from Facebook Pages and sends to a Telegram channel.
This project has been forked from [VariabileAleatoria/Telegram-Facebook-Pages-Bot](https://github.com/VariabileAleatoria/Telegram-Facebook-Pages-Bot)

## Setting Up Telegram Channel

For this project to work, it must have a Telegram channel, an active bot with admin rights, and an API Token for the bot. 

## Usage

Insert telegram bot token and the channel tag in the **config.py** file.  

Insert the FB pages you want to get posts from in the **pages.csv** file.  
The first line is needed so don't change it.  
The first column is the **page name**, you can set it to whatever you want but it will be the signature of the posts in every comment.  
The second name is the **page tag**, this must me the name of the page you can find in the URL with the broswer, this is what the bot actually needs to get posts from the pages.  
The last column is the **last post used**, that is the timestamp of the last post retrieved by the bot, and will be changed by it at runtime. **Be careful** to set it properly the first time, because the bot will try to retrieve all the posts which were published after that time. The timestamp format is '%Y-%m-%d %H:%M:%S'(example: 2019-09-07 19:38:29)  
I wrote that the bot will _try_ because right now the [module used](https://github.com/kevinzg/facebook-scraper) only gets the last two or three posts, keep that in mind if your pages posts more than 3 times in two minutes, or just change the check interval accordingly.  

## What's working
Right now the library used only retrieves text posts and photos, so no videos, shares or others

## Python Modules needed

To install modules in Python:
`$ pip install python-telegram-bot --upgrade`
`$ pip install facebook-scraper --upgrade

[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
[facebook-scraper](https://github.com/kevinzg/facebook-scraper)
