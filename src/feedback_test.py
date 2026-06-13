import json
import pytest
from feedback import collect_feedback, store_feedback, Feedback

def test_collect_feedback():
    feedback = collect_feedback()
    assert isinstance(feedback, Feedback)
    assert feedback.rating is not None
    assert feedback.comment is not None

def test_store_feedback(tmp_path):
    # Use the temporary directory for isolation.
    feedback = collect_feedback()
    store_feedback(feedback, path=tmp_path / "feedback.json")
    target_file = tmp_path / "feedback.json"
    assert target_file.exists()
    with target_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]["rating"] == feedback.rating
        assert data[0]["comment"] == feedback.comment
