# -*- coding: utf-8 -*-

"""
Task 2: scrape program details tab in terms of the program url resulted from step 1

@author: Jiangtao Shuai
"""
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


class ProgramDetailData:
    """
    encapsulate the data of program details tab
    """

    def __init__(self):
        self.description = None
        self.scope_list = None
        self.program_url = None


class TaskTwo:
    """
    Task 2: extract program details based on program url of the saved .csv file
    """
    output_path = "./output"

    def __init__(self, file_name):
        self.file_name = file_name
        self.program_df = None

    def readFile(self):
        """
        read the saved .csv file

        :return: --  Dataframe
        """
        self.program_df = pd.read_csv(self.file_name)
        return self.program_df

    def getProgramUrlList(self, program_df=None):
        """
        convert the program_url column to list

        :param program_df: the dataframe of the task one saved .csv file
        :type program_df: DataFrame

        :return: program_url_list  --  List
        """
        if program_df is None:
            program_df = self.readFile()

        program_url_list = program_df.program_url.to_list()

        return program_url_list

    def extractProgramDetailFromUrl(self, program_url):
        """
        extract information from program detail tab

        :param program_url: program url
        :type program_url: String

        :return: program_details  --  List
        """
        program_details = ProgramDetailData()
        program_details.program_url = program_url

        program_response = requests.get(program_url)
        program_soup = BeautifulSoup(program_response.text, 'html.parser')

        # description part
        description = ''
        program_section_list = program_soup.find_all('div', class_="bounty-section")
        for section in program_section_list:
            description = description + section.text

        program_details.description = description

        # scope part
        program_scope = program_soup.find_all('div', class_='react-component-researcher-target-groups')
        scope_list = []
        if program_scope is not None:
            for scope in program_scope:
                scope_info = json.loads(scope.attrs['data-react-props'])
                scope_list.append(scope_info)

        program_details.scope_list = scope_list

        return program_details

    def extractProgramDetail(self, is_all=False):
        """
        collect details in one list

        :param is_all: if search all programs
        :type is_all: Boolean

        :return: detail_list  --  List
        """

        detail_list = []
        if is_all:
            url_list = self.getProgramUrlList()
            for url in url_list:
                detail_list.append(self.extractProgramDetailFromUrl(url))

        else:
            program_df = self.readFile()
            sample_url = program_df.program_url[0]

            detail_list.append(self.extractProgramDetailFromUrl(sample_url))

        return detail_list


if __name__ == "__main__":
    print("Launching")

    file = './output/task_one.csv'
    task_two = TaskTwo(file)
    program_detail = task_two.extractProgramDetail()
    print(program_detail[0].description)

    print("finish")
