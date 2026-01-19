from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from cco_service.main import app

# 1. Mock the Redis client 
# We do this so the test passes even if no real Redis server is running.
app.state.redis = MagicMock()
app.state.redis.ping.return_value = True

client = TestClient(app)

def test_health_check_endpoint():
    """
    Sanity check:
    - Hits the root endpoint
    - Verifies 200 OK status
    - Checks if the core library name is correctly returned (proving the link)
    """
    response = client.get("/")
    
    # Assert HTTP success
    assert response.status_code == 200
    
    data = response.json()
    
    # Assert logic
    assert data["service_status"] == "online"
    
    # CRITICAL CHECK: This proves cco-service can "see" cco-core
    # If this fails, the local path dependency in pyproject.toml is broken
    assert data["core_library_linked"] == "cco_core"
    
    # Since we mocked Redis, this should be "connected" or handled gracefully
    # This prevents the test from failing just because Redis isn't installed on the laptop
    assert "redis_status" in data
