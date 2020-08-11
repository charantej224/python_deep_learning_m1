from bs4 import BeautifulSoup

from models.employee import Employee
from models.fulltime_employee import FullTimeEmployee
from webapps.web_reader import WebReader
from vector.vector import Vector


def main():
    problem1()
    problem2()
    problem3()


def problem1():
    employees = []
    print("running the main method")
    fulltime1 = FullTimeEmployee("Employee1", "FamilyName1", 175000, "Digital")
    fulltime1.full_time_benefits()
    fulltime2 = FullTimeEmployee("Employee2", "FamilyName2", 175000, "Digital")
    fulltime3 = FullTimeEmployee("Employee3", "FamilyName3", 175000, "Digital")
    fulltime4 = FullTimeEmployee("Employee4", "FamilyName4", 175000, "Digital")
    employees.append(fulltime1)
    employees.append(fulltime2)
    employees.append(fulltime3)
    employees.append(fulltime4)
    print("average salary")
    print(FullTimeEmployee.average_salary(employees))


def problem2():
    webreader = WebReader()
    raw_html = webreader.read_web_content("https://en.wikipedia.org/wiki/Deep_learning")
    soup = BeautifulSoup(raw_html, 'html.parser')
    print("title of the page {0}".format(soup.title.string))
    print("Found href links with html element a")
    number_of_links = 0
    for link in soup.find_all('a'):
        number_of_links += 1
        print(link.get('href'))
    print("number of links in a are {0}".format(number_of_links))


def problem3():
    value = Vector()
    output = value.reshape(value.generate_random(15), 3, 5)
    value.replace_maxmium(output, 0, 1)



if __name__ == "__main__":
    main()
