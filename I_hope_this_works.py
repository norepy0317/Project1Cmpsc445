import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MultiLabelBinarizer, OneHotEncoder
import numpy as np
import re

df = None  # Initialize df outside the try block

try:
    # Attempt to load the CSV
    df = pd.read_csv('/Users/alex/Documents/CMPSC 445/PRoject1/jobs_data_cleaned3.csv')

    # Salary Processing
    def process_salary(salary_str):
        if pd.isnull(salary_str):
            return np.nan
        salary_str = salary_str.replace('$', '').replace(',', '')
        match = re.match(r'(\d+) - (\d+)', salary_str)
        if match:
            lower, upper = int(match.group(1)), int(match.group(2))
            return (lower + upper) / 2
        else:
            return np.nan

    df['Salary_Numeric'] = df['Salary'].apply(process_salary)
    df = df.dropna(subset=['Salary_Numeric'])

    # Skill Encoding
    mlb = MultiLabelBinarizer()
    skills_encoded = pd.DataFrame(mlb.fit_transform(df['Required Skills'].str.split(', ')), columns=mlb.classes_)
    df = pd.concat([df, skills_encoded], axis=1)

    # Categorical Encoding
    categorical_cols = ['Job Title', 'Company', 'Location']
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_cols = pd.DataFrame(encoder.fit_transform(df[categorical_cols]))
    encoded_cols.columns = encoder.get_feature_names_out(categorical_cols)
    df = pd.concat([df, encoded_cols], axis=1)

    # Prepare features and target
    features = pd.concat([skills_encoded, encoded_cols], axis=1)
    target = df['Salary_Numeric']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Linear Regression Model
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    linear_predictions = linear_model.predict(X_test)
    linear_mse = mean_squared_error(y_test, linear_predictions)
    print(f"Linear Regression MSE: {linear_mse}")

    # Random Forest Regression Model
    forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
    forest_model.fit(X_train, y_train)
    forest_predictions = forest_model.predict(X_test)
    forest_mse = mean_squared_error(y_test, forest_predictions)
    print(f"Random Forest Regression MSE: {forest_mse}")

    # Skill Importance (Random Forest)
    feature_importances = forest_model.feature_importances_
    feature_importance_df = pd.DataFrame({'Feature': features.columns, 'Importance': feature_importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)
    print("\nTop Skill Importances (Random Forest):")
    print(feature_importance_df.head(10))

except pd.errors.ParserError as e:
    print(f"Error loading CSV: {e}")
    print("Continuing with available data.")
    if df is None:
        print("No data was loaded. Script will terminate.")
        exit()  # Exit the script if no data was loaded
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()  # Exit the script if file not found
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()  # Exit the script for other unexpected errors
