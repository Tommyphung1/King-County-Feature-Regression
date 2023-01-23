# Phase 2 Project
**Client:** Zillow Group, Inc
**Author**: Tommy Phung

## Overview
Zillow is an online real estate website that help home owners to buy, sell and rent homes. In order to give buyers and sellers a better idea of how much their homes should cost on the market, we will be using the dataset from King Country House Sales. The dataset has multiple potential attributes of a house that would justify a higher house price while others not as influencatial <br>
**Model 1:** The first model was modeling using square feet of living as the only paremeter. <br>
That reuslted in a relationship of a base cost of 260,974 and for every square foot, expected an increase in 355 which accounted for **36.2%** of the variance <br>

**Model 2:** The second model added grade, which was the second highest correlation, along side square feet of living  <br>
The base cost of -626890 for any given house. For every square foot increase the price by 231 while for ever grade increased the price by $150702. The model explains **41.8%** of the variance. <br>

**Model 3:** The third model add the house age which was expected to lower the house price. <br>
The base cost of -1,286,000 for any given house. For every square foot increase the price by 221 while for ever grade increased the price by $216,400. For every year the house increase by 3867 due to age. The model explains **46.4%** of the variance.<br>

**Final Model V1:** The final model has most of the attibutes of a house that proved to be linearly beneficial to price. Interation terms were added as well with grade and square feet of living, the top two correlation to price. The model explains **50.1%** of the variance. <br>

**Final Model V2:** Some of the final model weren't statistically significant and had little to no impact. There were remove for a cleaner interpretation. Since, adding parameter only increases the R squared score, this model explained **49.6%** of the variance. 


## Business Understanding 
Our main variable we are looking at is price and how each independent attributes influnce the price. The other data points such as latitude and longitude will not be considered for this project. A model would be needed to let seller know how much their house can sell for and whether a house is overpriced for the given features. Not all attributes will benefit the price which can let buyers and seller know what make a house valuable or what to improve on. The model should be make sense to intrepet easiler as we can see later that the large amount of parameter make the regression model harder in interpret. 

## Data Understanding
Their are 30155 houses in the dataset with the following columns. The columns are to be seperate initially to prepare them to be added in the final model. SOme columns were changed to become eaiser to read or treated as categories for interpretation.

The following columns and attributed that will be include are: <br>
**Continuous Datatype:** 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_garage', 'sqft_patio' <br>
**Categorical Datatype:** 'bedrooms', 'bathrooms', 'floors', 'waterfront', 'greenbelt', 'nuisance', 'condition', 'view', 'grade', 'heat_source', 'sewer_system' <br>
**Unused Attributes:** 'date', 'id', 'lat', 'long', 'address'<br>

*After exploring the dataset, I decided to remove these attributes for the following reason.* <br>
**sqft_above** - Similar or identical to sqft_living <br>
**nuisance** - Evenly split with relatively little different if a house have a nuisance or doesnt have a nuisance <br>

Due to the fact that buying and selling houses have a lot of attributes, we need to pick the best correlating attributes to make an effective model. We compared means of 'Yes', 'No' columns to see whether there was a big enough difference between the two as well as grouping houses that are the exception so that the models and graphs aren't skewed. 

## Method
We will start with a simple regression model and the intercept-only model and will progressively adding parameter to see if the model improves. Data need to be cleaned and based on the data type needs to be prepped for modeling. Categorical data needs dummy variables inorder to properly model. yr_built was changed to house_age by subtracting to the newest year which was 2022. Interaction terms were added to see if the two parameter were interacting with one anohter and added to the model. Each model is graphed to see if the parital regression shows a positive or negative relationship. 

## Results
### Model 1: 



### Model 2:




### Model 3:





### Final Model V1:




### Final Model V2:






### Conclusion:
The best performing parameters are **square feet of living**, **grade** and **house age**. Depending on the grade, the square feet of living can have a positve or negative effect on price. Other categorical attibutes like whether or not a house in on a waterfront or greenbelt ha shown to have a positive effect on price while others such as square feet of garage has a negative effect. 

The final model shows a strong positve relatioship to price with grade and house age. The model can only explains rouhgly 50% of the variance. Not all paraemter matters and some doesn't have a large enough sample to cosnider. 



