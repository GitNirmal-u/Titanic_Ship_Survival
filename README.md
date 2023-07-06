# Titanic_Ship_Survival

This repository contains a machine learning project on the Titanic dataset. The goal of this project is to predict the survival of passengers aboard the Titanic based on various features such as age, sex, passenger class, etc.

# Data Set:
The Titanic dataset used in this project provides information about the passengers on board the Titanic, including whether they survived or not. It consists of the following columns:

1) Survived: Survival status (0 = No, 1 = Yes)
2) Pclass: Passenger class (1 = 1st class, 2 = 2nd class, 3 = 3rd class)
3) Sex: Gender of the passenger
4) Age: Age of the passenger
5) Fare: Ticket fare
6) Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
7) sibsp - means weather Siblings / Spouse on board
8) parch - means weather Children / Parents on board
9) cabin - means Cabin Number

# Project Overview

The project follows these main steps:

1) Loading the dataset: The Titanic dataset is loaded into the project using pandas library to analyze and manipulate the data.
2) Data cleaning: The dataset is cleaned by handling missing values, removing irrelevant columns, and performing any necessary data transformations.
3) Exploratory Data Analysis (EDA): Exploratory analysis is performed to gain insights into the dataset. Visualizations and statistical summaries are used to understand the relationships between different features and the target variable (Survived).
4) Data preprocessing: The dataset is prepared for model training by encoding categorical variables, scaling numerical features if required, and splitting the data into training and testing sets.
5) Model selection: Various classification algorithms are evaluated on the dataset to determine the best model for predicting survival. The model with the highest performance is selected.
6) Handling imbalanced data: As the dataset may be imbalanced, techniques such as oversampling or undersampling are applied to balance the classes and improve model performance.Here Over sampling technique is used.
7) Hyperparameter tuning: The selected model is fine-tuned by performing hyperparameter tuning using techniques like Randomized Search CV to find the optimal combination of hyperparameters.
8) Model evaluation: The performance of the tuned model is evaluated using suitable metrics such as accuracy, precision, recall, and F1 score. The model's performance is also assessed using appropriate visualization techniques.

# Results
In this project we had a test data to predict the survival after building our machine learning model. 
There were total 275 passengers in test data out of which 148 passengers survived ie 53.8% and 127 passengers deceased ie 46.2%.
