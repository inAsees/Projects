from urllib.request import urlopen as u_req
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
import pandas as pd
import os


class ScrapInternshala:
    def __init__(self):
        self._df = self._load_from_file()
        self._base_url = "https://internshala.com"
        self._page1_url = self._base_url + "/internships/keywords-python/page-1"
        self._page2_url = self._base_url + "/internships/keywords-python/page-2"
        self._page3_url = self._base_url + "/internships/keywords-python/page-3"
        self._scrap_pages()

    def _scrap_pages(self) -> None:
        internshala_url = self._page3_url
        u_client = u_req(internshala_url)
        internshala_page = u_client.read()
        u_client.close()
        internshala_html = bs(internshala_page, "html.parser")
        companies_box = internshala_html.findAll("a", {"class": "view_detail_button"})
        for idx in range(len(companies_box)):
            details_url = self._base_url + companies_box[idx]["href"]
            u_client = u_req(details_url)
            page = u_client.read()
            u_client.close()
            page_html = bs(page, "html.parser")
            company = page_html.find("a", {"class": "link_display_like_text"}).text.strip()
            job = page_html.find("span", {"class": "profile_on_detail_page"}).text.strip()
            stipend = self._get_stipend(page_html.find("span", {"class": "stipend"}).text)
            duration = self._get_duration(page_html.findAll("div", {"class": "item_body"}))
            location = page_html.find("a", {"class": "location_link"}).text.strip()
            skill_set = None
            try:
                skill_set = page_html.find("div", {"class": "round_tabs_container"}).get_text().strip().split()
            except AttributeError as e:
                print(e)
                pass
            self._write_to_csv(company, job, stipend, duration, location, skill_set)

    def _write_to_csv(self, company: str, job: str, stipend: float, duration: str, location: str,
                      skill_set: list) -> None:
        row = {
            "company": company,
            "job": job,
            "stipend": stipend,
            "duration": duration,
            "location": location,
            "skill_set": skill_set
        }
        self._df = self._df.append(row, ignore_index=True)
        self._df.to_csv(r"C:\Users\DELL\Desktop\test_files\scrap_internshala.csv", index=False)

    @staticmethod
    def _get_stipend(raw_text: str) -> float:
        salary = "".join(raw_text.lstrip().split(" /month"))
        if len(salary) < 6:
            return int(salary)
        elif len(salary) > 5:
            if "-" in salary:
                salary = list(map(int, salary.split("-")))
                avg = (salary[0] + salary[1]) / 2
                return avg
            elif " lump sum +  Incentives" in salary:
                salary = "".join(salary.split(" lump sum +  Incentives"))
                return float(salary)
            elif " +  Incentives" in salary:
                salary = "".join(salary.split(" +  Incentives"))
                return float(salary)
            elif " lump sum" in salary:
                salary = "".join(salary.split(" lump sum"))
                return float(salary)

    @staticmethod
    def _get_duration(raw_text: ResultSet) -> str:
        for duration in raw_text:
            if "Months" in duration.text or "Month" in duration.text:
                return duration.text.strip()

    @staticmethod
    def _load_from_file() -> pd.DataFrame:
        path = input("path:")
        if os.path.exists(path):
            return pd.read_csv(path)
        return pd.DataFrame(columns=["company", "job", "stipend", "duration", "location", "skill_set"])


if __name__ == "__main__":
    scrap = ScrapInternshala()
