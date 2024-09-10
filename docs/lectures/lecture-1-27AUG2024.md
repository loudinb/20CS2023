# Lecture 1, Aug 27, 2024

Welcome to Python Programming (CS2023). This document outlines our plan for the first day and provides important information to get you started.

## Course Syllabus Review

### Schedule

Our course will meet on Tuesdays and Thursdays from 3:30 PM to 4:50 PM. While the full [schedule](../syllabus/24fs/24fs.ipynb) is published on the course website, here's a broad overview of our 15-week semester:

- Weeks 1-4: Python basics and writing quality code
- Weeks 5-6: The Python ecosystem, writing and distributing code
- Week 7: Midterm
- Weeks 8-12: Data structures and scientific computing
- Weeks 13-15: Applications in Machine Learning and Deep Learning


```{note}
The schedule is subject to change based on our progress.
```

### Insructor Support and Availability

Your success is our top priority. If you need assistance, please don't hesitate to reach out. For quick access to contact information and office hours, please refer to the [instructor information](../syllabus/instructor-information.md) section in the course syllabus.

- **Email:** I check my emails frequently, including evenings and weekends. You can expect a response within 24 hours in most cases.
- **Cell Phone:** For urgent matters, or if you haven't received an email response within 24 hours, feel free to use my cell phone number. 

```{admonition} Prioritization
- **Engaged Students:** Students who consistently attend classes, participate actively, complete assignments on time, and seek help proactively will receive priority in terms of support and assistance.

- **Less Engaged Students:** Those who frequently miss classes, consistently submit work late, or do not participate actively may find that their requests for help are given lower priority, especially when more engaged students need assistance.
```


### Assessment Plan and Grading

Your performance will be evaluated through:

- Weekly knowledge checks (30%)
- Programming assignments (35%)
- Midterm and Final Exam (35%)

Take 5 and review the [assessment plan and policies](../syllabus/assessment-plan-and-policies.md) along with the [grading policy](../syllabus/grading-policy.md).


## Class Enrollment Composition

Let's briefly look at the composition of enrolled students and discuss potential misalignments between the actual composition of enrolled students and the intended target audience for the course.

> Maybe some Python code would be appropriate here?  **Indeed it would!**  

Let's look at some Python code in an interactive [notebook](../topics/day1/class-profile.ipynb) to see what the composition of the class looks like, and potentially give you a first look at some common Python analysis libraries and techniques.


## Textbook

Our primary textbook will be available through O'Reilly Media.  Everyone should go through the steps now to confirm they can access the book through UC's institutional access.

