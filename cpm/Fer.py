import json
import requests
from datetime import datetime

LICENSE_URL = "https://raw.githubusercontent.com/MAKERBKZZ/vip/main/licenses.json"

def load_licenses():
    try:
        response = requests.get(LICENSE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error loading licenses: {e}")
        return []

def verify_license(username, license_key):
    licenses = load_licenses()
    for license in licenses:
        if license["username"] == username and license["license_key"] == license_key:
            expiration_date = datetime.strptime(license["expiration_date"], "%Y-%m-%d %H:%M:%S")
            if datetime.now() < expiration_date:
                return True
            else:
                return False
    return False