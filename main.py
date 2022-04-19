import os

def is_legal_name(name):
    if name == "Akka":
        return "Akka__Acre_"
    elif name == "al-Quds":
        return "alQuds__Jerusalem_"
    elif name == "Gaza":
        return "Gaza"
    elif name == "Haifa":
        return "Haifa"
    elif name == "Jaffa":
        return "Jaffa"
    elif name == "Nazareth":
        return "Nazareth"
    elif name == "Ramla":
        return "Ramla"
    elif name == "Safed":
        return "Safed"
    elif name == "Tiberias":
        return "Tiberias"
    elif name == "exit":
        return "exit"
    else:
        return "Illegal Input!"

def call_webDriver(name):
    web_name = is_legal_name(name)
    if web_name == "Illegal Input!":
        print("Illegal Input!")
    else:
        os.makedirs("./" + name, exist_ok = True)
        start_func(web_name)
        create_map(name)
        '''
        moduleName = "webDriver"
        __import__(moduleName)
        moduleName.start_func(web_name)
        '''

print("*******************************************************************************************************************")
print("                        ******* Welcone To The Digital Humanities Mini Project! *******")
print("You can pick one of the names of cities or villages from the short story: \"The Land Of The Sad Oranges\"")
print("to get to the specific web-page of the \"Zpchrot\" website, and the accordingly information files:")
print("  Akka, al-Quds, Gaza, Haifa, Jaffa, Nazareth, Ramla, Safed, or Tiberias")

print("******************************************************************************************************************")
name = ""

while name != "exit":
    name = input("Please enter the name of the city, or \"exit\" if you wish the program to stop: ")
    if name == "exit":
        print("The Program Been Has Stopped Successfully!")
        driver.close()
        break
    from webDriver import *
    call_webDriver(name)
    driver.implicitly_wait(20)

'''

call_webDriver("Akka")
call_webDriver("al-Quds")
call_webDriver("Gaza")
call_webDriver("Haifa")
call_webDriver("Jaffa")
call_webDriver("Nazareth")
call_webDriver("Ramla")
call_webDriver("Safed")
call_webDriver("Tiberias")
'''


get_data(names, number_of_vill)