import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the status code
    and the titles of all posts.

    The function sends a GET request to the JSONPlaceholder API
    to retrieve all posts.
    If the request is successful, it parses the fetched data
    into a JSON object and prints the titles of all the posts.

    Raises:
        requests.exceptions.RequestException:
        If there is an error with the HTTP request.
    """

    url = 'https://www.jsonplaceholder.org/posts'

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        posts = response.json()

        for post in posts:
            print(f"Title: {post['title']}")
    except requests.exceptions.RequestException as error:
        print(f"An error occured: {error}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder, structures the data,
    and writes it to a CSV file.

    The function sends a GET request to the JSONPlaceholder API
    to retrieve all posts.
    If the request is successful, it structures the data
    into a list of dictionaries, where each
    dictionary contains the 'id', 'title', and 'body' of a post.
    It then writes the data to a CSV
    file called 'posts.csv' with columns 'id', 'title', and 'body'.

    Raises:
        requests.exceptions.RequestException:
        If there is an error with the HTTP request.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()

        posts = response.json()

        structured_data = [{'id': post['id'], 'title':post['title'],
                            'body': post['body']} for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)

        print(f"Data has been successfully written to posts.csv")

    except requests.exceptions.RequestException as error:
        print(f"An error occured: {error}")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
