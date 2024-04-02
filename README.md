# ChurnPrediction
it's About Customer Churn Prediction
## Introduction
Customer churn, also known as customer attrition, refers to the phenomenon where customers leave a service or company for various reasons. Predicting customer churn is crucial for businesses as it allows them to take proactive measures to retain customers and improve overall customer satisfaction

## Dataset Overview

The dataset used for this analysis is churn_modelling.csv, containing the following features:

#### CustomerId: A unique identifier assigned to each customer.
#### Surname: Surname of the customer.
#### CreditScore: Credit Score of the customer.
#### Geography: The geographical location or country where the customer resides.
#### Gender: Specifies the gender of the customer (Male or Female).
#### Age: Represents the age of the customer.
#### Tenure: Refers to the number of years the customer has been with the bank or service.
#### Balance: Indicates the account balance of the customer.
#### NumOfProducts: Represents the number of products or services the customer has with the bank.
#### HasCrCard: A binary attribute indicating whether the customer has a credit card (1 for yes, 0 for no).
#### IsActiveMember: A binary attribute indicating whether the customer is an active member of the bank (1 for yes, 0 for no).
#### EstimatedSalary: Represents the estimated salary of the customer.
#### Exited: This attribute indicates whether the customer has churned or exited the bank (1 for churned, 0 for retained).

## Exploratory Data Analysis (EDA)

Histograms displaying the distribution of numerical features among customers who churned and those who didn't.

![Screenshot 2024-04-02 141429](https://github.com/Ravish54/ChurnPrediction/assets/127392207/93793330-444a-413e-93cb-73887d473b56)

Count plots showing categorical features among customers who churned.

![Screenshot 2024-04-02 141559](https://github.com/Ravish54/ChurnPrediction/assets/127392207/ef8233b4-4a62-4048-8e23-b227784bbd63)


Heatmap of correlation between features.

![Screenshot 2024-04-02 141622](https://github.com/Ravish54/ChurnPrediction/assets/127392207/b93e78de-1e40-4a7f-9452-31a7997b90a8)

Count plot showing the usage of credit cards in different countries.

![Screenshot 2024-04-02 141634](https://github.com/Ravish54/ChurnPrediction/assets/127392207/805c804b-4999-46fb-976b-084b9e7dd2d1)

Pie chart displaying the percentage of different age groups for longer-term engagement with the bank.

![Screenshot 2024-04-02 141641](https://github.com/Ravish54/ChurnPrediction/assets/127392207/4a02a065-deda-43d3-a0da-9c881a2582b4)


Bar plot showing the relationship between age groups and churn rate.

![Screenshot 2024-04-02 141648](https://github.com/Ravish54/ChurnPrediction/assets/127392207/2ca7ee42-0e45-4934-844a-8de175498191)




## Data Preprocessing
Handling Null Values

The dataset was checked for null values, and if present, they were dropped from the dataset.

Encoding Categorical Variables

Categorical variables were encoded using one-hot encoding to convert them into numerical format for model training.

Addressing Imbalanced Data

Due to the imbalanced nature of the target variable, SMOTE (Synthetic Minority Over-sampling Technique) was used to generate synthetic samples for the minority class.

## Model Building and Evaluation

Several machine learning models were trained and evaluated using the preprocessed dataset. Models include Logistic Regression, Support Vector Classifier (SVC), K-Nearest Neighbors (KNN), Decision Tree, Random Forest, and Gradient Boosting Classifier.


![Screenshot 2024-04-02 141659](https://github.com/Ravish54/ChurnPrediction/assets/127392207/46aac749-efd5-469e-bb09-1b20f4d9670c)

Model performance metrics such as accuracy, precision, recall, and F1-score were computed for each model.



## Streamlit app


![Screenshot 2024-04-02 072328](https://github.com/Ravish54/ChurnPrediction/assets/127392207/f3b0fee3-32d2-4f97-a343-7dbbab40265e)

![Screenshot 2024-04-02 072427](https://github.com/Ravish54/ChurnPrediction/assets/127392207/73ce7c58-64cd-4ccf-96e2-be43159c7f39)

