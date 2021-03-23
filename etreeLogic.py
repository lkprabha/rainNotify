from selenium import webdriver
import etree_Convert
import emailConfig

if __name__ == '__main__':
    browser = webdriver.Chrome()
    page_Source = "https://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597?day=1"
    browser.get(page_Source)
    html = browser.page_source

    etClient = etree_Convert.eTree_allocation(html)
    RainDiv = etClient.raindiv()

    rainmm= float(str(RainDiv[0].text[0: -2]))

    if rainmm <= 0:
        #print("Today is a sunny day !!")
        msg = "Today is a sunny day !!"
        eclient = emailConfig.configEmailSend.sendemail(msg)
    else:
        #print("To day is a rainy day and precipitation is: " + str(rainmm)+" mm ")
        msg = "To day is a rainy day and precipitation is: " + str(rainmm)+" mm "
        eclient = emailConfig.configEmailSend.sendemail(msg)
else:
    quit()

