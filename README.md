# Data Analysis of U.S. Medical Insurance Costs
This project,
provided by [Codecademy](https://www.codecademy.com/) as part of the Data Science Foundations course,
explores a dataset of medical insurance costs for individuals in the U.S.
using statistical analysis techniques in Python 3.11 and Jupyter Notebook.

## Before You Begin

Before doing anything,
please note that there is a `reports` directory in this project.
This directory contains the reports that I have generated using the Jupyter Notebook environment.
These are HTML files that can be opened in any browser thus don't require Jupyter Notebook to be installed.
Installing Jupyter can be troublesome, so I recommend opening the reports in the `reports` directory.

Additionally, if you are seeing this in GitHub, you can view the notebooks in the `notebooks` directory.
GitHub provides a preview for all Jupyter Notebook files, so you can view them directly in the browser.

## Installation

If you want to run the project yourself, you will need to install any of the following:
- Python 3.11+
- Conda environment(s)

Both of these installations require Jupyter to be installed,
but Conda environments might have them installed by default
depending on your environment configuration.

You need to install the dependencies in the `requirements.txt` file if you want to run the notebook.
_(The requirements also include Jupyter)_

You can install the `requirements.txt` file by running the following command in your terminal:
```bash
pip install -r requirements.txt
```
_(Tip: You can write `pip install -r` and then drag
and drop the `requirements.txt` file into the terminal 
to automatically write the path to the file)_

## Usage

I strongly recommend you first `cd` into the project directory before running the project,
since it might be difficult to find the notebook otherwise.

You can run the project (the Jupyter Notebook) by running the following command in your console:
```bash
jupyter notebook
```
This should open a browser window with the Jupyter Notebook environment on the directory you ran the command in.
You will have to select the notebook on the page that opens.

If you are using PyCharm, then you can execute the notebook directly in the editor.
_(I like to work like this, but I still recommend the browser version)_

# Project Description
_Provided by Codecademy_

For this project,
you will be investigating a medical insurance costs dataset in a .csv file
using the Python skills that you've developed.
This dataset and its parameters will seem familiar
if you've done any of the previous Python projects in the data science path.

However,
you're now tasked with working with the actual information in the dataset
and performing your own independent analysis on real-world data!
We will not be providing step-by-step instructions on what to do,
but we will provide you with a framework to structure your exploration and analysis.
For this project,
you will be investigating a medical insurance costs dataset in a .csv file
using the Python skills that you've developed.
This dataset and its parameters will seem familiar
if you've done any of the previous Python projects in the data science path.

## Project Objectives

- Work locally on your own computer
- Import a dataset into your program
- Analyze a dataset by building out functions or class methods
- Use libraries to assist in your analysis
- Optional: Document and organize your findings
- Optional: Make predictions about a dataset’s features based on your findings

# About the dataset

The dataset is stored in a `.csv` file. 
This dataset can be found, along with other datasets, [here](https://github.com/stedy/Machine-Learning-with-R-datasets).

Originally, this dataset is used for a prediction analysis, provided by the author, Brett Lantz.
In [kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance), the following quote is provided:

> Machine Learning with R by Brett Lantz is a book that provides an introduction to machine learning using R. 
> As far as I can tell, Packt Publishing does not make its datasets available online unless you buy the book and create 
> a user account which can be a problem if you are checking the book out from the library or borrowing the book from 
> a friend.
> All of these datasets are in the public domain
> but simply needed some cleaning up and recoding to match the format in the book.

## Content of the dataset

The dataset contains the following columns:
- `age`: age of primary beneficiary.
- `sex`: insurance contractor gender, female, male.
- `bmi`: Body mass index,
  providing an understanding of body,
  weights that are relatively high or low relative to height,objective index of body weight
  (kg / m ^ 2) using the ratio of height to weight,
  ideally 18.5 to 24.9.
- `children`: Number of children covered by health insurance / Number of dependents.
- `smoker`: Smoking, yes or no.
- `region`: The beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
- `charges`: Individual medical costs billed by health insurance.

# Personal notes

This project was originally provided to me by Codecademy, as part of the Data Science Foundations course.
While I completed the tasks of this project, I decided to take it a step further and create multiple reports.
The main idea is to expand further from the EDA, into a more statistical analysis of the dataset, and eventually
modeling the data.
