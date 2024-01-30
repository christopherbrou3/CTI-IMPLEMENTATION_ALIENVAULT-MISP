from OTXv2 import OTXv2, IndicatorTypes

# Initialize the OTXv2 client with your OTX API key
otx = OTXv2("25f83e9363653da5f91024a73189d8b8b3bac6ba874615e8ec6b4e09750d5f0c")

# Retrieve all pulses you are subscribed to
pulses = otx.getall()

# Iterate through the pulses and print out indicators
for pulse in pulses:
    print("Pulse Name: {}".format(pulse['name']))
    for indicator in pulse['indicators']:
        print("Indicator: {} Type: {}".format(indicator['indicator'], indicator['type']))

