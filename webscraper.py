from selenium import webdriver
import pandas as pd
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

us_state_abbrev = {
    "Alabama": "AL",
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)


driver.get("https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html")
driver.execute_script("window.scrollTo(0, 4000)") 						# allows clicker  to work

driver.find_element_by_xpath('/html/body/div[1]/main/article/section/div/div/div[4]/div/button').click()


tbody = driver.find_element_by_tag_name('tbody')
rows = tbody.find_elements_by_tag_name("tr") # get all of the rows in the table

#f = open('stats_TXT.txt', 'a')
f = open('stats_CSV.csv', 'a')
f.truncate(0)
f.write("State,Cases,Deaths,Website\n")

for row in rows:
	state = row.find_elements_by_tag_name("td")[0] 					#state
	cases = row.find_elements_by_tag_name("td")[1]					#cases
	deaths = row.find_elements_by_tag_name("td")[2]					#deaths
	stateinitial = us_state_abbrev[state.text]
	website = ("https://coronavirus.%s.gov" % stateinitial)
	#hyperlink = ("=HYPERLINK("'"%s"'")" % website)
	cases1 = cases.text
	deaths1 = deaths.text
	cases1 = cases1.replace(',','')
	deaths1 = deaths1.replace(',','')
	f.writelines([state.text, ',', cases1, ',' , deaths1, ',' , website, "\n"])
f.close()
driver.close()


