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

My client is Zillow, which help buyers and sellers thorugh their websites to give an overview on what a house would cost and arrange with agents and tours. <br>
Currently, houses are sold with the given information and price that the seller wants to post. There are selling cost posted on the website that anyone could see but doesn't explain why a house increase or decrease in price. Whether or not, that is accurate is determine by the buyer but to give the seller the best chances in selling their house, a model could be used to guage how much the house can be reasonable sold and potenitally how much in the future. Knowing what a house cost will ensure that a seller is never underselling or a buyer overpaying for a house. 

The current housing market are competivive for both buyers and sellers. <br>
For buyers, they would need to know whether a house is actually worth the market asking price. Houses can be inflated based on the loaction and giving buyers more insight whether its worth the price that are being marketed. <br>
For sellers, most are flipping houses to increase in vlaue before putting them back up in the market. Giving the knowledge on what buyers want can give seller the edge in ivnest in part of the house that would give the best price increase. 

Price is argualbly the most important aspect on purchasng a house so we will be looking at how the cost change based on different attributes. A model is created to let Zillow be able to integrate and let buyer and seller what the price should be. Zillow does have an estimate which could be replacing or combined with to make a better model. 

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

### Model 0: Intercept-Only Model
The model is y = 982866 with y being the mean of house prices. Although the model is very simple, it does not take into account anything with the house attributes. There is also a uneven ammount of houses above and below the price average that the model doesn't fit well. <br>
**There is a clear positive relationship that can perform better than intercept only model.** There are some variables that have high correlations that could prove useful. 
### Model 1: 
**The given model states that the starting cost of a house is $260,974 and for every square foot of living space a house has, the price increases by 355.** <br>

Our first model can explain **36.2%** of the variance of price with the parameter, sqft_living. sqft_living is statistically significant having a p-value less than .05. <br>
The single parameter perform well but we will try to see whether a combination of parameter can make the model better. Once the houses gets too expensive or cheaper, the model becomes less accurate. This make sense since the range in price and square feet varies greatly. 

### Model 2:
**The second model states that a price of a house starts with -626,890 and for every every square foot of living increase the price by 231. Alternatively, for every grade a house has, the price is expected to increase by 150,702.** <br>

Our new model now explain **41.8%** of the variance of the price with sqft_living and grade. Both sqft_living and grade are statistically significant with p-values less than .05. <br> 
This model make sense since a house with nothing, living space or grade has no value which is why the constant is negative. Square foot have an effect to the price but not as high as grade. Grade refer back to how the house well the house was built. Grade seems more impactful since they only range from 1-13 and both seems to positvitly effect the price of the house. 

Grade can be broken down to their specific grade and we can see the individual effects of grade.
### Model 3:
**The third model states that a price of a house starts with -1,286,000 and for every every square foot of living increase the price by 221. Alternatively, for every grade a house has, the price is expected to increase by 216,400. The house price also increases by 3867 for the house age.** <br>

Our new model now explain **46.4%** of the variance of the price with sqft_living, grade and house age. All of the parameter are statistically significant with p-values less than .05. <br> 
The house starts with a negative price with each parameter increasing the house price. The main factor of price was grade as they are limited to only 1-13 range. Next would be age, which only continue to increase in value follow by square feet of living. 

When grade is seperated as a category, we can se that only grade 11 and 12 increase the value of the house while the rest only decreases. Surprisingly, grade 13 negatively effect price but that could be due to the limited sample size. Grade 13 are classed as mansions. This model explains **47.6%** which is a 1.2% increase compared to grade being grouped together. 

### Final Model V1:
The 'best' model would include every single parameter of a house and add as many interaction terms as possible. The final model has a low starting value of 1.5 with majoirty of the cost being its grade, in a greenbelt and the view available. Most of the variables has a positive benifit to price while lower grade, condition and view lowered it. Not all parameters are statiscally significant such as the square foot of living, evough it had the best correlation. 

This model could explain **50.1%** of the variance.  To make it a little managable, I only added attributes that appear to have a linear relationship with price and excluded inclonsive data in the next model. 

### Final Model V2:

After removing interaction terms with statiscially insignicant parameters, I gotten a new model that had all of the pararmeter statiscally significant. The base house price increased to 1,355,000 with grade being a huge factor to price. For example, the best performing grade is grade 9 that interacts with square foot of living by 187 per square foot. Compare to the worst performing grade was grade 2 which decreases by -1477 per square foot.

Using this model, we can assume that the house has intrinsic value and loses that value with its correcponding grade since grade was determined when the house was built. This could translate to why house age is still a relavent parameter that increase in value as the house get older, showing that people value an older house verus a new house. This could be due to the fact that most house that are renovated are older houses which is reasonable. However, there wasn't a substantional amount of homes that were renovated. (4.2%)

The grade columns also follows a normal distribution so it stands to reason that higher than 7, the mean, would perform better than the others. When seperated with its respective grades, grade 7, 8, 9 have a positive relationship with square foot of living, meaning that if a house has one of these grades, the bigger the house, the more expensive the house becomes. Inversely, the lower the grade, less than 7, decreases in price with every square foot. Furthermore, the model states that being a grade lower than 7 is expected to lose roughly 1,000,000 in price which balances out the high constant. 

The other categorical parameters that were added and were statiscitcally significant were ones that would make sense to make ahouse more expensive. Such as view, condition and the heat source. View for example was divided between an excellent view, no view and everything inbetween. As expected, excellent view gave a 200,000 increase, follow by 50,000 with some type of view, and -60,000 for no view. This could correlate to the fact that half of all excellent views are also waterfront which had expected 188,000 on average to those that was not. 

### Conclusion:
The best performing parameters are **square feet of living**, **grade** and **house age**. Depending on the grade, the square feet of living can have a positve or negative effect on price. Other categorical attibutes like whether or not a house in on a waterfront or greenbelt ha shown to have a positive effect on price while others such as square feet of garage has a negative effect. 

The final model shows a strong positve relatioship to price with grade and house age. The model can only explains rouhgly 50% of the variance. Not all paraemter matters and some doesn't have a large enough sample to cosnider. 



