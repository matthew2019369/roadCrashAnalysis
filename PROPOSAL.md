## COMP257 Project Proposal
# STATISTICAL ANALYSIS OF ROAD ACCIDENT IN SOUTH AUSTRALIA

### "What cause fatality in road crash?"

### Summary 

Road crash is one of the most perilous issues that are always neglected and overlooked by Australian society. On 24th June, 2019, a 15-year-old was killed on the scene due to dangerous driving in an Adelaide car accident [ABC News 2019](https://www.abc.net.au/news/2019-06-23/girl-dies-after-being-hit-by-lamborghini-outside-restaurant/11238684?site=southeastsa).  According to a traffic statistics in 2019 by [SAPOL](https://www.police.sa.gov.au/about-us/traffic-statistics), there is a record of 100 fatalities with 93 fatal crashes and 622 serious injuries in 2017. This frightening record should concern most Australian and as a result, the project would focus on exploring the cause of fatalities in road crashes


## Goal 

1. Identify remarkable and significant factors, and determine how these factors contribute to the outcome of being fatal in road crash accident

2. Generate a best machine learning model in predicting fatality outcome
    
## Aim

To identify remarkable and significant factors, and determine how these factors contribute to the number of fatalities in road crash accident.
    
## Data Source and Background Information
    
The road crash data is obtained from [Department of Planning, Transport and Infrastructure serving in South Australia](https://data.gov.au/dataset/ds-sa-21386a53-56a1-4edf-bd0b-61ed15f10acf/details?fbclid=IwAR1-An_AH7-u18Q8domYoQq6EEpktu2PrHxpSoMnJTirWOuAC2JFbydEk3U). The datasets used in this project are comprised of 3 different types of csv files and they are: 
     
*  Crash Type records location description for each individual incidence such as number of car units involved in the accident, description of the crash environment, number of fatalities etc.
* Unit contains information of car unit involved in road crash as such number of causalties, gender, age etc.
* Causality contains causalty report for each accident incidence recorded such as casualty type, position of driver/passengers in the vehicle etc.

## Formats
    
 All data are stored in csv files. The dimension of each file is summarised in the table below.
 
|Year |Crash Type (row x column)|Unit (row x column)|Causality (row x column)|
|-----|-------------------------|-------------------|------------------------|
|2017 |        13237 x 31       |     28163 x 16    |       6237 x 12        |
|2018 |        13599 x 31       |     29033 x 16    |       6124 x 12        |

## Preliminary Exploration of The Data

 - Report ID is the common column in all CSV files, and it would be used to join the files into a large dataset.
 - Duplicated columns such as number of casualty in the dataset would be dropped. 


## Techniques used within the project

   Throughout the entire project, we will be using several machine learning models such as logistic regression, random forest, support vector machine, neuron network, in order to select the best model in explaining the fatality factor.  
  1.  **Data merging** - use the most appropriate joining method (inner/left/right joins) to merge the separate csv files into a large dataset for machine learning analysis.

  2. **Data cleansing**- detect and remove corrupted values in the datasets. Methods used for this purpose include: 
        - generate a report for null value proportion and remove features that contain large portion of missing values
        - imputation for missing continuous values

        - Ensuring that values in each categorical feature are uniform. Eg: “Yes” and “y” both represent option of yes, and only one form is allowed. 
  3. **Data exploration**
        - Detect outliers using boxplots
        - Encode categorical features using one hot encoding package if necessary
        - Detect multicollinearity among continuous features using scatter matrix and correlation matrix using seaborn packages 
        - Identify any grouping effects on number of fatalities
        - Cluster the mixed data using unsupervised learning method -K prototype, and examine if the data can be categorised into clusters. 
    
  4. **Regression model**  - several regression or classification algorithms could be applied to select the most significant features contributing to the cause of fatality factor. Models include logistic regression, random forest, support vector machine, neural network, and only the best one model would be selected to predict fatality factor. 
    
        - Some advanced machine learning models require tuning the best combination of hyperparameters in order to produce the best performance. Grid Search can be used to achieve this purpose. 
        - Recursive feature elimination can be implemented to explore the most significant features in contributing the explanatory power of the model.
    
## Project Plan
 
**Milestone #1** : Project Base -Semester break

 - Establish the base of the project, which includes Github source control,downloading and merging the datasets, and creating accounts on project management platform (Trello) for project communication.

**Milestone #2**: Data exploration Week 8

 - Analyse the dataset by generating visual plots, and identify possible association between features. 

**Milestone #3**: Model selection Week 9-11

 - Model the dataset using several machine learning algorithms, and select the best two models. 

**Milestone #4**: Model selection Week 12-13.

 - Prepare presentation in week 13.
