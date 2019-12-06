# COMP257 Road crash project

Group: COMP_Pract_06(Fri 4pm)\_Group C
Group Members: Chun Hei Lee, Tahmid Eshayst, Rania Sandhu ,Singyoung Sun
Project Title: What cause fatality in road crash?

We are conducting an analysis on road crash data in South Australia. The data in this analysis is retrieved from [Australia government](https://data.gov.au/dataset/ds-sa-21386a53-56a1-4edf-bd0b-61ed15f10acf/distribution/dist-sa-02fb14f9-8dcb-4a59-863c-5f7cc3ae1832/details?q=)

## Overview

Road crash is one of the most perilous issues that are always neglected and overlooked by Australian society. On 24th June, 2019, a 15-year-old was killed on the scene due to dangerous driving in an Adelaide car accident [ABC News 2019](https://www.abc.net.au/news/2019-06-23/girl-dies-after-being-hit-by-lamborghini-outside-restaurant/11238684?site=southeastsa). According to a traffic statistics in 2019 by [SAPOL](https://www.police.sa.gov.au/about-us/traffic-statistics), there is a record of 100 fatalities with 93 fatal crashes and 622 serious injuries in 2017. This frightening record should concern most Australian and as a result, the project would focus on exploring the cause of fatalities in road crashes.

## Summary

This analysis aims to identify remarkable and significant factors, and determine how these factors contribute to the outcome of being fatal in road crash accident, by generating a best machine learning model in predicting the fatality outcome. This project is sepearted into 5 different phases and each phase would have an individual python notebook. All five notebooks are listed in analysis structure section below. This analysis will only empahasise on the dataset from 2017 to 2018.

## Analysis structure

### 1 Data preprocessing

This is the preprocessing stage of our analysis. Datasets DATA_SA_Units,DATA_SA_Crash and DATA_SA_Casualty were merged using script.py. We removed features with more than 80% missing data, and features irrelevant to our objective in this notebook

### 2 Data cleansing

We cleaned the dataset with using feature engineering techniques, such as renaming columns for better data manipulation; dealing with null values; redefining groups for categories in categorical features based on domain knowledge; deriving new column from existing features, such as splitting times into peak or off-peak groups

### 3 Data visualisation

In this notebook, we visually scrutinised how considered features correlate with the fatality outcomes using summary tables and plotting charts. Observation and discussion for these visual aids were given

### 4 Feature selection

RFE available on sklearn was implemented to produce a ranking list of the considered features, which indicated how these features significantly affected the targeted outcome

### 5 Data analysis

Three distinctive models - logistic, MLP, and Rusboosting classifier were performed. The model with the best performance was selected and used to interpret features having strongest explanatory power on the outcome. Discussion and suggestion for future development were also be provided in this notebook

## Additional resource

### Archived

Contains additional works or resources contributed by group members and contains files that were used in project at earlier stages

### script.py

Python script used in Data preprocessing stage of the project

### datas

A location to store all csv and related files

### metadata.pdf

Metadata of the dataset downloaded from [Australia government](https://data.gov.au/dataset/ds-sa-21386a53-56a1-4edf-bd0b-61ed15f10acf/distribution/dist-sa-02fb14f9-8dcb-4a59-863c-5f7cc3ae1832/details?q=)
