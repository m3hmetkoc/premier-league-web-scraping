from selenium import webdriver
import pandas as pd 

class myclass():

    def __init__(self):
        pass

    def create_driver(self, args:tuple = None):
        """
        Creating the webdriver\n
        Can pass an argument for options of webdriver\n
        To pass multiple arguments, pass a tuple of strings\n
        return: webdriver.Chrome
        """
        options = webdriver.ChromeOptions() 
        if args != None : options.add_argument(args)
        driver = webdriver.Chrome(options=options) 

        return driver

    def get_website(self, url: str, webdriver: webdriver.Chrome, wait_time: float):
        """
        Getting the url\n
        Clicking a button (optional)\n
        Returning the page source\n
        url: must be string 
        webdriver: webdriver object
        return: page_source
        """
        try:
            webdriver.get(url) 
            webdriver.implicitly_wait(wait_time)
            #btn = webdriver.find_element("xpath", '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
            #btn.click()
        except:
            ConnectionError("There is an error occured, connection fail")
            
        return webdriver.page_source

    def create_csv(self, csv_name:str , data:list, column_names:list):
        """
        Creating the dataframe\n
        Storing in a csv file\n
        Pass csv name as an argument\n
        csv_name: must be string, data: data to map on the dataframe, column_names: must be list of strings
        """
        try:
            df = pd.DataFrame(data, columns = column_names)
            df.to_csv(csv_name, index=False)
        except:
            raise ValueError("Length of data has more or less columns")
        




