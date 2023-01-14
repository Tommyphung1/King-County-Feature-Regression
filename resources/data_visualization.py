import matplotlib.pyplot as plt
from resources import data_preperation as dp
import statsmodels.api as sm
def plot_dataframe(data, x_list, y , size = (15,15), regression = False, results = None):
    
    """
    Inputs: df - DataFrame, x - column name (x-axis), y - column name (y-axis), kind - Type of graph

    Display dataframe graph on a two different column.
    Optional regression input to add regression with a given result. 
    
    Output: Return the ax for plotting
    """
    index = 0
    if len(x_list) == 1:
        fig, ax = plt.subplots();
        data.plot.scatter(x_list[0], y, ax = ax, alpha = .5);
        
    else:
        fig, ax = plt.subplots(len(x_list), figsize = size);
        for column in x_list:
            data.plot.scatter(column, y, ax = ax[index], alpha = .5);
            if regression: 
                ax[index].set_title('{} vs {} - R2: {}'.format(column, y, round(results[index].rsquared,6)));
                sm.graphics.abline_plot(model_results= results[index] ,label = 'Regression Line', ax = ax[index], c = 'r');
                ax[index].axhline(data[y].mean(), c = 'black', label = 'Intecept Only' );
                ax[index].legend();
            else:
                ax[index].set_title('{} vs {}'.format(column, 'price'));
            index += 1
    return fig, ax


    
    
