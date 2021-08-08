# -*- coding: utf-8 -*-

"""
Sample task of TIME

@author: Jiangtao Shuai
"""
from step_1 import TaskOne
from step_2 import TaskTwo
from step_3 import TaskThree
from step_4 import TaskFour
import datetime


print("Launching")
start = datetime.datetime.now()

# step_1
PRIMATE_URL = "https://bugcrowd.com"
DYNAMIC_URL = "https://bugcrowd.com/programs.json?sort[]=promoted-desc&offset[]="
BASE_NUM = 25

scrapy = TaskOne(PRIMATE_URL, DYNAMIC_URL, BASE_NUM)
scrapy.exportScrapyResult("task_one.csv")

# step_2 & step_3
file_one = './output/task_one.csv'

task_three = TaskThree(file_one)
task_three.exportProgramBountyDataFrame("task_three.csv")

# step_4
file_three = './output/task_three.csv'

task_four = TaskFour(file_three)
task_four.plotHistogram(isSave=True)


end = datetime.datetime.now()
print(end - start)



