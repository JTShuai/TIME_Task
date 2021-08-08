# -*- coding: utf-8 -*-

"""
Task 4: visualise the min and max bounty

@author: Jiangtao Shuai
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


class TaskFour:
    def __init__(self, file_name):
        self.df = pd.read_csv(file_name)

    def processBountyData(self):
        """
        process the min bounty and max bounty, filter the data in which the program dose not offer bounty

        :return: df_bounty  --  DataFrame
        """

        # get data of MinBounty and MaxBounty columns
        df_bounty = self.df.loc[:, ['MinBounty', 'MaxBounty']].astype(float)

        # filter the non-bounty program
        df_bounty = df_bounty.loc[df_bounty['MaxBounty'] > 0, ['MinBounty', 'MaxBounty']]

        # round the value
        df_bounty = df_bounty.apply(lambda x: round(x, -3))
        
        return df_bounty

    def plotHistogram(self, df_bounty= None, isSave = False):
        """
        plot the histogram based on the processed data

        :param df_bounty: processed bounty data
        :type df_bounty: DataFrame

        :param isSave: determine if the figure be saved in folder
        :type isSave: Boolean
        """
        if df_bounty is None:
            df_bounty = self.processBountyData()

        # plot the histograms
        df_bounty.hist()

        if isSave:
            plt.savefig('./output/task_four.png')



if __name__ == '__main__':
    print("launching")
    file = './output/task_three.csv'

    task_four = TaskFour(file)
    task_four.plotHistogram(isSave=True)
    plt.show()
    # processed_df = task_four.processBountyData()
    # processed_df.to_csv('./output/test.csv')
