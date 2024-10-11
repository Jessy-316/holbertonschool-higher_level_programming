#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():

    request = requests.get('https://jsonplaceholder.typicode.com/posts')

    print(f"Status Code: {request.status_code}")

    if request.ok:
        posts = request.json()
        for post in posts:
            print(f"{post['title']}")
    else:
        print(f"Failed to fetch posts. Status Code: {request.status_code}")


def fetch_and_save_posts():
    request = requests.get('https://jsonplaceholder.typicode.com/posts')
    if request.status_code == 200:
        posts = request.json()
        structured_data = [{'id': post['id'], 'title': post['title'],
                            'body': post['body']} for post in posts]

        with open('posts.cdv', mode='w', newline='',
                  encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)
        print("Data has been successfully written to posts.csv")
    else:
        print(f"Failed to fetch posts. Status Code: {request.status_code}")
