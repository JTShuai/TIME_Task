# -*- coding: utf-8 -*-

"""
Task 1: extract program name and program-URL from https://bugcrowd.com/programs

@author: Jiangtao Shuai
"""
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


class TaskOne:
    """
    task 1 : scraping all program names and urls from https://bugcrowd.com/programs
    """
    output_path = "./output"

    def __init__(self, primate_url, dynamic_url, base_num):
        self.primate_url = primate_url
        self.dynamic_url = dynamic_url
        self.base_num = base_num

    def extractProgramsInfo(self):
        """
        extract all program names and URLs from the website

        :return: program_info_df --  DataFrame
        """
        k = 0
        program_name_list = []
        program_url_list = []

        # start scraping
        while True:
            # connect to the website
            current_page = self.dynamic_url + str(k * self.base_num)
            response = requests.get(current_page)

            content_dict = json.loads(response.content)
            programs = content_dict["programs"]

            # check if all programs have been recorded
            if not programs:
                break

            # traverse all programs within the current page
            for program in programs:
                program_name_list.append(program["name"])
                program_url_list.append(self.primate_url + program["program_url"])

            # update step value
            k += 1

        # reformulate the data structure
        program_info_df = pd.DataFrame(list(zip(program_name_list,program_url_list)),
                                       columns=['program_name', 'program_url']
                                       )

        return program_info_df

    def exportScrapyResult(self, file_name, program_info_df=None):
        """
        export the extracted information to .csv file

        :param file_name: the saved .csv file name without specified save path
        :type file_name: String

        :param program_info_df: the extracted information
        :type program_info_df: DataFrame
        """
        if program_info_df is None:
            program_info_df = self.extractProgramsInfo()

        # check the saving directory
        if not os.path.exists(self.output_path):
            os.mkdir(self.output_path)

        program_info_df.to_csv(os.path.join(self.output_path, file_name))






if __name__ == "__main__":
    print("Launching")

    PRIMATE_URL = "https://bugcrowd.com"
    DYNAMIC_URL = "https://bugcrowd.com/programs.json?sort[]=promoted-desc&offset[]="
    BASE_NUM = 25

    scrapy = TaskOne(PRIMATE_URL, DYNAMIC_URL, BASE_NUM)
    scrapy.exportScrapyResult("task_one.csv")

    print("finish")
