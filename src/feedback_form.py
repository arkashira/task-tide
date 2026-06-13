from dataclasses import dataclass
from enum import Enum
from json import dumps
import argparse
import sys

class Rating(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class Feedback:
    rating: Rating
    comment: str

def collect_feedback():
    parser = argparse.ArgumentParser(description='Provide feedback on task prioritization')
    parser.add_argument('--rating', type=int, choices=[1, 2, 3], help='Rating (1-3)')
    parser.add_argument('--comment', type=str, help='Comment')
    try:
        args = parser.parse_args()
        return Feedback(Rating(args.rating), args.comment)
    except SystemExit as e:
        print("Error: Invalid arguments")
        sys.exit(1)

def store_feedback(feedback: Feedback):
    with open('feedback.json', 'w') as f:
        f.write(dumps({'rating': feedback.rating.value, 'comment': feedback.comment}))

if __name__ == "__main__":
    feedback = collect_feedback()
    store_feedback(feedback)
