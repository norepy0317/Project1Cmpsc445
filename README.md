# Project1Cmpsc445
Project 1
Project Description

This project aims to develop machine learning models to predict salaries based on job posting data. It also seeks to identify the most important skills for various computer science-related job roles. The project utilizes salary prediction models and feature importance techniques to provide insights into salary trends and skill demands in the job market.


How to Use

Data Preparation:
Ensure you have the required Python libraries installed (pandas, scikit-learn, numpy, matplotlib, seaborn, plotly). You can install them using pip install pandas scikit-learn numpy matplotlib seaborn plotly.
Place the cleaned CSV file (e.g., jobs_data_cleaned.csv) in the same directory as the Python script.
Run the Script: Execute the Python script. It will:
Load the CSV data.
Preprocess the data.
Train the salary prediction models.
Calculate skill importance.
Generate visualizations.
View Results: The script will print the performance metrics of the models (MSE) and the top skill importances. It will also generate and display various visualizations.
Training

Salary Prediction Models: Two models are trained:
Linear Regression
Random Forest Regression
Training Process:
The dataset is split into training and testing sets.
Each model is trained on the training data.
Model performance is evaluated on the test data.
Inferencing

Salary Prediction: The trained models can be used to predict salaries for new job postings by providing the relevant input features (job title, company, location, skills).
Skill Importance: The feature importance scores from the Random Forest model provide insights into the importance of different skills for salary prediction.
Data Collection

Data Sources: From a csv I created to work on preprocessing data and my machine learning code. I could not scrape the data from any job listing sites.
Collected Attributes:
Job Title
Company
Location
Required Skills
Salary
Number of Data Samples: 500
Used Tools

Python
pandas (for data manipulation)
scikit-learn (for machine learning)
numpy (for numerical operations)
matplotlib, seaborn, plotly (for visualization)
Data Preprocessing

Data Cleaning:
Handled missing values (if any).
Processed salary ranges into numerical values (average of the range).
Handled inconsistencies in the "Required Skills" column.
Handled encoding issues.
Handled rows with parsing errors.
Data Integration: The data is assumed to be in a single CSV file.
Data Ingestion: The data is ingested into the Python script using pandas' read_csv function.
Data Description and Metadata Specification

Data Description: The dataset contains information about job postings, including job titles, companies, locations, required skills, and salaries.
Metadata Specification:
File Format: CSV
Delimiter: Comma (,)
Encoding: UTF-8
Columns:
Job Title (Categorical)
Company (Categorical)
Location (Categorical)
Required Skills (Text)
Salary (Text - Salary Range)
Sample Data: (Assuming a simplified example)
Code snippet

Job Title,Company,Location,Required Skills,Salary
Software Engineer,Google,Mountain View,Python, Java, C++,$120,000 - $150,000
Data Scientist,Amazon,Seattle,Python, R, Machine Learning,$110,000 - $140,000
Web Developer,Microsoft,Redmond,HTML, CSS, JavaScript,$90,000 - $120,000
Feature Engineering

How data is processed and prepared for the machine learning model after loading from data repositories:
Salary Processing: The "Salary" column (which is initially a range) is converted into a numerical value by taking the average of the range.
Skill Encoding: The "Required Skills" column, which contains a comma-separated list of skills, is encoded using the MultiLabelBinarizer from scikit-learn. This creates new columns for each skill, with binary values indicating the presence or absence of that skill.
Categorical Encoding: Categorical columns ("Job Title," "Company," and "Location") are encoded using one-hot encoding with OneHotEncoder from scikit-learn. This creates new binary columns for each category within those columns.
Model Development and Evaluation

Train and Test Data Partition:
The dataset is split into training and testing sets using train_test_split from scikit-learn.
A typical split is 80% for training and 20% for testing.
Salary Prediction: Model-1
Machine Learning Model: Linear Regression
Input to Model: Encoded skills and encoded categorical features (job title, company, location).
Size of Train Data: 80% of the total dataset (example).
Attributes to the Machine Learning Model: Encoded skills, encoded job title, encoded company, encoded location.
Performance with Training Data: Performance metrics (e.g., Mean Squared Error) will be calculated on the training data.
Performance with Test Data: Performance metrics (e.g., Mean Squared Error) will be calculated on the test data to evaluate the model's generalization performance.
Salary Prediction: Model-2
Machine Learning Model: Random Forest Regression
Input to Model: Encoded skills and encoded categorical features (job title, company, location).
Size of Train Data: 80% of the total dataset (example).
Attributes to the Machine Learning Model: Encoded skills, encoded job title, encoded company, encoded location.
Performance with Training Data: Performance metrics (e.g., Mean Squared Error) will be calculated on the training data.
Performance with Test Data: Performance metrics (e.g., Mean Squared Error) will be calculated on the test data to evaluate the model's generalization performance.
Skill Importance:
Description of the exploited feature importance techniques to identify the most important skills for different job roles in computer science, data science, and AI:
The Random Forest Regression model provides feature importance scores as a byproduct of the training process. These scores indicate the relative importance of each feature (skill) in predicting salaries.
The feature_importances_ attribute of the trained Random Forest model is used to obtain these scores.
Identified important skills for 5 job roles of your choice: 
Software Engineer: Python, Java, C++, Git, Data Structures
Data Scientist: Python, R, Machine Learning, Statistics, Data Visualization
AI Engineer: Python, Deep Learning, TensorFlow, PyTorch, Natural Language Processing
Web Developer: HTML, CSS, JavaScript, React, Node.js
Cybersecurity Analyst: Network Security, Cryptography, Risk Assessment, Incident Response, Linux
Visualization

Histograms to show the distribution of predicted salaries for different job roles:
Histograms can be used to visualize the distribution of predicted salaries for each job role.
The x-axis would represent the predicted salary ranges, and the y-axis would represent the frequency of predictions within each range.
Box plots to compare the salary distributions across different job roles and locations:
Box plots can be used to compare the salary distributions across different job roles and locations.
Each box plot would represent the median, quartiles, and outliers of the salary distribution for a specific job role or location.
A map to visualize the average predicted salaries across different locations:
A map (e.g., using Plotly) can be used to visualize the average predicted salaries across different geographical locations.
The map would use color intensity or markers to represent the average salary for each location.
Bar plots to show the importance of different skills for each job role:
Bar plots can be used to show the importance of different skills for each job role.
The x-axis would represent the skills, and the y-axis would represent the feature importance scores from the Random Forest model.
Heatmaps to visualize the importance of skills across different job roles:
Heatmaps can be used to visualize the importance of skills across different job roles.
The x-axis and y-axis would represent the skills and job roles, respectively, and the color intensity would represent the feature importance scores.
Discussion and Conclusions

Project findings, including insights gained from data analysis: The project's findings will include insights into salary prediction accuracy, the most important skills for different job roles, and salary distribution patterns across job roles and locations.
Challenges encountered during model development:
Data cleaning and preprocessing were challenging due to inconsistencies in the data.
Handling categorical features and high dimensionality was a consideration.
Model performance might vary based on the quality and quantity of data.
Recommendations for improving the performance of the model:
Gather more data to improve model accuracy and generalization.
Explore more advanced feature engineering techniques.
Experiment with different machine learning models and hyperparameter tuning.
Address data inconsistencies more thoroughly during cleaning.
