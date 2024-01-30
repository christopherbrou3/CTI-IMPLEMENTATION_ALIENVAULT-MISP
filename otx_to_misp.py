# otx_to_misp.py

from OTXv2 import OTXv2
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# OTX configuration
otx_api_key = "25f83e9363653da5f91024a73189d8b8b3bac6ba874615e8ec6b4e09750d5f0c"
otx = OTXv2(otx_api_key)

# MISP configuration
misp_url = "https://192.168.44.179"
misp_api_key = "DFeEoY9stYktT7MaXfOrqpcLUc0sHcWH7UrubmU0"
misp_headers = {'Authorization': misp_api_key, 'Content-Type': 'application/json'}

# Retrieve OTX Indicators
pulses = otx.getall()

# Transform OTX Data and Send to MISP
for pulse in pulses:
    # Check if the indicators list is not empty
    if pulse.get("indicators"):
        # Transform OTX data into MISP format
        misp_data = {
            "value": pulse["indicators"][0]["indicator"],
            "type": "text",  # Use the appropriate MISP indicator type based on your data
            "category": "Network activity",
            "comment": pulse["name"],
            "to_ids": False,
        }

        # Send data to MISP
        misp_response = requests.post(f"{misp_url}/events", headers=misp_headers, data=json.dumps(misp_data), verify=False)

        if misp_response.status_code == 200:
            print(f"Indicator '{misp_data['value']}' added to MISP successfully.")
        else:
            print(f"Error adding indicator '{misp_data['value']}' to MISP. Status code: {misp_response.status_code}")

