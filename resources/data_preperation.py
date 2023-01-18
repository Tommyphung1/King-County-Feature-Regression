import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy

def format_df_columns(serie, _format):
    """
    Input: DateFrame Serie (column)
    
    Format the column to a given format,
    Current working formats int, str
    
    Output: DateFrame Serie (column)
    
    """
    
    None
    
def check_and_drop(dataframe):
    """
    Input: DataFrame
    
    Determine whether to remove rows or columns based on the number of missing values in the row or column
    Return the new dateframe and display the action that it took
    
    Output: DataFrame
    """
    print('Number of Missing Values: {}'.format(dataframe.isna().sum().values.sum()))
          
    has_na = [column for column in dataframe.columns if dataframe[column].isna().sum() > 0]
    for column in has_na:
        if dataframe[column].isna().sum()/len(dataframe) > .5:
            print('Dropping column: {}'.format(column))
            dataframe.drop(column, axis = 1, inplace = True)
        else:
            print('Dropping rows: {}'.format(column))
            dataframe.dropna(subset= column, axis = 0, inplace= True )
    
    print('Number of Missing Values: {}'.format(dataframe.isna().sum().values.sum()))
    
    num = dataframe.duplicated().sum()
    print('Number of duplicates: {}'.format(num))
    
    if dataframe.duplicated().sum() > 0:
        dataframe.drop_duplicates(inplace = True)
        print('Removed {} duplicates'.format(num - dataframe.duplicated().sum()))
        print('Number of duplicates: {}'.format(dataframe.duplicated().sum()))
    return dataframe
    
def correlation_with(dataframe, column):
    """
    Input: DataFrame, column name
    
    Return the correlation of a given column with all the columns.
    Make it sorted and readable to decide which column to use. 
    Currently used for positive correlations 
    
    Output: Dict
    """
    df_cc = zip(dataframe.corrwith(dataframe[column]).index,dataframe.corrwith(dataframe[column]).values)
    best_pairs = {x:y for x, y in df_cc if (y > 0) and (y < 1)}
    best_pairs = sorted(best_pairs.items(), key = lambda x: x[1], reverse = True)
    
    return best_pairs

def create_model(dataframe, x_list, y):
    """
    Input: Dataframe, list of independent variables (x_list) , dependent (y)
    
    Create a model from the dataframe with the given variable names only and return the model and the results
    
    Output: Model, Results
    """
    
    X = dataframe[x_list]
    y = dataframe[y]
    model = sm.OLS(y, sm.add_constant(X))
    results = model.fit()

    return model, results

def seperate_dataframe(dataframe):
    """
    Input: dataframe
    
    Take a dataframe and seperate them with numeric data types and object data types
    
    Output: Two Dataframe subsets
    """
    df_numeric = dataframe.select_dtypes('number')
    df_categories = dataframe.select_dtypes('object')
    
    return df_numeric, df_categories

def outliers_remove(dataframe, column):
    """
    Input: Dataframe, column's name (column)
    
    Take a dataframe and return a subset with the outlier removed from the given column name.
    Default to removing 3 standard deviation away as outliers.
    
    Output: Dataframe
    """
    original = len(dataframe)
    new_df = dataframe[abs(dataframe[column]) < dataframe[column].std()*3]
    print('{} observations were removed. '.format(original - len(new_df)))
    return new_df