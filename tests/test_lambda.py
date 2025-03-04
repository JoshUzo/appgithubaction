import pytest
import json
from src.lambda_function import lambda_handler

def test_lambda_handler():
    event = {}  # Mock event
    context = {}  # Mock context
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert "message" in json.loads(response["body"])
