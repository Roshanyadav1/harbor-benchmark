import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "no report.json found"
    assert report_path.stat().st_size > 0, "report.json is empty"


def test_report_schema():
    """The report file contains the expected JSON fields and types."""
    report_path = Path("/app/report.json")
    data = json.loads(report_path.read_text())

    assert isinstance(data, dict), "report.json must contain a JSON object"
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert isinstance(data["top_path"], str), "top_path must be a string"
    assert data["total_requests"] >= 0, "total_requests must be non-negative"
    assert data["unique_ips"] >= 0, "unique_ips must be non-negative"
