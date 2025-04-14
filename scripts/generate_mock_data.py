
import json

# Example script to generate mock vulnerability data
mock_data = [
    {"id": "CVE-1234", "severity": "high", "description": "Example vulnerability 1"},
    {"id": "CVE-5678", "severity": "medium", "description": "Example vulnerability 2"}
]

# Save mock data to a file
with open("mock_vuln_data.json", "w") as f:
    json.dump(mock_data, f)
