from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.universityadmissions.se/intl/search?period=10&graduateLevel=on&semesterPart=0&languageOfInstruction=en'

#opening up connection, grabbing the page
uClient = uReq(my_url)
#loads content into variable
page_html = uClient.read()
#close client
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

# grabs each course
containers = page_soup.findAll("div", {"class": "namearea"})

filename = "majors.csv"
f = open(filename, "w")

headers = "course_name, college_name, college_location\n"

f.write(headers)

#gets the title of image
for container in containers:
	#Course Name
	course_container = container.findAll("h3", {"class":"heading4"})
	course_name = course_container[0].text.strip()

	#Name of college
	college_container = container.findAll("span", {"class":"appl_fontsmall"})
	college_nameComplex = college_container[1].text.split("Credits,")
	college_nameLessComplex = college_nameComplex[1].split("Location:")
	college_name = college_nameLessComplex[0].strip()

	#College Location
	college_location = college_nameLessComplex[len(college_nameLessComplex)-1].strip()

	f.write(course_name + "," + college_name + "," + college_location + "\n")

f.close()