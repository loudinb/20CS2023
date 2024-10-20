from datetime import timedelta
from time import sleep

from ars.box import Box
from ars.qtype.shortanswer import ShortAnswer

# Create a box
review_box = Box("Review Box", timedelta(seconds=30))

# Create some questions
q1 = ShortAnswer("What's the capital of France?", "Paris")

# Add questions to the box
review_box.add_question(q1)

print(review_box)  # Output: Box(name='Review Box', questions_count=2)

# Ask the question, which updates the last_asked property to the current time
print(q1.ask())  # Output: "What's the capital of France?"

# Get the next priority question
# Since the question was just asked, it won't be returned
next_question = review_box.get_next_priority_question()
if next_question:
    print(next_question.ask())
else:
    print("No priority question available")

sleep(31)  # Wait for the priority interval to pass

# Get the next priority question
# Since the question was asked more than 30 seconds ago, it will be returned
next_question = review_box.get_next_priority_question()
if next_question:
    print(next_question.ask())