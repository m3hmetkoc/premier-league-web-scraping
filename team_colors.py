from bs4 import BeautifulSoup
from premier_league.scraping_data import myclass

baseurl = "https://www.premierleague.com"

scrape = myclass() 
my_driver = scrape.create_driver("--headless")
src = scrape.get_website(url= baseurl + "/clubs", webdriver=my_driver, wait_time=5) 

def get_links(page_src, parser="html.parser"):
    """
    Creating soup object\n
    Getting hex codes of the colors\n
    They both will be returning a list\n
    :parser: a parser to parse, "html.parser", "lxml"
    :page_src: page_source

    """
    soup = BeautifulSoup(page_src, parser)
    team_links = soup.find_all("li", class_ = "club-card-wrapper")

    """
    Getting club page links
    Storing inside a list
    """
    link_list=[]
    for item in team_links:
        for link in item.find_all("a", href=True):
            link_list.append(baseurl + link["href"]) 
    
    return link_list

def get_colors(link_list:list):
    """
    link_list: club pages links
    """

    """
    Getting hex codes 
    Storing inside a list
    """
    color_list = []
    for link in link_list:
        source = scrape.get_website(url=link, webdriver=my_driver, wait_time=0)
        my_soup = BeautifulSoup(source, "lxml") 
        color_list.append(my_soup.find_all("stop", attrs = {"offset": "100%"})[0]["stop-color"])
    return color_list

links = get_links(page_src=src)  
data = get_colors(links) 
scrape.create_csv("team_colors.csv", data= data, column_names=["Color Codes"])
             
                                 