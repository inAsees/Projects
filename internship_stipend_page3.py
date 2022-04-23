from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

intershala_url = "https://internshala.com/internships/keywords-python/page-3"
uClient = uReq(intershala_url)
intershala_Page = uClient.read()
uClient.close()
intershala_html = bs(intershala_Page, "html.parser")
print(intershala_html)
# company = intershala_html.findAll("div", {
#     "class": "container-fluid individual_internship"})
#
# stipend = company[0].find_all_next("span", {"class": "stipend"})
#
# result_page3 = []
# for idx in range(len(stipend)):
#     result_page3.append(stipend[idx].text)
# print(result_page3)
# length_result_page3 = len(result_page3)
#
# final_list = []
# for ele in result_page3:
#     salary = "".join(ele.lstrip().split(" /month"))
#     salary = int(salary)
#     final_list.append(salary)
#
# total_stipend_page3 = sum(final_list)
# print("final list:", final_list)
# print("length of the final list", len(final_list))
# print("total stipend is equal to:", total_stipend_page3)
# print("Average stipend is equal to:", total_stipend_page3 / length_result_page3)
