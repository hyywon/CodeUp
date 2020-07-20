import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

#indeed page extract
def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div",{"class":"pagination"})
  links = pagination.find_all('a')
  pages = []
  for link in links[:-1]:
      pages.append(int(link.string))
  #마지막 페이지 추출
  max_page = pages[-1]
  return max_page


def extract_indeed_jobs(last_page):
  jobs = []
  # for page in range(last_page) :
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})#resource 는 list
  for result in results:
      title = result.find("h2",{"class":"title"}).find("a")["title"]
      company = result.find("span",{"class":"company"})
      company_anchor = company.find("a")

      if company_anchor is not None:
        # anchor tag가 있는 경우
        #print(company_anchor.string)
          company = str(company_anchor.string)
      else :
        # anchor tag가 없는 경우
        #print(company.string)
          company =str(company.string)

      company = company.strip()
      print(company)
  return jobs
