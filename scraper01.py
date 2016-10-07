from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://wwisnorthsmithfield.maxgalaxy.net/LeagueScheduleTeamDetail.aspx?TeamRegistrationID=4542&WebReportID=7&GUID=91ee4112-15bc-41a2-a8bd-24b2d3599eee"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("dl", "boccat")
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links
