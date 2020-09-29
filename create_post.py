import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')

file_header = """
---
layout: post
title: {title}
date: {date}
preview_img:
description:
published: false
comments: false
---
"""


def validate_file_name(string):
    if len(string) < 5:
        print('Filename must be longer than 5 symbols')
        return False

    string = string.replace(' ', '-').lower()
    return string


while True:
    title = input('Please, enter filename: ')
    filename = validate_file_name(title)

    if filename:
        file_path = f'_posts/{today}-{filename}.md'
        with open(file_path, 'w') as f:
            f.write(file_header.format(
                title=title.capitalize(),
                date=today,
            ).strip())
            print(f'File created successfully: {file_path}')

        break
