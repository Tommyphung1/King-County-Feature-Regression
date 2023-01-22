import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_dataframe(x, y, hline = False):

    """
    Input: x (x axis data) - Dataframe or list-like array
           y (y_axis data) - Dataframe or list-like array
           hline (default: False) - int or float
    Output: fig, 
            ax 
    
    Description: Expect to be given 1 dimensional dataframes and plot against one another in a scatter plot. Can accept a horizontal line to plot alongside the same plot and figure. 
                 If the data are not a Dataframe, generic labels are created in place. Will not except dataframes that have multiple columns. Ticks are evenly divided into 10 ticks and can be hard to interpret
                 
    """
    if not (isinstance(x,pd.DataFrame) & isinstance(y,pd.DataFrame)):    ## Check if they are dataframes that has titles for the axises
        x_axis = 'Independent Variable'
        y_axis = 'Dependent Variable'
    else :
        x_axis = x.columns[0]
        y_axis =  y.columns[0]
        if (len(x.columns) > 1) | (len(y.columns) > 1):
            print('Invalid Data Inputs: X length = {}, Y length = {}'.format(len(x.columns,len(y.columns))))


    fig, ax = plt.subplots(figsize = (7,5))    ## Create the plots

    ax.scatter(x, y, alpha = .7, color = 'green');
    ax.set_ylabel(y_axis)
    ax.set_xlabel(x_axis)

    ax.set_title('{} vs {}'.format(x_axis, y_axis))
    y_ticks = np.arange(0,3000000, 250000)
    y_ticks_str = ['${:,}'.format(y) for y in y_ticks]
    ax.set_yticks(y_ticks);
    ax.set_yticklabels(y_ticks_str);

    if isinstance(hline, int) | (isinstance(hline, float)) :    ## If an integer was given, draw a line
        ax.axhline(hline, color = 'red', label = 'Intercept Only: y = {}'.format(round(hline)))
        ax.legend();
        
    return fig, ax