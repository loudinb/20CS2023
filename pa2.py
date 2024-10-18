import random
import logging
from typing import Dict, List, Tuple

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class StateCapitalsQuiz:
    def __init__(self):
        self.state_capitals: Dict[str, str] = {
            "Alabama": "Montgomery",
            "Alaska": "Juneau",
            "Arizona": "Phoenix",
            "Arkansas": "Little Rock",
            "California": "Sacramento",
            "Colorado": "Denver",
            "Connecticut": "Hartford",
            "Delaware": "Dover",
            "Florida": "Tallahassee",
            "Georgia": "Atlanta",
            # Add more states as needed...
        }
        self.buckets: Dict[int, List[str]] = {
            1: list(self.state_capitals.keys()),
            2: [], 3: [], 4: [], 5: []
        }
        self.round_number: int = 1

    def choose_state(self) -> Tuple[str, int]:
        logging.info(f"Round {self.round_number}:")
        
        for bucket, states in self.buckets.items():
            if states and (bucket == 1 or self.round_number % (2 ** (bucket - 1)) == 0):
                logging.info(f"Choosing a state from Bucket {bucket}.")
                return random.choice(states), bucket
        
        logging.info("No states available in active buckets. Fallback to random state.")
        return random.choice(list(self.state_capitals.keys())), 1

    def ask_question(self, state: str, bucket_num: int) -> bool:
        capital_guess = input(f"What is the capital of {state}? ").strip().lower()
        
        if capital_guess == "exit":
            print("Thank you for playing! Goodbye.")
            return False

        if capital_guess == self.state_capitals[state].lower():
            print(f"Correct! The capital of {state} is {self.state_capitals[state]}.")
            self._promote_state(state)
        else:
            print(f"Incorrect. The capital of {state} is {self.state_capitals[state]}.")
            self._demote_state(state)
        return True

    def _log_bucket_counts(self):
        counts = ", ".join(f"{i}={len(b)}" for i, b in self.buckets.items())
        logging.info(f"Bucket Counts: {counts}")

    def _promote_state(self, state: str):
        for bucket_num in range(1, 5):
            if state in self.buckets[bucket_num]:
                self.buckets[bucket_num].remove(state)
                self.buckets[bucket_num + 1].append(state)
                logging.info(f"State '{state}' promoted to Bucket {bucket_num + 1}")
                self._log_bucket_counts()
                break

    def _demote_state(self, state: str):
        for bucket_num in range(1, 6):
            if state in self.buckets[bucket_num]:
                self.buckets[bucket_num].remove(state)
                self.buckets[1].append(state)
                logging.info(f"State '{state}' demoted to Bucket 1")
                self._log_bucket_counts()
                break

    def start_quiz(self):
        print("Welcome to the State Capitals Quiz! Type 'exit' to quit.")
        while True:
            if all(not bucket for bucket in list(self.buckets.values())[:-1]):
                print("You've mastered all the state capitals! Well done!")
                break
            
            state, bucket_num = self.choose_state()
            if not self.ask_question(state, bucket_num):
                break
            self.round_number += 1

if __name__ == "__main__":
    quiz = StateCapitalsQuiz()
    quiz.start_quiz()