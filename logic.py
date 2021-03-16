from selenium import webdriver

browser = webdriver.Chrome()
url = "https://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597?day=1"
browser.get(url)

element_xpath = "//div[@class='right']/p[@class='panel-item']/span[@class='value']"

element_precipitation_Tuple = browser.find_element_by_xpath(element_xpath)
element_value = (element_precipitation_Tuple).text
element_substring_float = float(element_value[:-2])

print(float(element_substring_float))

if element_substring_float > 0:
    print("Today is a RAINY DAY Precipitation is  : ", element_value)
else:
    print("To day is a sunny Day :) ")

print("test")




