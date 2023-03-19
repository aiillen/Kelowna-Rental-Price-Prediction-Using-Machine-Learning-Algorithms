 # Kelowna-Rental-Price-Prediction-Using-Machine-Learning-Algorithms

## Introduction

The goal of this project is to build a machine learning model that can accurately predict the price of properties in city of Kelowna in a given location. The motivation behind this project was to help students and young professionals who often struggle to estimate the real value of a property when searching for accommodation. By leveraging the power of data and machine learning, I hope to provide a more objective and accurate estimation of property prices, thus empowering users in price negotiations and facilitating informed decision-making. Additionally, this project is also useful for people who want to publish their properties on different sites for the first time. By using this model to predict the best price for their property, they can save time and effort in researching the current market price of their property.



## Data Collection

To build the predictive model, I collected data from Facebook Marketplace using web scraping techniques. I extracted information about various property features such as number of bedrooms and bathrooms, property type, location, amenities, and more. In addition to the Facebook Marketplace data, I also used the Walk Score API to obtain information about the walk score, bike score, and transit score of each property based on its coordinates.

## Data Cleaning and Exploration

After collecting the data, I performed extensive cleaning and preprocessing to ensure its quality and consistency. I removed duplicates, handled missing values, and applied various transformations to the data to make it suitable for analysis and modeling. I then performed exploratory data analysis (EDA) to gain insights about the data distribution, correlations between features, and potential outliers.

## Modeling

I utilized several machine learning algorithms in building the predictive model, such as linear regression, random forest, and gradient boosting. To evaluate the performance of each model, I employed various metrics such as mean squared error (MSE), R-squared, and cross-validation. In addition, I carried out feature selection and engineering to identify the most important predictors and improve the model's performance.

After comparing all the models, XGBoost displayed the best performance, so I selected it as the final model.

## Conclusion

Overall, this project demonstrates the power of data and machine learning in predicting real estate prices. By leveraging web scraping techniques and the Walk Score API, I was able to collect and preprocess a large amount of data and build an accurate predictive model. This project can be used as a tool to help students and young professionals estimate the real value of a property and make informed decisions about their housing choices.

## Web app
After selecting XGBoost as the final model, I proceeded to build a web application using Streamlit. The app provides a user-friendly interface that enables users to input the required data and obtain the predicted output. To ensure the model's accessibility, I deployed it on a cloud platform and generated a link that can be accessed by anyone.

https://aiillen-kelowna-rental-price-prediction--notebookswebapp-uhrqjs.streamlit.app/





