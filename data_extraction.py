import requests
import config

def extract_linkedin_profile():
    """Fetches LinkedIn profile data from a premade JSON endpoint."""
    print("Fetching mock LinkedIn profile data...")
    try:
        response = requests.get(config.MOCK_DATA_URL, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data.")
            return {}
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}