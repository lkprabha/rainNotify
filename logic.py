import self as self
from lxml import etree
from selenium import webdriver

#Asign web page in to etree structure
class PageWithListings:
    def __init__(self, page_source):
        self.tree = etree.HTML(page_source)

   def get_listings(self):
       result_Locator =  "//div[@class='right']/p[@class='panel-item']/span[@class='value']"
       result_divs = self.tree.findall(result_Locator)
       return result_divs

  def RainAmount(self, rainmm):
        rainmm = self.result_divs[0].text
        return rainmm

 if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("https://www.accuweather.com/en/sg/singapore/300597/daily-weather-forecast/300597?day=1")
    html = browser.page_source

    listings_page = PageWithListings(html)

  #  rainFall
    if RainAmount() > 0:
            print("To day is a rainy day and precipitation is: ",RainAmount().text)
    else:
        print("To day is a sunny day!")
browser.quit()






