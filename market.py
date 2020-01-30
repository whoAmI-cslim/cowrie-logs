import urllib.request
import json
import sys
import os
import datetime
from types import SimpleNamespace
from dateutil.parser import parse
import colorama
from colorama import Fore, Style


##########################################Install dependancies#######################################

dataDir = "/root/"

pipcheck = os.system("pip -V > pipcheck.txt")
reqcheck = os.system("pip list | grep -F requests > reqcheck.txt")
datecheck = os.system("pip list | grep -F dateutil > dateutil.txt")

dateversion = "python-dateutil   2.8.1"
reqversion = "requests          2.21.0"
pipversion = "pip 20.0.2 from /usr/local/lib/python3.7/dist-packages/pip (python 3.7)"

with open("pipcheck.txt") as pipCheck:
  if pipversion in pipCheck.read():
   os.system("rm pipcheck.txt")
  else:
   print ("Installing dependancy: pip for Python3")
   os.system("apt-get install python3-pip")
   os.system("pip install --upgrade pip")
   os.system("rm pipcheck.txt")

with open("reqcheck.txt") as reqCheck:
  if reqversion in reqCheck.read():
   os.system("rm reqcheck.txt")
  else:
   print ("Installing dependancy: requests")
   os.system("pip install requests")
   os.system("rm reqcheck.txt")

with open("dateutil.txt") as dateCheck:
 if dateversion in dateCheck.read():
  os.system("rm dateutil.txt")
 else:
  print ("Installing dependancy: python-dateutils")
  os.system("pip install python-dateutils")
  os.system("rm dateutil.txt")

import dateutil
from dateutil import parser
import requests

##########################################Request Data for API call###################################

print ("\n\n\t\tWelcome to the Hunter Stock Market Analysis Tool\n\n\n")

timeSeries = "TIME_SERIES_DAILY_ADJUSTED"

global symbols

symbols = []

n = int(input("How many market symbols would like to watch? (1-20): "))
for i in range(0, n):
   num = i + 1
   symnum = print("\n(",num,") Enter the market symbol would you like to watch?: ", end=" ")
   symbol = input()
   symbols.append(symbol)

###########################################Function to make sure correct symbols selected#############

def get_symbols():
 print ("\n")
 for i in range(0, n):
    num = i + 1
    symnum = print("\n(",num,") Enter the market symbol would you like to watch?: ", end=" ")
    symbol = input()
    symbols.append(symbol)

###########################################Continue getting information################################

print("\nYou chose the following symbols: ", symbols)

strsymbols = ''.join(str(e) for e in symbols)

global correctsym
correctsym = input("\nWere these the correct symbol(s)? (Y/N): ")

while "N" in  correctsym:
 get_symbols()
 correctsym = input("\nWere these the correct symbol(s)? (Y/N): ")

datatype = "json"

apikey = "Tsk_fefa9db383814556a1cb191326de65f9"

global outputsize

global typeans

typeans = " "

choice = '0'

print ("\n")

