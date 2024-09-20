# Exercise 4

## Class Methods and Attributes

In this exercise, you will enhance the existing classes with class attributes and methods, and create a new `Analytics` class to practice these concepts further.

```{warning}
If there is any ambiguity in the requirements, make a reasonable assumption and proceed. Then look at the provided unit tests to understand the expected behavior, and adjust your implementation accordingly.
```

## Step 1: Enhance the `User` Class

Update the `user.py` file:

1. Add a class attribute `total_users` to keep track of the number of users.
2. Implement a class method `get_user_count` that returns the total number of users.
3. Create a static method `is_valid_username` that checks if a username meets certain criteria (e.g., length, allowed characters).
4. Add a class method `create_anonymous_user` that creates a user with a generated username.
5. Use the `is_valid_username` method in the `__init__` method to validate usernames.

## Step 2: Enhance the `Post` Class

Update the `post.py` file:

1. Add a class attribute `post_id_counter` to generate unique IDs for posts.
2. Implement a class method `get_post_count` that returns the total number of posts created.
3. Create a static method `is_valid_content` that checks if the post content is appropriate (e.g., not empty, within character limit).
4. Use the `is_valid_content` method in the `__init__` method to validate post content.
5. Add a class method `create_shared_post` that creates a new post as a share of an existing post.

## Step 3: Enhance the `Comment` Class

Update the `comment.py` file:

1. Add a class attribute to track the total number of comments across all posts.
2. Implement a class method to get the average number of comments per post.
3. Create a static method to format comment content (e.g., remove extra whitespace, capitalize first letter).
4. Use the formatting method in the `__init__` method when setting the comment content.

## Step 4: Create an `Analytics` Class

Create a new file `analytics.py`:

1. Implement an `Analytics` class with the following features:

   a. Class attributes:
      - `total_likes`: int, initialized to 0
      - `total_shares`: int, initialized to 0
      - `active_users`: set(), initialized as an empty set

   b. Class methods:
      - `update_likes(cls, count: int) -> None`: Increases `total_likes` by `count`
      - `update_shares(cls, count: int) -> None`: Increases `total_shares` by `count`
      - `add_active_user(cls, user_id: str) -> None`: Adds `user_id` to `active_users` set
      - `remove_active_user(cls, user_id: str) -> None`: Removes `user_id` from `active_users` set

   c. Static methods:
      - `calculate_engagement_rate(total_interactions: int, total_users: int) -> float`: 
        Returns the engagement rate as a percentage (interactions / users * 100)
      - `identify_trending_posts(posts: List[Post], threshold: int) -> List[Post]`: 
        Returns a list of Post objects with likes above the given threshold

   d. Class method:
      - `generate_report(cls) -> str`: Returns a formatted string containing:
        - Total likes
        - Total shares
        - Number of active users
        - Current engagement rate (using `calculate_engagement_rate`)

## Step 5: Implement Tagging System

Create a new file `tag.py`:

1. Implement a `Tag` class with the following features:

   a. Class attribute:
      - `all_tags`: Dict[str, 'Tag'], initialized as an empty dictionary

   b. Instance attributes (in `__init__`):
      - `name`: str
      - `usage_count`: int, initialized to 0

   c. Class method:
      - `get_or_create(cls, tag_name: str) -> 'Tag'`: 
        If a tag with `tag_name` exists in `all_tags`, return it. Otherwise, create a new Tag, add it to `all_tags`, and return it.

   d. Instance method:
      - `increment_usage(self) -> None`: Increases `usage_count` by 1

   e. Static methods:
      - `get_trending_tags(top_n: int = 5) -> List['Tag']`: 
        Returns the `top_n` tags with the highest `usage_count`

2. Update the `Post` class in `post.py`:
   
   a. Add an instance attribute:
      - `tags`: List[Tag], initialized as an empty list in `__init__`

   b. Add a method:
      - `add_tag(self, tag_name: str) -> None`: 
        Uses `Tag.get_or_create(tag_name)` to get a Tag object, adds it to the `tags` list, and calls `increment_usage()` on the tag.

   c. Modify the `__init__` method to automatically detect and add tags from the post content:
      - Look for words starting with '#' in the post content
      - For each hashtag found, call `self.add_tag(tag_name)`

## Testing

### Interactive Testing

To test your enhanced code interactively using a Python shell:

1. Open a terminal and navigate to your project directory.
2. Start the Python interactive shell by typing `python` or `python3`.
3. Import your classes:
   ```python
   from user import User
   from post import Post
   from comment import Comment
   from analytics import Analytics
   from tag import Tag
   ```
4. Create instances and test the new class methods and attributes:
   ```python
   # Test User class
   user1 = User("johndoe", "john@example.com")
   user2 = User("janedoe", "jane@example.com")
   print(User.get_user_count())
   anon_user = User.create_anonymous_user()
   
   # Test Post class
   post1 = user1.create_post("Hello #world!")
   post2 = user2.create_post("Learning #python is fun!")
   print(Post.get_post_count())
   shared_post = Post.create_shared_post(user2, post1)
   
   # Test Comment class
   comment1 = Comment(user2, post1, "Great post!")
   print(Comment.get_average_comments_per_post())
   
   # Test Analytics class
   analytics = Analytics()
   print(analytics.generate_summary_report())
   
   # Test Tag class
   world_tag = Tag.get_or_create_tag("world")
   python_tag = Tag.get_or_create_tag("python")
   print(Tag.get_trending_tags())
   ```
5. Verify that the output matches your expectations and that the class methods and attributes are working correctly.

### Running Unit Tests

Download the provided unit tests for the classes:

- [test_user.py](test_user.py)
- [test_post.py](test_post.py)
- [test_comment.py](test_comment.py)
- [test_analytics.py](test_analytics.py)
- [test_tag.py](test_tag.py)

To run the provided unit tests:

1. Ensure you have test files for each class: `test_user.py`, `test_post.py`, `test_comment.py`, `test_analytics.py`, and `test_tag.py`.

2. Open a terminal and navigate to your project directory.

3. Run the tests for each class:
   ```
   python -m unittest test_user.py
   python -m unittest test_post.py
   python -m unittest test_comment.py
   python -m unittest test_analytics.py
   python -m unittest test_tag.py
   ```

4. To run all tests at once, use:
   ```
   python -m unittest discover
   ```

5. Review the test output. All tests should pass if your implementation is correct.

6. If any tests fail, review the error messages, go back to your implementation, and make the necessary corrections.