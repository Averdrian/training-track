from fastapi.testclient import TestClient


from main import app


client = TestClient(app)


class TestHealth:
    
    def test_health_returns_200_ok(self):
        response = client.get("/health")
        assert response.status_code == 200
    