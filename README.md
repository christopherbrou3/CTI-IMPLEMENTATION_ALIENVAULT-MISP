# CTI-IMPLEMENTATION_ALIENVAULT-MISP
Developed scripts or tools to automatically retrieve and update  data from the feeds and from ALIENVAULT to MISP.

# OTX_IOC_RETRIEVER.PY
otx_ioc_retriever.py is a created Python script that interacts with the AlienVault Open Threat Exchange (OTX) API to retrieve indicators of compromise (IOCs) from pulses on which we have subscribed. 
               
               To update otx_ioc_retriever.py you need to update this part to your own Alienvalut using your own OTX API KEY : 
               replace  OTXv2("25f83e9363653da5f91024a73189d8b8b3bac6ba874615e8ec6b4e09750d5f0c") with your actual OTX API key.

# OTX_TO_MISP.PY
otx_to_misp.py is a Python script that retrieves indicators from AlienVault Open Threat Exchange (OTX) pulses and sends them to a MISP (Malware Information Sharing Platform & Threat Sharing) instance.
To adapt this script for another system or use case, you may need to make the following changes:

    API Keys and URLs: Replace the existing OTX API key, MISP URL, and MISP API key with your credentials.

    MISP Indicator Type: Adjust the MISP indicator type ("type": "text") based on the type of data you are handling.

    Category and Comment: Modify the MISP category and comment fields according to your requirements.

    Error Handling: Enhance error handling mechanisms as needed.

    Security Considerations: Be cautious about disabling SSL verification (verify=False) in the requests to MISP. It's generally recommended to use a secure connection, especially in production environments.



RITA is an open source framework for network traffic analysis.
RITA provides an install script that works on Ubuntu, Debian, Security Onion, and CentOS


Choose one of the following install methods:

 
     sudo ./install.sh (will install RITA as well as supported versions of Zeek and MongoDB. This is suitable if you want to get started as quickly as possible or you don't already have Zeek or MongoDB.)

    sudo ./install.sh --disable-zeek --disable-mongo ( will install RITA only, without Zeek or MongoDB. You may also use these flags individually.)


    SPLUNK SETUP 
    
Certainly! Here are the steps to install Splunk on Ubuntu 22.04 using the provided .deb package:
1.	Navigate to the Downloads  where ou have install your slpunk .deb from splunk.com website after that ( Open a terminal and navigate to the directory where the Splunk .deb package is located. In your case, it's the /home/brou/Downloads directory.)
bash
•  cd /home/brou/Downloads
•  Install Splunk: Use the dpkg command to install the Splunk .deb package. Replace splunk-9.1.2-b6b9c8185839-linux-2.6-amd64.deb with the actual name of your Splunk package.
 Bash(splunk-9.1.2-b6b9c8185839-linux-2.6-amd64.deb= may change depending of  the splunk setup numbers ) 

              sudo dpkg -i splunk-9.1.2-b6b9c8185839-linux-2.6-amd64.deb
  	
If there are any missing dependencies, the dpkg command will notify you. You can use apt to install these dependencies:
bash
                     
              sudo apt-get install -f
                      
•  Start Splunk: Navigate to the Splunk installation directory and start Splunk:
bash

            cd /opt/splunk
           sudo ./bin/splunk start
           
•  Access Splunk Web: Open a web browser and go to http://localhost:8000. Log in with the admin credentials you set during the installation.
•  Explore and Search: Once logged in, you can start exploring and searching your data using the Splunk Search & Reporting interface.
•  Stop Splunk: If needed, you can stop Splunk using the following command:
bash

          cd /opt/splunk
         sudo ./bin/splunk stop


Install curl if some error appear before the installation  from up use the command below to fix it :
bash

           sudo apt-get update
          sudo apt-get install curl

