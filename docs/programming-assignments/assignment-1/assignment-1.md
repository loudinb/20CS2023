# Assignment 1

**Instagram-like Application Using Object-Oriented Programming (OOP)**

In this assignment, you will implement an Instagram-like application using **Object-Oriented Programming (OOP)** principles in Python. The application will simulate basic social media functionalities, including user creation, following, posting, and commenting. The focus will be on two core OOP principles: **encapsulation** and **composition**.

You can refer to the [reference material](reference-material.md) while working on the assignment for some specific syntax and examples related to implementing the classes and various functionalities.

The implementation details for each class are provided separately in the following sections:

- [User Class](user-class.md)
- [Post Class](post-class.md)
- [Comment Class](comment-class.md)

Follow the instructions in each section to implement the corresponding class.


## Testing Your Implementation

We have provided a sample application file `instamimic.py` that serves as the main module for the project. This file:

1. Imports all necessary classes
2. Contains the `InstaMimicApp` class, which acts as a central manager
3. Handles all interactions between User, Post, and Comment classes

The `InstaMimicApp` class includes methods to create users, posts, comments, and manage user relationships. This structure prevents circular imports between classes, a common issue in Python that can cause runtime errors. By centralizing these operations, we maintain a clear and manageable code structure.

This approach is considered a best practice in Python application design, especially for projects with interrelated classes.

- [instamimic.py](instamimic.py)

### Interactive Testing

The Jupyeter Notebook `app-demonstration.ipynb` provides a demonstration of how to use the `InstaMimicApp` class to create users, posts, comments, and follow users. You can refer to this notebook to understand how to test your implementation interactively.

- [instamimic-demo](instamimic-demo.ipynb)

### Automated Testing

The provided module-level unit tests are required. Your implementation **must pass all of the unit tests** to be considered correct.

- [tests_instamimic.py](tests_instamimic.py)
- [tests_user.py](tests_user.py)
- [tests_post.py](tests_post.py)
- [tests_comment.py](tests_comment.py)

You can run the unit tests using the following command:

```bash
python -m unittest tests_instamimic.py
python -m unittest tests_user.py
python -m unittest tests_post.py
python -m unittest tests_comment.py
```
You can also run all of the tests at once using the following command:

```bash
python -m unittest discover
```

## GitHub Repository

For your convenience, a GitHub repository has been created for this assignment.  This repository contains the starter code and the unit tests for the assignment. This is a template repository, so you can create a new repository from this template and start working on the assignment.

Access the repository using the following link:

[https://github.com/20CS2023-FS24/programming-assignment-1](https://github.com/20CS2023-FS24/programming-assignment-1)

This repository is only provided for the convenience of those familiar with GitHub, and may want to use it to manage their assignment code, and work in a Codespace.

```{note}
Please refer to GitHub's documentation on [creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for more information:
```
