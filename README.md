# CTI-IMPLEMENTATION_ALIENVAULT-MISP
Developed scripts or tools to automatically retrieve and update  data from the feeds and from ALIENVAULT to MISP.

# OTX_IOC_RETRIEVER.PY
otx_ioc_retriever.py is a created Python script that interacts with the AlienVault Open Threat Exchange (OTX) API to retrieve indicators of compromise (IOCs) from pulses on which we have subscribed. 
to update otx_ioc_retriever.py you need to update this part to your own Alienvalut using your own  OTX API KEY replace  OTXv2("25f83e9363653da5f91024a73189d8b8b3bac6ba874615e8ec6b4e09750d5f0c") with your actual OTX API key.

# OTX_TO_MISP.PY
otx_to_misp.py is a Python script that retrieves indicators from AlienVault Open Threat Exchange (OTX) pulses and sends them to a MISP (Malware Information Sharing Platform & Threat Sharing) instance.
To adapt this script for another system or use case, you may need to make the following changes:

    API Keys and URLs: Replace the existing OTX API key, MISP URL, and MISP API key with your own credentials.

    MISP Indicator Type: Adjust the MISP indicator type ("type": "text") based on the type of data you are handling.

    Category and Comment: Modify the MISP category and comment fields according to your requirements.

    Error Handling: Enhance error handling mechanisms as needed.

    Security Considerations: Be cautious about disabling SSL verification (verify=False) in the requests to MISP. It's generally recommended to use a secure connection, especially in production environments.
