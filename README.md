# Sample Task
Sample task of TIME

## Task 1
The codes are in the *step_1.py*. The scraped program name and program url were saved in *task_one.csv* of the output folder.

## Task 2
The codes are in the *step_2.py*. This script extracts the information within the *program details tab* 
and encapsulate it in the *ProgramDetailData* object.

## Task 3
The corresponding codes are in the *step_3.py*. This script process the generated *ProgramDetailData* object in order to 
get the min bounty and max bounty of each program. 
*To some programs does not mention the bounty, the min and max bounties are assigned as '0.0'.*

**ATTENTION: There are some programs, in which the bounties are not involved in the "program details" tab. 
In this way, the min bounty and max bounty did not be collected.
(e.g., https://bugcrowd.com/programs/teasers/Pn7YEFSanfM8zqKGDo6rdZce)**

## Task 4
The corresponding codes are in the *step_4.py*. This script rounds the bounties and plots the bounty histogram figure.
The resulted figure were saved as *'task_four.png'* in the output folder.

## Task 5
How to structure the texts automatically and to convert thematically similar blocks into a uniform format?

 - structure the texts automatically:  use embedding technique. e.g., doc2vec.
 - convert similar blocks into a uniform format: 
    - Classifier based methods: based the embedded vector, every block can be labeled by a trained classifier(e.g., SVM), then the similar blocks would be classified with the same label.
    - Clustering based methods: based the embedded vector, clustering method, e.g., K-means, can be applied in order to group the similar blocks.


