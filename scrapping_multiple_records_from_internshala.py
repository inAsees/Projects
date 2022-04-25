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
    lump_sum_per_month: int
    incentive: str
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
        with open(file_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f,
                                    fieldnames=["company", "job_title", "lump_sum_per_month", "incentive", "duration",
                                                "location", "skill_set"])
            writer.writeheader()
            print("Dumping begins....")
            for ele in self._company_info_list:
                writer.writerow(
                    {"company": ele.company, "job_title": ele.job_title, "lump_sum_per_month": ele.lump_sum_per_month,
                     "incentive": ele.incentive, "duration": ele.duration, "location": ele.location,
                     "skill_set": ele.skill_set})
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
        incentive_if_any = company_soup.findAll("i")
        stipend = cls._get_stipend(company_soup.find("span", {"class": "stipend"}).text, incentive_if_any)
        duration = cls._get_duration(company_soup.findAll("div", {"class": "item_body"}))
        location = company_soup.find("a", {"class": "location_link"}).text.strip()
        skill_set = "Not mentioned"
        try:
            skill_set = company_soup.find("div", {"class": "round_tabs_container"}).get_text().strip().split()
        except AttributeError as e:
            pass

        return CompanyInfo(company, job, stipend[0], stipend[1], duration, location, skill_set)

    @staticmethod
    def _get_stipend(raw_text: str, incentive_if_any: ResultSet) -> tuple[int, str]:
        incentive = "0"
        for i in incentive_if_any:
            try:
                text = i.get("popover_content")
                if "starting" in text:
                    continue
                idx = text.index("(")
                incentive = text[idx:]
            except:
                pass

        salary = "".join(raw_text.lstrip().split(" /month"))
        if len(salary) < 6:
            return int(salary), "0"
        elif len(salary) > 5:
            if "-" in raw_text and " lump sum" in raw_text:
                raw_salary = raw_text.split(" lump sum")
                raw_salary = raw_salary[0].split("-")
                avg = (int(raw_salary[0]) + int(raw_salary[1])) // 2
                return int(avg), "0"
            elif "-" in salary:
                salary = list(map(int, salary.split("-")))
                avg = (salary[0] + salary[1]) // 2
                return int(avg), "0"

            elif " lump sum +  Incentives" in salary:
                salary = "".join(salary.split(" lump sum +  Incentives"))
                return int(salary), incentive
            elif " +  Incentives" in salary:
                salary = "".join(salary.split(" +  Incentives"))
                return int(salary), incentive
            elif " lump sum" in salary:
                salary = "".join(salary.split(" lump sum"))
                return int(salary), "0"
            else:
                salary = 0
                incentive = "0"
                return salary, incentive

    @staticmethod
    def _get_duration(raw_text: ResultSet) -> str:
        for duration in raw_text:
            if "Months" in duration.text or "Month" in duration.text:
                return duration.text.strip()


if __name__ == "__main__":
    scrapper = ScrapInternshala()
    scrapper.scrap_all_pages()
    scrapper.dump(r"C:\Users\DELL\Desktop\test_files\test_scrap.csv")
