from scraping_data import myclass
from bs4 import BeautifulSoup


baseurl = "https://www.adamchoi.co.uk/bttsresult/detailed"

scrape = myclass() 
my_driver = scrape.create_driver("--headless")
src = scrape.get_website(url= baseurl, webdriver=my_driver, wait_time=5) 

def parse_html(page_src:str, parser = "html.parser"):
        """
        Creating soup object\n
        Getting win rates and team names\n
        They both will be returning a list\n
        :parser: a parser to parse, "html.parser", "lxml"
        :page_src: page_source
        """

        soup = BeautifulSoup(page_src, parser)
        win_rates = soup.find_all("div", class_ = "progress-bar progress-bar-success ng-binding")
        teams = soup.find_all("div", class_ = "col-lg-3 col-sm-6 col-xs-12 ng-binding")

        """
        Getting the texts from the lists and storing inside a new list 
        Since there are three win rates for all teams
        Grouping up three by three
        """
        win_rates_list = [win_rate.get_text() for win_rate in win_rates]
        win_rates_nested_list = [win_rates_list[i:i+3] for i in range(0, len(win_rates_list), 3)]

        """
        Teams list does not have only the team names
        Items looks like this: Aston Villa Overall BTTS Win
        Using string methods to get the team name
        """
        team_name_list = []
        for team_name in teams:
            text = team_name.get_text()
            index = text.find("Overall")  
            team_name_list.append(text[:index-1])

        """
        Merging team names and win rates 
        Returning a nested list that stores the team names and win rates 
        """
        for i in range(len(team_name_list)):
            win_rates_nested_list[i].insert(0, team_name_list[i])

        return win_rates_nested_list

data = parse_html(page_src=src) 
scrape.create_csv(csv_name="btts_data.csv", data=data, column_names=["Teams", "Overall Win Rate", "Home Win Rate", "Away Win Rate"])