#!/usr/bin/env python3

import csv
import os
from datetime import datetime
from os import path

date_format = '%Y-%m-%d %H:%M:%S'
fields = ['page_name', 'page_tag', 'last_post_used']
now = datetime.now().strftime(date_format)

def setup():
    print("This is the setup process for the bot, please be ready with the info required:")
    print("- Telegram Bot Token can be found in your chat with @BotFather")
    print("- The tag of the channel where the bot is admin")
    print("- The ids of the facebook pages you are interested (can be found in the url https://www.facebook.com/" + '\033[1m' + "<page_id>"+'\033[0m'+")")
    print("\nDo you want to proceed? [Y/n]")
    proceed = input()
    if proceed=='n':
        exit()
    with open('config.py', 'w') as f:
        print("Enter the Token:")
        TOKEN = input()
        print("Enter the chat/channel tag:")
        chat_id = input()
        if chat_id[0] == '@':
            chat_id = chat_id[1:]
        f.writelines(["TOKEN = '"+TOKEN+"'"+'\n', "chat_id = '@"+ chat_id +"'"])
    with open('pages.csv','w') as f:
        csv_writer = csv.DictWriter(f, fields)
        csv_writer.writeheader()
        c = 'y'
        while c != 'n':
            row = {}
            print("Give me a facebook page id:")
            row['page_tag'] = input()
            print("What name you want to associate to this page?:")
            row['page_name'] = input()
            row['last_post_used'] = now
            csv_writer.writerow(row)
            print("Do you want to add another page? [y/n]:")
            while True:
                c = input()
                if c != 'y' and c != 'n':
                    print("Invalid input, please enter 'y' or 'n'")
                else:
                    break
    print('The bot is now configured, you can start it with ./scraper.py')

def add_pages():
    with open('pages.csv','a') as f:
        csv_writer = csv.DictWriter(f, fields)
        c = 'y'
        while c != 'n':
            row = {}
            print("Give me a facebook page id:")
            row['page_tag'] = input()
            print("What name you want to associate to this page?:")
            row['page_name'] = input()
            row['last_post_used'] = now
            csv_writer.writerow(row)
            print("Do you want to add another page? [y/n]:")
            while True:
                c = input()
                if c != 'y' and c != 'n':
                    print("Invalid input, please enter 'y' or 'n'")
                else:
                    break
    print('The bot is now configured, you can start it with ./scraper.py')

# Main
if path.isfile('pages.csv'):
    print("Do you want to add pages to the current configuration?") 
    print("If the answer is 'n' the script will procede with a clean setup")
    print("Add new pages?: [Y/n]")
    c = input()
    if c=='n':
        setup()
    else:
        add_pages()
else:
    setup()

