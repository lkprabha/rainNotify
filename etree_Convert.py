from lxml import etree


class eTree_allocation:
    def __init__(self, page_Source):
        self.tree = etree.HTML(page_Source)

    def raindiv(self):
        locator = ".//div[@class='right']/p[@class='panel-item']/span[@class='value']"
        divs = self.tree.findall(locator)
        return divs

