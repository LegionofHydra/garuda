import sys
if sys.version_info<(3,0):
   sys.stderr.write("\nYou need python 3.0 or later to run this script\n")
   sys.stderr.write("Please update and make sure you use the command python3 geo-recon.py <IP NUMBER> <COMMAND>\n\n")
   sys.exit(0)

import requests
import json
from colorama import Fore, Back, Style
import os
from modules.commands import command
from modules.commands import listCommand
from modules.helps import help
from modules.welcome import welcome
from modules.getData import getGeo
from modules.reputation_fetch import file_call
from modules.reputation_fetch import single_call
from modules.nmapVerify import verify
from modules.myip import myIp
from modules.Daily_summery import daily


syA = sys.argv

def zero(syA):
   #Verify for argumements and IPs, if not it will read the banner and will close
   if (len(sys.argv) == 1):
      welcome()
      sys.exit(0)
      verify()

zero(syA)




#Test for use and execute

if (len(sys.argv) > 1):
   syA1 = sys.argv[1]
   if sys.argv[1].startswith('-'):
         if syA1 == "--help" or syA1 == '-h':
            os.system('clear')
            welcome()
            help(syA1)

         elif syA1 == '-b' or syA1 == '--banner':
            os.system('clear')            
            welcome()
         elif syA1 == '-c' or syA1 == '--commands':
            os.system('clear')            
            welcome()
            listCommand()
         elif syA1 == '-d':
            os.system('clear')            
            welcome()
            daily()



   elif syA1 == 'localhost':
      ip = myIp()
      os.system('clear')
      welcome()
      syA1 = ip
      getGeo(syA1)
      single_call(syA1)


   else:
      os.system('clear')
      welcome()
      print(Fore.WHITE + '\n Wait a minute....')
      single_call(syA1)
      getGeo(syA1)

   

if (len(sys.argv) > 2):

   syA1 = sys.argv[1]
   syA2 = sys.argv[2]

   if syA1 == '-f' or syA1 == '--file': 
      os.system('clear')            
      welcome()
      file_call(syA2)
   else:
      command(syA2, syA1)











         
