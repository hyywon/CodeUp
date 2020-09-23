import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)  #마지막 숫자 가져오기
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class": "fs-body3"}).find("a")["title"]
    #unpacking
    company, location = html.find("h3", {
        "class": "fc-black-700 fs-body1 mb4"
    }).find_all(
        "span", recursive=False)
    #첫단계에 있는 span만 가져오기 위해서 사용
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("•")
    link_id = html.find("div", {
        "class": "grid--cell grid ai-center w12"
    }).find("button")["data-id"]

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f"https://stackoverflow.com/jobs/{link_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping So : page {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
