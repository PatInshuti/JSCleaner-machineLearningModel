
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from browsermobproxy import Server
# import json

# # from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options as FirefoxOptions


# server = Server("/Users/manesha/Desktop/University/Capstone/JSCleaner-machineLearningModel/evaluation/browsermob-proxy/bin/browsermob-proxy")
# server.start()
# proxy = server.create_proxy()

# d = DesiredCapabilities.FIREFOX
# d['loggingPrefs'] = {'browser': 'ALL'}

# firefox_binary = '/usr/local/bin/firefox-developer'  # Must be the developer edition!!!
# # driver = webdriver.Firefox(firefox_binary=firefox_binary)
# fp = webdriver.FirefoxProfile('/Users/manesha/Library/Application Support/Firefox/Profiles/et1zmgvb.Capstone')

# fp.set_proxy(proxy.selenium_proxy())
# driver = webdriver.Firefox(fp,  capabilities=d)


#  get websites from txt files


# driver.get(websites[0])


# proxy.new_har(websites[0], options={'captureHeaders': True})

# result = json.dumps(proxy.har, ensure_ascii=False)
# print result
# server.stop()    
# driver.quit()

# # a = input("go")


import os

# f_websites = open("websites.txt", "r")
# websites = []
# # store websites in an array
# for i in range(100):
#     websites.append(f_websites.readline().rstrip())


# for url in websites:
command = "python harRecorder/harRecorder.py" 
print command
os.system(command)
