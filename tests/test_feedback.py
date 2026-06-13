import json
from feedback import FeedbackMechanism

def test_collect_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    assert len(mechanism.feedback_data) == 1
    assert mechanism.feedback_data[0]["rating"] == 5
    assert mechanism.feedback_data[0]["comment"] == "Great job!"

def test_store_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    mechanism.store_feedback("feedback.json")
    with open("feedback.json", 'r') as file:
        data = file.read()
    assert json.loads(data) == [{"rating": 5, "comment": "Great job!"}]

def test_load_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    mechanism.store_feedback("feedback.json")
    loaded_data = mechanism.load_feedback("feedback.json")
    assert loaded_data == [{"rating": 5, "comment": "Great job!"}]
