from bs4 import BeautifulSoup
import lxml
import requests
# import os



url =  "https://trip.llnl.gov/results/results2018-1.html"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
  
# Parses the HTML content
soup = BeautifulSoup(html_content, 'lxml')
pageTitle = soup.h2
pageSubTitle = soup.h4  
tables = soup.find_all('table', attrs={"border": "4"})

# Attributes to remove
REMOVE_ATTRIBUTES = [
  'cellpadding', 'cellspacing', 'width', 'align', 'class', 'style'
]

# Recursively remove listed attributes
for attribute in REMOVE_ATTRIBUTES:
  for tag in soup.find_all(attrs={attribute: True}):
    del tag[attribute]

for tag in soup.find_all(attrs={'valign': 'top'}):
  tag.decompose()

print(pageTitle)
print(pageSubTitle)
print("<h3>I-125 Results</h3>")
print("<!-------Table 1------->")
print(tables[0])
print("<!------Table 2-------->")
print(tables[1])
print("<!-------Table 3-------->")
print(tables[2])
print("<h3>I-131 Results</h3>")
print("<!-------Table 4-------->")
print(tables[3])
print("<!-------Table 5-------->")
print(tables[4])
print("<!-------Table 6-------->")
print(tables[5])
