#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://wwisnorthsmithfield.maxgalaxy.net/LeagueScheduleTeamDetail.aspx?TeamRegistrationID=4647&WebReportID=7"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)
print soup.prettify()

file = open("sunday.txt", "w")
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

# grep notes
#grep -A 20 ucLeagueScheduleTeamDetail_reptEventScheduleList_Tr sunday.txt | grep -v "<" >> sundaySlim.txt
