import requests
import json
from colorama import Fore, Back, Style
from .getData import getGeo

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

# defining the function for fetching info
def fetch_iprepu(ip):

  querystring = {
      'ipAddress': ip,
      'maxAgeInDays': '90'
  }
  
  headers = {
      'Accept': 'application/json',
      'Key': 'e978ab6babe64dc5874d49d53f5efe9da81c447c8a54a912fbaa37711d12dd203363a6a2925fe746'
  }
  
  response = requests.request(method='GET', url=url, headers=headers, params=querystring)
  
  
  decodedResponse = json.loads(response.text)
  # print (json.dumps(decodedResponse, sort_keys=True, indent=2))
  # print(decodedResponse['data']['domain'])

  print ( "=================== Summery For the IP: " + Fore.GREEN + json.dumps(decodedResponse ["data"]["ipAddress"]) + Fore.WHITE + "===================")
  print()
  print ( Fore.WHITE + "Domain: " + json.dumps(decodedResponse ["data"]["domain"]))
  print ( "Hostname: " + json.dumps(decodedResponse ["data"]["hostnames"]))
  print ( "Usage Type: " + json.dumps(decodedResponse ["data"]["usageType"]))
  print ( Fore.YELLOW + "Confidence of Abuse: " + json.dumps(decodedResponse ["data"]["abuseConfidenceScore"]))
  print ( Fore.WHITE + "Number Times of Reported: " + json.dumps(decodedResponse ["data"]["totalReports"]))
  print ( "Last Reported: " + json.dumps(decodedResponse ["data"]["lastReportedAt"]))
  print ( "Whitelisted: " + json.dumps(decodedResponse ["data"]["isWhitelisted"]) + "\n")
  print()

  getGeo(ip)
  print("---------------------------------------------------------------------------")
  print()

  with open('./outtojson.json', 'a') as f:
    json.dump(decodedResponse, f, indent=2)



#take input from a file
def file_call(file):

  # Get the file handler
  fhand = open(file)
  ip_array = []

  # Loop through each line via file handler
  for line in fhand:
    ip_array.append(line.rstrip())         # to avoid printing /n in end of the line

  print(ip_array[1])


  # caller function
  for data in ip_array:
    fetch_iprepu(data)



#calling fr single ip check
def single_call(singleip):
  fetch_iprepu(singleip)
