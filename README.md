# Car-Price-Prediction

This project focuses on predicting car prices using machine learning techniques. The goal is to build a model that can accurately estimate the price of a car based on various features such as make, model, mileage, year of manufacture, and other relevant attributes.

Data Collection and Preprocessing
1. Data Source: We collected our dataset from Kaggle, consisting of car listings with details like make, model, year, mileage, engine size, fuel type, and price.
2. Data Cleaning: We performed data cleaning tasks such as handling missing values, removing duplicates, and correcting inconsistencies in the dataset.
3. Feature Engineering: We created new features like age of the car (current year - year of manufacture) and extracted meaningful information from existing features.

Exploratory Data Analysis (EDA)
1. Statistical Analysis: We conducted statistical analysis to understand the distribution of car prices and identify any outliers.
2. Visualization: Utilizing libraries like matplotlib and seaborn, we created visualizations (histograms, scatter plots, etc.) to explore relationships between features and the target variable (car price).

Model Building
1. Feature Selection: Based on EDA, we selected relevant features for training our model.
2. Model Selection: We experimented with different machine learning algorithms such as Linear Regression, Random Forest, and Gradient Boosting to find the best-performing model for our data.
3. Model Training and Evaluation: We split our dataset into training and testing sets, trained our models on the training data, and evaluated them using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

Deployment
1. Jupyter Notebook: We developed and documented our entire project workflow in a Jupyter Notebook, detailing each step from data preprocessing to model evaluation.
2. GitHub Repository: This project is hosted on GitHub, allowing others to explore our code, reproduce our findings, and contribute to further improvements.

Future Work
1. Hyperparameter Tuning: We plan to optimize our models further by tuning hyperparameters to achieve better performance.
2. Deployment: We aim to deploy our trained model as a web service or integrate it into a car pricing application.
