from django.http import HttpResponse
import csv
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

def data(request):
    return render(request, 'submit.html')

def scrape_data(request):
    # Write your web scraping code here
    # Return scraped data as a list of lists (each list representing a row)
    url = "https://www.naukri.com/data-analyst-jobs?k=data%20analyst&nignbevent_src=jobsearchDeskGNB&experience=0&jobAge=7&jobPostType=1"
    n = requests.get(url)
    soup = BeautifulSoup(n.text, "html.parser")
    print(soup)
  
    
    # Job Title
    job_title = soup.find_all("div", class_="row1")
    print(job_title)
    title_name = [i.text for i in job_title]

    # Comapny
    company = soup.find_all("a", class_=" comp-name")
    company_list = [i.text for i in company]

    # yrs
    year = soup.find_all("span", class_="expwdth")
    years_exp = [i.text for i in year]

    # sal
    sal = soup.find_all("span", title_="Not disclosed ")
    salary = [i.text for i in sal]

    # degree
    degree = soup.find_all("span", class_="job-desc")
    degree_qul = [i.text for i in degree]

    # keypoints
    keys = soup.find_all("ul", class_="tags-gt ")
    key_points = [i.text for i in keys]

    # Add serial numbers
    serial_numbers = list(range(1, len(title_name) + 1))

    # Saving data in CSV
    df = pd.DataFrame({"SL.No": serial_numbers, "Job_Title": title_name, "Company": company_list, "years": years_exp, "Sal": salary, "degree":degree_qul,"keys":key_points})
    csv_output = io.StringIO()
    df.to_csv(csv_output, index=False)
    csv_output.seek(0)

    # Return CSV as HttpResponse for download
    response = HttpResponse(csv_output, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Naukri.csv'
    return response
 