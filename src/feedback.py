import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Feedback:
    rating: int
    comment: str

class FeedbackMechanism:
    def __init__(self):
        self.feedback_data = []

    def collect_feedback(self, rating: int, comment: str) -> None:
        feedback = Feedback(rating, comment)
        self.feedback_data.append(feedback.__dict__)

    def store_feedback(self, filename: str) -> None:
        with open(filename, 'w') as file:
            json.dump(self.feedback_data, file)

    def load_feedback(self, filename: str) -> Dict:
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
