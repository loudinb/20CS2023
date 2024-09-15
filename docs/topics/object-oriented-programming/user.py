"""A module that defines the User class for managing user profiles and posts.

This module contains the User class, which allows for creating and managing 
user profiles with a username, bio, and a collection of posts. It includes 
methods for creating posts, retrieving posts, and getting the user's join date.
"""

from datetime import datetime


class User:
    """A class representing a user with a profile and posts."""

    def __init__(self, username, bio):
        """Initializes a new User instance.

        Args:
            username (str): The username of the user.
            bio (str): A short bio for the user.
        """
        self.username = username  # Initialize username
        self.bio = bio  # Initialize bio
        self.posts = []  # Initialize posts as an empty list
        self.join_date = datetime.now()  # Initialize join_date to current date

    def create_post(self, image_url, caption):
        """Creates a new post for the user.

        Args:
            image_url (str): The URL of the image for the post.
            caption (str): The caption for the post.

        Returns:
            str: A confirmation message for the post creation.
        """
        post = {
            'image_url': image_url,
            'caption': caption,
            'timestamp': datetime.now()  # Set to the current date and time
        }
        self.posts.append(post)
        return (f"{self.username} posted: {caption} at "
                f"{post['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")

    def get_posts(self):
        """Returns the list of posts created by the user.

        Returns:
            list: A list of dictionaries representing the user's posts.
        """
        return self.posts

    def get_join_date(self):
        """Returns the user's join date in a readable format.

        Returns:
            str: A string representing the user's join date.
        """
        return f"Joined on: {self.join_date.strftime('%Y-%m-%d')}"
