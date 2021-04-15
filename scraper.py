#!/usr/bin/env python3

import telegram, threading
from facebook_scraper import get_posts
from datetime import datetime
import csv
from tempfile import NamedTemporaryFile
import shutil
import config

TOKEN = config.TOKEN
bot = telegram.Bot(TOKEN)

chat_id = config.chat_id

date_format = '%Y-%m-%d %H:%M:%S'

fields = ['page_name', 'page_tag', 'last_post_used']

WAIT_SECONDS = 120

def check():
    with open('pages.csv', mode='r+') as csv_file, NamedTemporaryFile(mode='w', delete=False) as tempfile:
        csv_reader = csv.DictReader(csv_file)
        csv_writer = csv.DictWriter(tempfile, fields)
        line_count = 0
        csv_writer.writeheader()
        for page in csv_reader:
            posts = list(get_posts(page['page_tag'], pages=2))
            posts.sort(key = lambda x: x['time'])
            for post in posts:
                if post['time'] <= datetime.strptime(page['last_post_used'], date_format): # post already sent to channel
                    continue
                if post['images'] is not None:
                    images = [telegram.InputMediaPhoto(post['images'][0], caption=(post['text'] if post['text'] else '') + '\n[' + page['page_name'] + ']')]
                    for image in post['images'][1:]:
                        images.append(telegram.InputMediaPhoto(image))
                    bot.send_media_group(chat_id, images)
                elif post['video'] is not None:
                    bot.send_video(chat_id, post['video'], caption=(post['text'] if post['text'] else '') + '\n[' + page['page_name'] + ']')
                elif post['text'] is not None:
                    bot.send_message(chat_id, (post['text'] if post['text'] else '')+ '\n[' + page['page_name'] + ']')
            page['last_post_used'] = posts[-1]['time']
            row = {'page_name': page['page_name'], 'page_tag': page['page_tag'], 'last_post_used': page['last_post_used']}
            csv_writer.writerow(row)
        shutil.move(tempfile.name, 'pages.csv')
        threading.Timer(WAIT_SECONDS, check).start()

check()
