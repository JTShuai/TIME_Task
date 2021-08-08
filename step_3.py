# -*- coding: utf-8 -*-

"""
Task 3: extract minimal bounty and max bounty of each program

@author: Jiangtao Shuai
"""

from step_2 import TaskTwo, ProgramDetailData
import re
import os


class TaskThree(TaskTwo):

    def __init__(self, file_name):
        super(TaskThree, self).__init__(file_name)

        self.pattern = re.compile(r'(?:[\$]{1}[,\d]+.?\d*\b)')
        self.reward_ranges = 'rewardRanges'

    def extractDescriptionCurrencyList(self, program_data: ProgramDetailData):
        """
        :param program_data: extracted program details
        :type program_data: ProgramDetailData

        :return: currency_list  --  List
        """

        currency_list = []

        # search all bounty from text
        description_matches = re.findall(self.pattern, program_data.description)
        if description_matches:
            try:
                currency_list.extend(self.__reformulateCurrencyToNumber(description_matches))
                currency_list.sort()
            except:
                print(program_data.program_url)

        return currency_list

    def __reformulateCurrencyToNumber(self, currency_list):
        """
        delete dollar sign and comma
        """

        try:
            number_list = [float(re.sub("[^-0-9.]", '', x)) for x in currency_list]
            return number_list
        except:
            print(currency_list)

    def getMinAndMaxBounty(self, program_data: ProgramDetailData):
        """
        Get the min and max bounty of one program.
        if the program does not have the bounty, then both of the min and max bounty are assigned as "0.0".

        :param program_data: encapsulated program details
        :type program_data: ProgramDetailData

        :returns: min_bounty  --  String, max_bounty  --  String
        """

        min_bounty = ''
        max_bounty = ''

        # check if there is a scope
        scope_list = program_data.scope_list
        if scope_list:
            boundary_bounty = scope_list[0][self.reward_ranges]

            min_bounty += str(boundary_bounty['min'])
            max_bounty += str(boundary_bounty['max'])
        else:
            # search bounty in description text
            text_currency_list = self.extractDescriptionCurrencyList(program_data)

            # check if the list is empty
            if text_currency_list:
                min_bounty += str(text_currency_list[0])
                max_bounty += str(text_currency_list[-1])
            else:
                min_bounty = '0.0'
                max_bounty = '0.0'

        return min_bounty, max_bounty
    
    def getProgramBountyDataFrame(self):
        """
        traverse all program details in order to collect the bounties in a dataframe

        :return: program_url_df  --  DataFrame
        """

        all_program_obj_list = task_three.extractProgramDetail(True)

        min_bounty_list = []
        max_bounty_list = []

        # search boundary bounties of all programs
        for program in all_program_obj_list:
            min_bounty, max_bounty = self.getMinAndMaxBounty(program)
            min_bounty_list.append(min_bounty)
            max_bounty_list.append(max_bounty)

        program_url_df = self.program_df
        program_url_df['MinBounty'] = min_bounty_list
        program_url_df['MaxBounty'] = max_bounty_list

        # rename the first two columns
        program_url_df = program_url_df.rename(columns={"program_name": "Name",
                                                        "program_url": "URL"})
        program_url_df = program_url_df.drop(columns=['Unnamed: 0'])

        return program_url_df

    def exportProgramBountyDataFrame(self, file_name):
        """
        export the searched result to .csv file
        """

        program_url_df = self.getProgramBountyDataFrame()
        program_url_df.to_csv(os.path.join(self.output_path, file_name))


if __name__ == "__main__":
    print("Launching")

    file = './output/task_one.csv'

    task_three = TaskThree(file)
    task_three.exportProgramBountyDataFrame("task_three.csv")

    print("finish")
