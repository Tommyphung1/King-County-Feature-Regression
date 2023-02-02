# Phase 2 Project
**Client:** Zillow Group, Inc
**Author**: Tommy Phung

## Overview
[**Zillow**](https://www.zillow.com/) is an online real estate website that helps homeowners to buy, sell and rent homes.  The dataset from King Country House Sales was used to model the effect on price.  The dataset has multiple potential attributes of a house that would justify a higher house price while others are not as influential. <br>

**Model 1:** The first model was modeled using square feet of living as the only parameter. <br>
That resulted in a relationship of a base cost of **260,974** and for every square foot, expected an increase in **355** which accounted for **36.2%** of the variance. <br>

**Model 2:** The second model added grade, which was the second highest correlation, alongside square feet of living.  <br>
The base cost of **-626,890** for any given house. For every square foot increase the price by **231** while for every grade increased the price by **150702**. The model explains **41.8%** of the variance. <br>

**Model 3:** The third model adds the house age which was expected to lower the house price. <br>
The base cost of **-1,286,000** for any given house. For every square foot increase the price by **221** while for every grade increased the price by **216,400**. For every year the house increase by 3867 due to age. The model explains **46.4%** of the variance.<br>

**Final Model V1:** The final model has most of the attributes of a house that proved to be linearly beneficial to price. Interaction terms were added as well with grade and square feet of living, the top two correlations to price. The model explains **50.1%** of the variance. <br>

**Final Model V2:** Some of the final models weren't statistically significant and had little to no impact. There were removed for a cleaner interpretation. Since, adding a parameter only increases the R squared score, this model explained **49.6%** of the variance. Keeping relevant parameter enable users to read the model better. 

## Business Understanding
My client is **Zillow**, which helps buyers and sellers through their website with a list of all the available houses in a given area. A user can select preferences on houses to filter out there the desired house.  <br>

Currently, houses are sold with the given information and priced based on the user's input. There are two ways to determine the price of a house on the website. First, there are past selling prices of the house which are publicly displayed to see. Second, Zillow has what is called Zestimate to give the user an idea of how the market price of the house.  The former doesn't take into consideration anything that the current home buyer could infer. To improve their system, models should be given and integrated if prove useful. 

For **buyers**, it is particularly useful to determine if the house is reasonably priced before purchasing. Knowing what attributes increase or decrease a house's price may influence whether or not a desired detail is worth the price for it.  <br>

For **sellers**, knowing what is desirable and the cost for it may allow the seller to change them if possible. For example, if the number of bedrooms increases the house price enough, the seller may invest in making more or less depending on the model. 

Price is arguably the most important aspect of purchasing a house so we will be looking at how the cost change based on different attributes. A model is created to let Zillow be able to integrate and let buyers and sellers what the price should be. Zillow does have an estimate which could be replaced or combined to make a better model. 

## Data Understanding
The dataset that is being used is from [Kong County](https://kingcounty.gov/) <br>

There are **30155** houses listed in the dataset with **25** different columns. Although there are a lot of attributes in a house, not all of them influence the house price. By plotting and modeling the different variables, we can see which attributes are important and which to ignore. This data spans to as late 1900 so there is a substantial amount of data from the years that can give a rough idea of the housing market in the area. <br>

Using dummy variables, we can model the continuous variables with the categorical variables to determine which combination of parameters is useful in predicting the house price. <br>

Although we would like to use all of the available data, that is simpling not easy to model so some variables are excluded. Some variables such as ID, address, latitude, and longitude are excluded since they should have any influence on price. The following were the columns in the dataset to consider and the ones that were removed. 

**Continuous Datatype:** <br>
'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'sqft_garage', 'sqft_patio' <br>
**Categorical Datatype:** <br>
'bedrooms', 'bathrooms', 'floors', 'waterfront', 'greenbelt', 'nuisance', 'condition', 'view', 'grade', 'heat_source', 'sewer_system' <br>
**Unused Attributes:** <br>
'date', 'id', 'lat', 'long', 'address'<br>

*After exploring the dataset, I decided to remove these attributes for the following reason.* <br>
**sqft_above** - Similar or identical to sqft_living <br>
**nuisance** - Evenly split with relatively little difference if a house has a nuisance or doesn't have a nuisance <br>

## Method
We will start with a simple regression model and the intercept-only model and will progressively adding parameter to see if the model improves. Data need to be cleaned and based on the data type needs to be prepped for modeling. Categorical data needs dummy variables inorder to properly model. yr_built was changed to house_age by subtracting to the newest year which was 2022. Interaction terms were added to see if the two parameter were interacting with one anohter and added to the model. Each model is graphed to see if the parital regression shows a positive or negative relationship. 

## Results

### Model 0: Intercept-Only Model
![Intercept_Only Model](https://github.com/Tommyphung1/Project-2/blob/afdfdebeca1a409088c409d2b35b210a1a417f30/pictures/Baseline%20model%20Int%20Only.JPG)) <br>

The model is **y = 982866** with y being the mean of house prices. Although the model is very simple, it does not take into account anything with the house attributes. There is also an uneven amount of houses above and below the price average that the model doesn't fit well. <br>

**There is a clear positive relationship that can perform better than the intercept-only model.** Some variables have high correlations that could prove useful. 

### Model 1: 
![Intercept_Only Model](https://github.com/Tommyphung1/Project-2/blob/afdfdebeca1a409088c409d2b35b210a1a417f30/pictures/First%20Model%20Graph.JPG) <br>

**The given states that the starting cost of a house is 260,974 and for every square foot of living space a house has, the price increases by 356.** <br>

Our first model can explain **36.2%** of the variance of price with the parameter, sqft_living. sqft_living is statistically significant having a p-value less than .05. <br>
The single parameter performs well but we will try to see whether a combination of parameters can make the model better. Once the houses get too expensive or cheaper, the model becomes less accurate. This makes sense since the range in price and square feet varies greatly. 

**Recommendation:** Since this model only has one parameter, the larger the square foot is, the more the house increases. 

### Model 2:
![Square Living Model](https://github.com/Tommyphung1/Project-2/blob/afdfdebeca1a409088c409d2b35b210a1a417f30/pictures/Mode%202%20Regression%20QQPlot.JPG) <br>
**The new model states that a price of a house starts at **-626,900** and for every square foot of living increase the price by **231.** Alternatively, for every grade a house has, the price is expected to increase by 150,700.** <br>

Our new model now explains **41.8%** of the variance of the price with sqft_living and grade. Both sqft_living and grade are statistically significant with p-values less than .05. <br> 
This model makes sense since a house with nothing, living space or grade has no value which is why the constant is negative. Square feet affect the price but are not as high as the grade. Grade refers back to how the house well the house was built. The grade seems more impactful since they only range from 1-13 and both seem to positively affect the price of the house. 

**Recommendation:** The square foot of a house is still impactful so the bigger the house, the more expensive a house is predicted to become. The grade is a little harder to change since that is determined during the construction of the house itself. Since it is harder to change and has a fixed amount of grade, it has a large effect on price. Assuming that a house average is 7, the house cost balances out with the initial cost. 

Grades can be broken down into their specific grade and we can see the individual effects of grades.
### Model 3:
![House Age Model](https://github.com/Tommyphung1/Project-2/blob/afdfdebeca1a409088c409d2b35b210a1a417f30/pictures/House%20Age%20Model%203.JPG) <br>
**The third model states that a price of a house starts at -1,286,000 and for every square foot of living increase the price by 221. Alternatively, for every grade a house has, the price is expected to increase by 216,400. The house price also increases by 3867 for the house age.** <br>

Our new model now explains **46.4%** of the variance of the price with sqft_living, grade, and house age. All of the parameters are statistically significant with p-values less than .05. <br> 
The house starts with a negative price with each parameter increasing the house price. The main factor of price was grade which range from 1-13. Next would be age, which only continues to increase in value followed by square feet of living. 

**Recommendation:** When using this model, the large negative constant need to be balanced by the grade as the model 2. Square foot of living is still a positive parameter so that remains true. The extra parameter of house age tells us that older houses are expected to increase in price. This could be due to inflation in price as well as how house prices trend to increase rather than decrease when other factors are not considered. From these models, all of their parameters don't change except for age which sellers have no control over. The seller can infer that if nothing changes with the house, the price increase 3866 a year. Although the value can add up the older the house becomes, it is not nearly high enough when prices are in the hundreds of thousands. 

### Final Model V1:
![Final Model](https://github.com/Tommyphung1/Project-2/blob/afdfdebeca1a409088c409d2b35b210a1a417f30/pictures/Final%20Model%20Regressin%20Plots.JPG) <br>
The 'best' model would include every single parameter of a house and add as many interaction terms as possible. The final model has a low starting value of 1.5 with the majority of the cost being its grade, in a greenbelt, and the view available. Most of the variables have a positive benefit to price while lower grade, condition, and view lowered it. Not all parameters are statistically significant such as the square foot of living, enough that it had the best correlation. 

This model could explain **50.1%** of the variance.  To make it a little manageable, I only added attributes that appear to have a linear relationship with price and excluded inconclusive data in the next model. 

### Final Model V2:

After removing interaction terms with statistically insignificant parameters, I created a new model that had all of the parameters statistically significant. The base house price increased to 1,355,000 with the grade being a huge factor in price. For example, the best-performing grade is grade 9 which interacts with a square foot of living by 187 per square foot. Compare to the worst performing grade was grade 2 which decreases by -1477 per square foot.

Using this model, we can assume that the house has intrinsic value and loses that value with its corresponding grade since the grade was determined when the house was built. This could translate to why house age is still a relevant parameter that increases in value as the house gets older, showing that people value an older house versus a new house. This could be because most houses that are renovated are older houses which is reasonable. However, there wasn't a substantial amount of homes that were renovated. (4.2%)

The grade columns also follow a normal distribution so it stands to reason that higher than 7, the mean, would perform better than the others. When separated by their respective grades, grades 7, 8, and 9 have a positive relationship with a square foot of living, meaning that if a house has one of these grades, the bigger the house, the more expensive the house becomes. Inversely, the lower the grade, less than 7, decreases in price with every square foot. Furthermore, the model states that being a grade lower than 7 is expected to lose roughly 1,000,000 in price which balances out the high constant. 

The other categorical parameters that were added and were statistically significant were ones that would make sense to make a house more expensive. Such as view, condition, and heat source. View for example was divided between an excellent view, no view, and everything in between. As expected, excellent view gave a 200,000 increase, followed by **50,000** with some type of view, and **-60,000** for no view. This could correlate to the fact that half of all excellent views are also waterfront which had expected **188,000** on average to those that were not. 

## Conclusion:
The best-performing parameters are **square feet of living**, **grade** and **house age**. Depending on the grade, the square feet of living can have a positive or negative effect on price. Other categorical attributes like whether or not a house is on a waterfront or greenbelt have shown to have a positive effect on price while others such as **square feet of the garage have a negative effect.** 

**The final model shows a strong positive relationship between price with grade and house age.** The model can only explain roughly **50%** of the variance. Not all parameters matters and some don't have a large enough sample to consider. Based on the reference we used, anything lower or worst than the reference was more likely to give a negative effect on price. 

When considering parameters to add, **not all of them are significant to add in the model**. <br>
Some will have no effects while others need interaction terms to see if they are significant or not. Adding many parameters will make the model *accurate* but could be misleading as R-square will always increase the parameters added. A balance of parameters with linear relationships and categories can lead to an even better model. 

To make a model read easier, **a model should have a negatively linear relationship with the dependent variables.** <br>
Without them, the constant would be negative which in this case would make sense if the model started with a positive value. A positive constant for these models can be inferred as the price of the land itself which doesn't necessarily have the attributes yet. 

**Square foot of living correlates with the grade that benefited the model.** <br>
Finding correlating parameters can lead to an accurate model and should be added if possible.  

## Next Steps
+ **More Interaction Terms** <br>
The model only has interaction terms with a square foot of living and grade since they were the most correlating parameters to price. There could be other useful interaction terms to be added but wouldn't be obvious to add. 
+ **Added more outside interactions** <br>
Based on the categorical datatypes, the outside environment has a strong effect on the house price. Adding more of these attributes could lead to more linear relationships that could benefit the model. These could be hard to track as the houses span through many years and the environment changes often. 
+ **Current Economic Status** <br>
For the past 3 years, we lived through a pandemic and that could affect house prices. There have been other events that could prove useful to know. Knowing the value of the dollar or inflation rate during the time could give more insight into how buyers and seller value their money.

## For More Information

Please review our full analysis in [Jupyter Notebook](./house_notebook.ipynb) or the [presentation](./presentation_2.pdf).

For any additional questions, please contact **Tommy Phung, phungtommy109@gmail.com**

## Repository Structure

```                  
├── README.md                           <- The top-level README for reviewers of this project
├── house_notebook.ipynb                <- Narrative documentation of analysis in Jupyter notebook
├── presentation_2.pdf                    <- PDF version of project presentation
├── resources
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── helper_functions_v2.py          <- .py script of all the functions used for the notebook
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── pictures                            <- Graphs and plots created by code
└── data                                <- Original dataset from Website
```
