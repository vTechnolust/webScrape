import requests
from bs4 import BeautifulSoup
import encodings, os

url = "http://wwisnorthsmithfield.maxgalaxy.net/LeagueScheduleTeamDetail.aspx?TeamRegistrationID=4542&WebReportID=7&GUID=91ee4112-15bc-41a2-a8bd-24b2d3599eee"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

#for link in soup.findAll("tr"):
#    print link.get("id")

g_data = soup.find_all("td",{"class": "tableColumn"})

myList = []

for item in g_data:
    myList.append(item.text.replace('\n','').replace(' ','').replace('\r',''))
#
#while 'Thu' in myList:
#    myList.remove('Thu')
#
#while 'AdultLeague' in myList:
#    myList.remove('AdultLeague')
#
#while '' in myList:
#    myList.remove('')
#
listLength = len(myList)

#for x in range(0, 8):
for index in range(len(myList)):
    print 'Current Record :', myList[index]

#print ' \n'.join(myList)
