import matplotlib.pyplot as plt
from resources import data_preperation as dp
import statsmodels.api as sm
def plot_dataframe(data, columns, size = (15,15), regression = False, results = None):
    
    """
    Inputs: df - DataFrame, x - column name (x-axis), y - column name (y-axis), kind - Type of graph

    Display dataframe graph on a two different column.
    Optional regression input to add regression with a given result. 
    
    Output: Return the ax for plotting
    """
    index = 0
    models = {}
    fig, ax = plt.subplots(len(columns), figsize = size);
    for column in columns:
        data.plot.scatter(column, 'price', ax = ax[index], alpha = .5);
        if regression: 
            
            ax[index].set_title('{} vs {} - R2: {}'.format(column, 'price', round(results[index].rsquared,6)));
            sm.graphics.abline_plot(model_results= results[index] ,label = 'Regression Line', ax = ax[index], c = 'r');
            ax[index].axhline(data['price'].mean(), c = 'black', label = 'Intecept Only' );
            ax[index].legend();
            
        else:
            ax[index].set_title('{} vs {}'.format(column, 'price'));
        index += 1
    return fig, ax


    
    
