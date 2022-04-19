from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(20)
wait = WebDriverWait(driver, 20)

########
# This function calls the function in graph.py moudle in order to create a diagram
names = []
number_of_vill = []
from graph import *

########
def start_func(name):
    if name == "Haifa":
        driver.get("https://www.zochrot.org/villages/district_view/38/en?Haifa")
    elif name == "Jaffa":
        driver.get("https://www.zochrot.org/villages/district_view/1/en?Jaffa")
    elif name == "Akka__Acre_":
        driver.get("https://www.zochrot.org/villages/district_view/2/en?Akka__Acre_")
    elif name == "alQuds__Jerusalem_":
        driver.get("https://www.zochrot.org/villages/district_view/40/en?alQuds__Jerusalem_")
    elif name == "Gaza":
        driver.get("https://www.zochrot.org/villages/district_view/37/en?Gaza")
    elif name == "Nazareth":
        driver.get("https://www.zochrot.org/villages/district_view/41/en?Nazareth")
    elif name == "Ramla":
        driver.get("https://www.zochrot.org/villages/district_view/34/en?Ramla")
    elif name == "Safed":
        driver.get("https://www.zochrot.org/villages/district_view/43/en?Safed")
    elif name == "Tiberias":
        driver.get("https://www.zochrot.org/villages/district_view/44/en?Tiberias")
    main_fun(name)

########
def main_fun(name):
    
    if name == "Akka__Acre_":
        name = "Akka"
    elif name == "alQuds__Jerusalem_":
        name = "al-Quds"
    
    create_file(name)
    i = 1
    while True:
        x = ret_elements('//*[@id="main"]/section[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[' + str(i) + ']')
        if x == []: 
            break

        # write_to_files
        write_line(name + "_Info", x, i)
        villages_map.update({name: i})
        #more_info_into_file(name, x, i)
        i = i + 1

########
def ret_elements(xpath):
    arr = []
    for x in driver.find_elements(By.XPATH, xpath):
        arr.append(x.text)
    return arr

########
def create_file(name):
    f = open("./" + name + "/" + name + "_list.txt", "a", encoding="utf-8")
    f.write("Localities Of " + name + " Descret:\n\n")

########
def write_line(name, elements, num):
    name = name.split("_")[0]
    path = "./" + name + '/'
    f = open(path + name + "_list.txt", "a", encoding="utf-8")
    str1 = elements[0]
    f.write(str(num) + ". " + str1 +'\n')
    more_info(num, path, str1, elements)

########
def more_info(num, path, name, elements):
        j = 1
        href = ""
        href = driver.find_element_by_xpath('//*[@id="main"]/section[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div['+ str(num) + ']/a').get_attribute('href')
        driver.get(href)
        info = ret_elements('//*[@id="info"]')
        info_array = info[0].split("\n")
        f = open(path + name + "_Info.txt", "w", encoding="utf-8") 
        f.write(name + "\n\n")
        for j in range(1, len(info_array)):
            f.write("   " + str(info_array[j]) + "\r")
        f.write("\n")
        driver.back()

def create_map(name):
    names.append(name)
    number_of_vill.append(villages_map[name])