while choice == '0':
 print ("What data would you like to pull: Choose as many options as you'd like:")
 print ("1. Quotes")
 print ("2. News")
 print ("3. Chart")

 print ("\nType your numbers here with a comma in between: ", end= " ")
 choice = input()

 if choice == "1":
  print ("\nYou've only selected Quotes. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "quote"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "2":
  print ("\nYou've only selected News. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "news"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "3":
  print ("\nYou've only selected Charts. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "chart"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "1, 2" or "1,2":
  print ("\nYou've selected Quotes and News. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "quote,news"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "2, 3" or "2,3":
  print ("\nYou've selected News and Charts. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "news,chart"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "1, 3" or "1,3":
  print ("\nYou've selected Quotes and Charts. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "quote,chart"
  if "N" or "n" in yousure:
   choice == '0'

 elif choice == "1, 2, 3" or "1,2,3" or "1, 2,3" or "1,2, 3":
  print ("\nYou've selected all options: Quotes, Charts, and News. Is that correct? (Y/N): ", end= " ")
  yousure = input()
  typeans = "quote,news,chart"
  if "N" or "n" in yousure:
   choice == '0'

 else:
  print ("\nVery funny. You didn't select any of the available options.\n")
  choice == '0'


if "chart" in typeans:
 choice2 == '0'
 global chartans
 chartans = " "
 while choice2 == '0':
   print ("\nHow far back would you like to get chart data? Your options are: (Choose one)")
   print ("1. Max (15 years)")
   print ("2. Five Years")
   print ("3. Two Years")
   print ("4. One Year")
   print ("5. Year to Date")
   print ("6. Six Months")
   print ("7. Three Months")
   print ("8. One Month")
   print ("9. Five Days")
   print ("10. Today")

   print ("\nType your numerical selection here: ", end= " ")
   choice2 = input()

   if choice2 == 1:
    yousure = input("\nYou selected Max. Is that correct? (Y/N) : ")
    chartans = "max"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 2:
    yousure = input("\nYou selected Five Years. Is that correct? (Y/N) : ")
    chartans = "5y"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 3:
    yousure = input("\nYou selected Two Years. Is that correct? (Y/N) : ")
    chartans = "2y"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 4:
    yousure = input("\nYou selected One Year. Is that correct? (Y/N) : ")
    chartans = "1y"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 5:
    yousure = input("\nYou selected Year-to-Date. Is that correct? (Y/N) : ")
    chartans = "ytd"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 6:
    yousure = input("\nYou selected Six Months. Is that correct? (Y/N) : ")
    chartans = "6m"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 7:
    yousure = input("\nYou selected Three Months. Is that correct? (Y/N)?: ")
    chartans = "3m"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 8:
    yousure = input("\nYou selected One Month. Is that correct? (Y/N): ")
    chartans = "1m"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 9:
    yousure = input("\nYou selected Five Days. Is that correct? (Y/N): ")
    chartans = "5d"
    if yousure == "N":
     choice2 == '0'

   elif choice2 == 10:
    yousure = input("\n You selected Today. Is that correct? (Y/N) : ")
    chartans = "today"
    if yousure == "N":
     choice2 == '0'


######################################################################################################################

def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print (text)


##########################################################API Call to get .json#######################################

if len(symbols) < 2 and "quote" in typeans and "chart" in typeans and "news" in tyepans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/batch?types=" + typeans + "&range=" + chartans + "&last=10&token=" + apikey

if len(symbols) < 2 and "quote" in typeans and "chart" in typeans and "news" not in typeans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/batch?types=" + typeans + "&range=" + chartans + "&token=" + apikey

if len(symbols) < 2 and "quote" in typeans and "news" in typeans and "chart" not in typeans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/batch?types=" + typeans +  "&last=10&token=" + apikey

if (len(symbols) < 2) and ("quote" in typeans) and ("chart" not in typeans) and ("news" not in typeans):
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/book" "?token=" + apikey

if len(symbols) < 2 and "news" in typeans and "chart" in typeans and "quote" not in typeans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/batch?types=" + typeans + "&range=" + chartans + "&last=10&token=" + apikey

if len(symbols) < 2 and "news" in typeans and "chart" not in typeans and "quote" not in typeans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/" + typeans + "&last=10&token=" + apikey

if len(symbols) < 2 and "chart" in typeans and "quote" not in typeans and "news" not in typeans:
 url = "https://sandbox.iexapis.com/stable/stock/" + symbol + "/" + typeans + "&range=" + chartans + "&token=" + apikey

#################################################################json parsing and print results#########################################################

#print (url)


response = requests.request("GET", url).json()

#respjson = json.dumps(response, sort_keys=True, indent=4)
respjson = json.loads(json.dumps(response))

#print (respjson)

companyName = (respjson["quote"]["companyName"])
print ("\n\t\t\tResults from your search\n\n\n")
print ("\t\tYou searched for: " + companyName + " | Symbol: " + symbol)
print ("\n\n\t\t\tHere's what I found for you\n\n")

print ("\tTicker Symbol\t\tInformation")

weekhi = (respjson["quote"]["week52High"])
print ("\n\t" + symbol + "\t| \t52 Week High: $", weekhi)

weeklow = (respjson["quote"]["week52Low"])
print ("\n\t" + symbol + "\t| \t52 Week Low: $", weeklow)

realPrice = (respjson["quote"]["iexRealtimePrice"])
print ("\n\t" + symbol + "\t| \tReal Time Price: $", realPrice)

percentchange = (respjson["quote"]["change"])
print ("\n\t" + symbol + "\t| \tPercentage of Change: %", percentchange, "\n")


print ("\n\n\n\t\tRecent " + companyName + " News \n\n")
for item in respjson["news"]:
 source = item["source"]
 print ("\tFrom: " + source)
 newsdate = item["datetime"]
 newdate = newsdate / 1000.0
 newerdate = datetime.datetime.fromtimestamp(newdate).strftime('%Y-%m-%d')
 headline = item["headline"]
 print ("\tDate : " + newerdate)
 print ("\tHeadline: " + headline + "\n")
 summary = item["summary"]
 print ("\tSummary: " + summary + "\n")
 newsurl = item["url"]
 print ("\tYou can find more information at: " + url)

 print ("\n\n\n\n")

#############################################################Test stuff below here#############################################

#text = json.dumps(obj, sort_keys=True, indent=4)

#if len(symbols) < 2:
# url = "https://sandbox.iexapis.com/stable/stock/market/batch?symbols=" + symbols + "&" + typeans

#response = requests.request("GET", url).json()

#print (url)

#jprint(response)

#neatjson_resp = json.dumps(json_response, indent=2)

#global var

#var = {}

#x = 0

#while x < len(symbols):
# var["symbol{}".format(x)] = symbols[x]
# x = x + 1


