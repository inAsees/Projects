import csv
from dataclasses import dataclass
from typing import List
import requests as req
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet


@dataclass
class CompanyInfo:
    company: str
    job_title: str
    stipend: str
    duration: str
    location: str
    skill_set: List[str]


class ScrapInternshala:
    def __init__(self):
        self._base_url = "https://internshala.com"
        _python_intern_page = "internships/keywords-python"
        self._python_internship_page_url = ["{}/{}/page-{}".format(self._base_url, _python_intern_page, i) for i in
                                            range(1, 4)]
        self._company_info_list = []  # type: List[CompanyInfo]

    def scrap_all_pages(self) -> None:
        page_no = 1
        for url in self._python_internship_page_url:
            print("Page {} scrapping begins....".format(page_no))
            self._scrap_url(url)
            print("\n")
            print("Page {} scrapping finished....".format(page_no))
            page_no += 1

    def dump(self, file_path: str):
        with open(file_path, "w", newline="") as f:
            writer = csv.DictWriter(f,
                                    fieldnames=["company", "job_title", "stipend", "duration", "location", "skill_set"])
            writer.writeheader()
            print("Dumping begins....")
            for ele in self._company_info_list:
                writer.writerow({"company": ele.company, "job_title": ele.job_title, "stipend": ele.stipend,
                                 "duration": ele.duration, "location": ele.location, "skill_set": ele.skill_set})
            print("Dumping finished....")

    def _scrap_url(self, url: str) -> None:
        page_src = req.get(url).text
        page_soup = bs(page_src, "html.parser")
        companies_box = page_soup.findAll("a", {"class": "view_detail_button"})

        for company in companies_box:
            details_url = self._base_url + company["href"]
            company_details_src = req.get(details_url).text
            company_details_soup = bs(company_details_src, "html.parser")
            company_info = self._parse_company_info(company_details_soup)
            self._company_info_list.append(company_info)
            print(">", end="")

    @classmethod
    def _parse_company_info(cls, company_soup: bs) -> CompanyInfo:
        company = company_soup.find("a", {"class": "link_display_like_text"}).text.strip()
        job = company_soup.find("span", {"class": "profile_on_detail_page"}).text.strip()
        stipend = cls._get_stipend(company_soup.find("span", {"class": "stipend"}).text)
        duration = cls._get_duration(company_soup.findAll("div", {"class": "item_body"}))
        location = company_soup.find("a", {"class": "location_link"}).text.strip()
        skill_set = None
        try:
            skill_set = company_soup.find("div", {"class": "round_tabs_container"}).get_text().strip().split()
        except AttributeError as e:
            print(e)
            pass

        return CompanyInfo(company, job, stipend, duration, location, skill_set)

    @staticmethod
    def _get_stipend(raw_text: str) -> str:
        salary = "".join(raw_text.lstrip().split(" /month"))
        if len(salary) < 6:
            return salary
        elif len(salary) > 5:
            if "-" in salary:
                salary = list(map(int, salary.split("-")))
                avg = (salary[0] + salary[1]) / 2
                return str(avg)
            elif " lump sum +  Incentives" in salary:
                salary = "".join(salary.split(" lump sum +  Incentives"))
                return salary + " plus incentives"
            elif " +  Incentives" in salary:
                salary = "".join(salary.split(" +  Incentives"))
                return salary + " plus incentives"
            elif " lump sum" in salary:
                salary = "".join(salary.split(" lump sum"))
                return salary

    @staticmethod
    def _get_duration(raw_text: ResultSet) -> str:
        for duration in raw_text:
            if "Months" in duration.text or "Month" in duration.text:
                return duration.text.strip()


if __name__ == "__main__":
    scrapper = ScrapInternshala()
    scrapper.scrap_all_pages()
    scrapper.dump(r"C:\Users\DELL\Desktop\test_files\internshala_scrapped.csv")
