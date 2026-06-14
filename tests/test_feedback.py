from feedback import FeedbackMechanism

def test_collect_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    mechanism.store_feedback("feedback.json") # Store the feedback before loading
    assert len(mechanism.load_feedback("feedback.json")) == 1

def test_store_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    mechanism.store_feedback("feedback.json")
    assert mechanism.load_feedback("feedback.json") == [{"rating": 5, "comment": "Great job!"}]

def test_load_feedback():
    mechanism = FeedbackMechanism()
    mechanism.collect_feedback(5, "Great job!")
    mechanism.store_feedback("feedback.json")
    assert mechanism.load_feedback("feedback.json") == [{"rating": 5, "comment": "Great job!"}]