1. Review the [O'Reilly Access FAQ](../faqs/oreilly_access.md) and follow the instructions to create an account with your UC email address.
2. Verify you can access [Scientific Computing with Python](https://learning.oreilly.com/library/view/scientific-computing-with/9781838822323/).

Physical books are also available for puchase online (e.g., Amazon, Barnes and Noble, etc.)

## GitHub and GitHub Classroom

Throughout this semester, we will be utilizing [GitHub Classroom](https://classroom.github.com/) for assignment distribution. GitHub Classroom will streamline our workflow, including the automatic evaluation of submitted code.

If you do not already have a GitHub account, please [create one](https://github.com/join) now. I highly recommend using a GitHub username based on your real name, as it is common for employers to review your work on GitHub.  Also, please edit your profile to include your full name.

Next, please confirm that you can access this [test assignment](https://classroom.github.com/a/vg4czhxa) on GitHub Classroom. The first time you use GitHub Classroom, you will need to authorize access to your GitHub account.

```{note}
I encourage you to sign up for [GitHub Education](https://github.com/education/students), which upgrades your GitHub Free plan to the [GitHub Pro plan](https://docs.github.com/en/get-started/learning-about-github/githubs-plans).
```  

## Python Distribution and Development IDE

Before we begin coding, it's important to set up your Python development environment. This involves two main components: a Python distribution and an Integrated Development Environment (IDE).

### Python Distribution

A Python distribution is a package that includes the Python interpreter (which runs your code) and often comes with a set of pre-installed libraries. 

```{warning}
The most common issue users encounter is managing multiple Python installations and libraries, or having an improperly configured system that prevents their Python interpreter from locating the correct libraries referenced in their code.  If you have Python installed from the Windows Store you should uninstall it before proceeding.
```

For this course, you should install Python 3.11 or newer from one of the following distributions:

1. **Standard Python Distribution**: This is the official Python distribution from python.org. It provides a clean, up-to-date version of Python without any additional packages.
   - Download: https://www.python.org/downloads/
   - Recommended for: Users who want a minimal installation and prefer to manage their own packages.
   - Note: During installation, remember to check the box that says "Add Python to PATH" to ensure you can run Python from any location on your computer.

2. **Miniconda**: This is a minimal installer for conda. It's a smaller alternative to Anaconda that includes only conda, Python, and a small number of other useful packages.
   - Download: https://docs.conda.io/en/latest/miniconda.html
   - Recommended for: Users who want the conda package manager but prefer a minimal initial installation.


Finally, open a command prompt and launch the interactive Python shell (IPython) by typing `python`.


### Development IDE

An Integrated Development Environment (IDE) is a software application that provides comprehensive facilities for software development. It typically includes a code editor, debugger, and other helpful tools that make coding easier and more efficient.

While you're free to use any environment you're comfortable with, we recommend one of the following for beginners:

1. **PyCharm**: A full-featured IDE with a gentler learning curve for students. PyCharm offers features like code completion, error highlighting, and an integrated debugger, which can be particularly helpful for learning Python.
   - Download: https://www.jetbrains.com/edu-products/download/#section=pycharm-edu
  
2. **Visual Studio Code with Python extension**: A lightweight, customizable editor popular among developers. VS Code is highly flexible and can be used for many programming languages. The Python extension adds Python-specific features like IntelliSense (code completion), linting, debugging, and code formatting.
   - Download VS Code: https://code.visualstudio.com/
   - Install the Python extension from within VS Code
   
Both of these IDEs offer powerful features that can help you write, test, and debug your Python code more effectively. Choose the one that feels most comfortable for you, as the best IDE is the one you enjoy using.

Remember, regardless of which IDE you choose, make sure you have installed a Python distribution first. The IDE will use this Python installation to run your code. When setting up your chosen IDE, you'll need to point it to your installed Python distribution.

```{note}
Jet Brains provides [free education licenses](https://www.jetbrains.com/community/education/#students) to all of their development tools.  
```

## Generative AI

In our rapidly evolving field of computer science, it's crucial to address the role of Generative AI in your academic journey. As your instructor, I want to emphasize the importance of engaging with these cutting-edge technologies while maintaining the highest standards of academic integrity.

Generative AI presents a unique opportunity for you to expand your understanding of complex concepts in our field. I encourage you to explore these tools as part of your self-directed learning. They can serve as valuable resources for:

- Deepening your comprehension of challenging topics
- Stimulating creative problem-solving approaches
- Providing an interactive platform to test and refine your ideas

Given the trajectory of our industry, familiarity with these technologies is becoming increasingly vital for future computer science professionals. By engaging with Generative AI in your study process, you'll gain insights into its capabilities, limitations, and potential impacts on our field.

View Generative AI as a supplementary tool in your learning toolkit. Explore its capabilities, understand its functioning, and use it to enhance your comprehension. However, when it comes to demonstrating your knowledge and skills in assessed work, rely on your own abilities. This approach will not only ensure academic honesty but also contribute significantly to your growth as a computer scientist.

```{admonition} Academic Integrity
Generative AI is strictly prohibited for use in any graded components of this course. This includes, but is not limited to:

- Assignments
- Projects
- Examinations
- Any other assessed work

All submissions must be solely your own work, reflecting your personal understanding and skills. Using Generative AI for graded work violates our academic integrity policy and impedes your genuine learning process.
```

Should we give Generative AI a try?

Let's look at a [demonstration](../topics/day1/claude-3.5-sonnet-demonstration.ipynb) that uses Calude AI.  Compare the output to the code found in [class profile](../topics/day1/class-profile.ipynb).  Interestingly, you may observe that the "Pre-Junior" academic level is missing from the GenAI code. **Why is that?**