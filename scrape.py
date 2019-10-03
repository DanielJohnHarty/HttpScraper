
from bs4 import BeautifulSoup
import requests

target = r"https://www.datasciencetech.institute/applied-msc-in-data-engineering"
response = requests.get(target)
html = response.content
output_file = "module_descs.txt"
soup = BeautifulSoup(html, 'html.parser')


with open(output_file, 'w') as file:
    for tag in soup.find_all("strong"): # all module descriptuions are in <strong> tags
        if 'hrs' in tag.text: # each module description has a number of hours
            print(tag.text)
            file.write(tag.text + "\n") #Print the text and write it to the file


