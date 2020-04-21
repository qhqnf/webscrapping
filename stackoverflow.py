# %%
import requests
from bs4 import BeautifulSoup

# %%
URL = f"https://stackoverflow.com/jobs?q=python&pg="


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("a", {"class": "s-link"})["title"]

    company = html.find(
        "h3", {"class": "fc-black-700 fs-body1 mb4"}).find_all("span")[0].get_text(strip=True)
    company = company.strip("-").strip("\r")

    location = html.find(
        "h3", {"class": "fc-black-700 fs-body1 mb4"}).find_all("span")[1].get_text(strip=True)

    jobid = html["data-jobid"]
    return {'title': title, 'company': company, 'location': location,
            "apply_link": f"https://stackoverflow.com/jobs/{jobid}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping stackoverflow: Page {page}")
        result = requests.get(f"{URL}+{page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


# last_page = get_last_page()
# print(last_page)

# %%

def get_jobs():
    last_page = get_last_page()

    jobs = extract_jobs(10)

    return jobs