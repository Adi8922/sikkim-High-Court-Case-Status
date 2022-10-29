import requests
from bs4 import BeautifulSoup
import json

session = requests.session()
base_url = "https://hcs.gov.in/"
url = "https://hcs.gov.in/hcs/hcourt/hg_case_search"
url1 = "https://hcs.gov.in/hcs/hcourt/hg_case_search?ajax_form=1&_wrapper_format=drupal_ajax"
url2 = "https://hcs.gov.in/hcs/hgcases/SKHC010001112022?_wrapper_format=drupal_ajax"
response = session.get(url , verify = False)
content = response.content
soup = BeautifulSoup(content , "lxml")
# print(soup)

# case_no = str(input("Enter Your Case Number\n"))
# case_year = str(input("Enter Your Case Year\n"))

Headers1 = {
        "Accept" : "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept-Language" : "en-US,en;q=0.5",
        "Connection" : "keep-alive",
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Host" : "hcs.gov.in",
        "Origin" : "https://hcs.gov.in",
        "Referer ": "https://hcs.gov.in/hcs/hcourt/hg_case_search",
        "Sec-Fetch-Dest" : "empty",
        "Sec-Fetch-Mode" : "cors",
        "Sec-Fetch-Site" : "same-origin",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "X-Requested-With" : "XMLHttpRequest"
    }

payload1 = {
        "form_build_id" : "form-spHBAv2MkW7Wxg4cKVL6KXyjoK-miKif2c9Y_wArxM4",
        "form_id" : "ajax_example_form",
        "casetype" : "15",
        "caseno" : "2",#case_no,
        "caseyear" : "2022",#case_year,
        "_triggering_element_name" : "op",
        "_triggering_element_value" : "Search",
        "_drupal_ajax" : "1",
        "ajax_page_state[theme]" : "mytheme",
        "ajax_page_state[theme_token]" : "",
        "ajax_page_state[libraries]" : "asset_injector/css/animation_accordin,asset_injector/css/contract_style,asset_injector/css/judgeprofile,asset_injector/css/side_bar,asset_injector/css/table,asset_injector/js/districthideshow,asset_injector/js/seperate_tab_,core/drupal.ajax,core/html5shiv,core/jquery.form,mytheme/mylibrarynew,system/base,views/views.module"

    }


res1 = session.post(url1 , headers=Headers1 , data=payload1 , verify = False)
data = res1.json()
soup1 = BeautifulSoup(data[1]["data"] , "lxml")
url_details = soup1.find("a",{"class":"use-ajax"})['href']
details = base_url + url_details

output_data = []
case_details_value = {}
res2 = session.post(details , headers=Headers1 , verify = False)
data2 =  res2.json()
soup2 = BeautifulSoup(data2[0]["data"] , "lxml")

case_details_div = soup2.find_all("div")
case_details = case_details_div[1].find_all("div", {"class":"col-md-6"})
token_num = case_details[1].text.strip()
case_type = case_details[3].text.strip()
date_filing = case_details[5].text.strip()
case_status = case_details[7].text.strip()
case_number = case_details[9].text.strip()
cnr_number = case_details[11].text.strip()
next_date = case_details[13].text.strip()

case_details_value["Token Number"] = token_num
case_details_value["Case Type"] = case_type
case_details_value["Date of Filing"] = date_filing
case_details_value["Case Status"] = case_status
case_details_value["Case Number"] = case_number
case_details_value["CNR"] = cnr_number
case_details_value["Next Date"] = next_date

output_data.append(case_details_value)
print(output_data)