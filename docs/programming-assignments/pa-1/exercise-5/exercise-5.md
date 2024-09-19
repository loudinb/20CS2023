# Exercise 5

## Static Methods

In this exercise, you will enhance the existing classes with static methods and create a new `Utility` class to practice these concepts further.

```{warning}
If there is any ambiguity in the requirements, make a reasonable assumption and proceed. Then look at the provided unit tests to understand the expected behavior, and adjust your implementation accordingly.
```

## Step 1: Enhance the `User` Class

Update the `user.py` file:

1. Add a static method `is_valid_username` that checks if a username meets certain criteria (e.g., length, allowed characters).
2. Use the `is_valid_username` method in the `__init__` method to validate usernames.
3. Implement a static method `generate_random_username` that creates a random username.
4. Create a static method `format_user_info` that takes a username and email and returns a formatted string.

## Step 2: Enhance the `Post` Class

Update the `post.py` file:

1. Implement a static method `is_valid_content` that checks if the post content is appropriate (e.g., not empty, within character limit).
2. Use the `is_valid_content` method in the `__init__` method to validate post content.
3. Create a static method `extract_hashtags` that takes a post content and returns a list of hashtags.
4. Add a static method `format_post` that takes post content and returns a formatted string (e.g., truncating long content).

## Step 3: Enhance the `Comment` Class

Update the `comment.py` file:

1. Create a static method `format_content` to format comment content (e.g., remove extra whitespace, capitalize first letter).
2. Use the `format_content` method in the `__init__` method when setting the comment content.
3. Implement a static method `is_valid_content` to check if the comment content is appropriate.
4. Add a static method `generate_comment_preview` that takes a comment and returns a short preview.

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
   from utility import Utility
   ```
4. Test the new static methods:
   ```python
   # Test User class static methods
   print(User.is_valid_username("john_doe"))
   print(User.generate_random_username())
   print(User.format_user_info("john_doe", "john@example.com"))

   # Test Post class static methods
   print(Post.is_valid_content("Hello, world!"))
   print(Post.extract_hashtags("I love #python and #coding"))
   print(Post.format_post("This is a very long post content that should be truncated"))

   # Test Comment class static methods
   print(Comment.format_content("  this is a comment  "))
   print(Comment.is_valid_content("Valid comment"))
   print(Comment.generate_comment_preview("This is a long comment that should be previewed"))

   # Test Utility class methods
   print(Utility.is_valid_email("user@example.com"))
   print(Utility.generate_random_string(8))
   print(Utility.format_timestamp(datetime.now()))
   print(Utility.truncate_string("This is a long string", 10))
   ```
5. Verify that the output matches your expectations and that the static methods are working correctly.

### Running Unit Tests

Download the provided unit tests for the classes:

- [test_user.py](test_user.py)
- [test_post.py](test_post.py)
- [test_comment.py](test_comment.py)
- [test_utility.py](test_utility.py)

To run the provided unit tests:

1. Ensure you have test files for each class: `test_user.py`, `test_post.py`, `test_comment.py`, and `test_utility.py`.

2. Open a terminal and navigate to your project directory.

3. Run the tests for each class:
   ```
   python -m unittest test_user.py
   python -m unittest test_post.py
   python -m unittest test_comment.py
   python -m unittest test_utility.py
   ```

4. To run all tests at once, use:
   ```
   python -m unittest discover
   ```

5. Review the test output. All tests should pass if your implementation is correct.

6. If any tests fail, review the error messages, go back to your implementation, and make the necessary corrections.