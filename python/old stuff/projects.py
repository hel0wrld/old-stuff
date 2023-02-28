import requests
from bs4 import BeautifulSoup
r= requests.get(url="http://www.iitkgp.ac.in/department/IM")
html_content=r.text
soup=BeautifulSoup(html_content, 'html.parser')
#print(soup.prettify())
'''aaa=soup.find('div', attrs={'class': 'aboutTheDepartmentFacultyListing'})
l=aaa.text.strip()+'\n'
l1=soup.find_all('div', attrs={'class': 'aboutTheDepartmentFacultyListing'})
l2=[]
for links in l1:
    l2.append(links.a['href'])
print(l2)
l=l.split('\n')[:-1]
print(len(l))
print(l)
print(l1)'''
headtag=soup.find('div', attrs={'class': 'aboutTheDepartmentFacultyListing'})
bruh=headtag.contents
print(bruh[0].contents)