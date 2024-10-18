import random

from question_box import QuestionBox
from time_delayed_question_box import TimeDelayedQuestionBox

class AdaptiveSpacedRepetitionSystem:
    def __init__(self, quiz_items, num_repetition_stages=5, reattempt_delay=90):
        self.reattempt_bucket = TimeDelayedQuestionBox(delay=reattempt_delay)
        self.repetition_buckets = [QuestionBox(i) for i in range(num_repetition_stages)]
        
        for item in quiz_items:
            self.repetition_buckets[0].add(item)

    def __repr__(self):
        return (f"AdaptiveSpacedRepetitionSystem("
                f"num_repetition_stages={len(self.repetition_buckets)}, "
                f"reattempt_delay={self.reattempt_bucket.reattempt_delay}, "
                f"total_items={sum(len(bucket.items) for bucket in self.repetition_buckets) + len(self.reattempt_bucket.items)})")

    def choose_next_item(self):
        eligible_items = self.reattempt_bucket.get_eligible()
        if eligible_items:
            return random.choice(eligible_items), 'reattempt'
        
        for bucket in self.repetition_buckets:
            if bucket.items:
                return random.choice(bucket.items), f'bucket_{bucket.index}'
        
        return None, None

    def process_answer(self, item, source, is_correct):
        if is_correct:
            if source == 'reattempt':
                self.reattempt_bucket.remove(item)
            self.promote_item(item)
        else:
            if source != 'reattempt':
                self.reattempt_bucket.add(item)
            self.demote_item(item)

    def promote_item(self, item):
        for i, bucket in enumerate(self.repetition_buckets[:-1]):
            if item in bucket.items:
                bucket.remove(item)
                self.repetition_buckets[i + 1].add(item)
                break

    def demote_item(self, item):
        for bucket in self.repetition_buckets[1:]:
            if item in bucket.items:
                bucket.remove(item)
                self.repetition_buckets[0].add(item)
                break

    def is_complete(self):
        return all(len(bucket.items) == 0 for bucket in self.repetition_buckets[:-1]) and \
               len(self.reattempt_bucket.items) == 0

    def run_quiz(self, get_answer):
        while not self.is_complete():
            item, source = self.choose_next_item()
            if item is None:
                break

            answer = get_answer(item)
            if answer.lower() == 'exit':
                break

            is_correct = item.check_answer(answer)
            self.process_answer(item, source, is_correct)