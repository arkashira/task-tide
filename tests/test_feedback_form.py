import pytest
import sys
from unittest.mock import patch
from src.feedback_form import collect_feedback, store_feedback, Feedback, Rating

def test_collect_feedback():
    with patch('sys.argv', ['__main__.py', '--rating', '2', '--comment', 'Test comment']):
        feedback = collect_feedback()
        assert feedback.rating in [Rating.LOW, Rating.MEDIUM, Rating.HIGH]
        assert isinstance(feedback.comment, str)

def test_store_feedback(tmp_path):
    feedback = Feedback(Rating.MEDIUM, 'This is a comment')
    store_feedback(feedback)
    assert (tmp_path / 'feedback.json').exists() == False
    with open('feedback.json', 'r') as f:
        data = eval(f.read())
        assert data['rating'] == feedback.rating.value
        assert data['comment'] == feedback.comment
