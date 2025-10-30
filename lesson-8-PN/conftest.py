import pytest
import requests
from config import Config


@pytest.fixture(scope="session", autouse=True)
def check_api_availability():
    try:
        response = requests.get(
            f"{Config.get_base_url()}/projects",
            headers={"Authorization": f"Bearer {Config.API_TOKEN}"},
            timeout=10
        )
        if response.status_code == 401:
            pytest.fail("Invalid API token. Please check Config.API_TOKEN")
    except requests.exceptions.ConnectionError:
        pytest.fail("API is not available. Please check connection")
    except requests.exceptions.Timeout:
        pytest.fail("API request timeout. Please check your connection")
