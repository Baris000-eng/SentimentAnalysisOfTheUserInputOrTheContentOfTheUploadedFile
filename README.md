# SentimentAnalysisOfTheUserInputOrTheContentOfTheUploadedFile
This project provides a sentiment analysis of the user input or the content of the uploaded text file.

First Note: For testing my application, you can use any IDE (Integrated Development Environment) you want. However, PyCharm is recommended.

How to set up?

1-) Firstly, fork the project from my Github repository to your Github repository. After that, you can clone the project to your local machine by using the following command:

git clone https://github.com/Baris000-eng/SentimentAnalysisOfTheUserInputOrTheContentOfTheUploadedFile

2-) You should go to the directory of the project with "cd" command.
e.g. cd path/to/project

3-) Then, you should run one of the following commands from the terminal.

- python sentimentAnalysisOfUserInputOrUploadedFile.py
- python3 sentimentAnalysisOfUserInputOrUploadedFile.py

Note 1: Only if your python version in your computer is python 3.x, then you can run the second command. The first command directly considers the default python configuration in your computer regardless of what version you already installed.

Note 2: At the second step, you can run the python file also by right clicking on the name of the python file 
(e.g. sentimentAnalysisOfUserInputOrUploadedFile.py) and then pressing the option called 
"Run sentimentAnalysisOfUserInputOrUploadedFile.py".

4-) Now, you can obtain sentiment analysis of the inputted text in one of the following ways: 
  * Input any text you want to the text area, press the "Analyze Text" button, and then examine the compound, positive, negative,      and neutral scores.
  * Press the "Upload File" button, pick any txt file you want from your computer, press the "Analyze Text" button, and then examine   the compound, positive, negative, neutral scores.


Important Note: For providing the sentiment analysis, the VADER library is utilized. VADER is an open-source and rule-based NLP tool which is used for the sentiment analysis.

