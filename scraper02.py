#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://wwisnorthsmithfield.maxgalaxy.net/LeagueScheduleTeamDetail.aspx?TeamRegistrationID=4542&WebReportID=7&GUID=91ee4112-15bc-41a2-a8bd-24b2d3599eee"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)
print soup.prettify()

file = open("newfile.txt", "w")
file.write(soup.prettify())
file.close()

#table = soup.find("table", border=1)
#
#for row in table.findAll('Tr')[1:]:
#    col = row.findAll('td class')
#    rank = col[0].string
#    artist = col[1].string
#    album = col[2].string
#    record = (rank, artist, album)
#    print "|".join(record)
