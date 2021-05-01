# Telegram-Facebook-Pages-Bot
Telegram bot which sends posts from a list of Facebook Pages to a Telegram channel.  

Every post has this structure:  
[Media] (if present)  
[Text] (if present)  
[Signature] (with a name associated to the page by the user)  

## Usage
### Automatic setup
Just run `setup.py`

### Manual setup
Insert telegram bot token and the channel tag in the **config.py** file.  
Insert the FB pages you want to get posts from in a **pages.csv** file.  
The first line is needed and must be `page_name,page_tag,last_post_used`.  
The first column is the **page name**, you can set it to whatever you want but it will be the signature of the posts in every comment.  
The second name is the **page tag**, this must me the name of the page you can find in the URL with the broswer, this is what the bot actually needs to get posts from the pages.  
The last column is the **last post used**, that is the id of the last post retrieved by the bot, and will be changed by it at runtime.  
**Be careful** to set it properly the first time, because the bot will try to retrieve all the posts which were published after that one.    
Follow [these instructions](https://github.com/kevinzg/facebook-scraper/issues/28#issuecomment-793066983) to extract cookies and save them as `cookies.txt` in the same folder of `scraper.py` (set your language to english before exporting cookies to avoid gettin low quality images)


## What's working
- text posts
- image post *
- image galleries *
- video *

\* if present text will be used as caption

Shares work partially.

## Module needed
[python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
[facebook-scraper](https://github.com/kevinzg/facebook-scraper)

## Example of pages.csv

```
page_name,page_tag,last_post_used
Facebook Page,facebook,284507553110844
```

## Warnings and known issues
- Since facebook-scraper is not able to return reliable timestamp for posts, this bot is currently relying on the assumption that posts ids always grow, if suddenly new posts will start having ids with values smaller then previous ones then the bot will stop forwarding posts to the channel.  
This check should be probably done in a smarter way, any contribution is much appreciated.  
- Scraper can return low quality images when using cookies (apparently if language on facebook is set to english this doesn't happen).  
- Error handling is missing
