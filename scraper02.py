#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup

mech = Browser()
url = "http://wwisnorthsmithfield.maxgalaxy.net/LeagueScheduleTeamDetail.aspx?TeamRegistrationID=4542&WebReportID=7&GUID=91ee4112-15bc-41a2-a8bd-24b2d3599eee"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)
#print soup.prettify()
table = soup.find("table", border=1)

for row in table.findAll('tr')[1:]:
    col = row.findAll('td')
    rank = wrTableTimeColumn[0].string
    artist = wrTableFacilityColumn1].string
    album = col[2].string
    cover_link = col[3].img['src']
    record = (rank, artist, album, cover_link)
    print "|".join(record)
