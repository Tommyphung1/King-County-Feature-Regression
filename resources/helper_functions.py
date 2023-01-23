
def plot_dataframe(x, y, hline = False):

    """
    ____________________________________________________________________________________________________
    Input: x (x axis data) - Dataframe or list-like array,
           y (y_axis data) - Dataframe or list-like array
           hline (default: False) - int or float
    ____________________________________________________________________________________________________
    Output: fig, 
            ax 
    ____________________________________________________________________________________________________
    Description: Expect to be given 1 dimensional dataframes and plot against one another in a scatter plot. Can accept a horizontal line to plot alongside the same plot and figure. 
                 If the data are not a Dataframe, generic labels are created in place. Will not except dataframes that have multiple columns. Ticks are evenly divided into 10 ticks and can be hard to interpret
                 
    """
    if not (isinstance(x,pd.DataFrame) & isinstance(y,pd.DataFrame)):
        x_axis = 'Independent Variable'
        y_axis = 'Dependent Variable'
    else :
        x_axis = x.columns[0]
        y_axis =  y.columns[0]
        if (len(x.columns) > 1) | (len(y.columns) > 1):
            print('Invalid Data Inputs: X length = {}, Y length = {}'.format(len(x.columns,len(y.columns))))


    fig, ax = plt.subplots(figsize = (7,5))

    ax.scatter(x, y, alpha = .7, color = 'green');
    ax.set_ylabel(y_axis)
    ax.set_xlabel(x_axis)

    ax.set_title('{} vs {}'.format(x_axis, y_axis))
    y_ticks = np.arange(0,round(y.max()), round(y.max())/10)
    y_ticks_str = ['${:,}'.format(y) for y in y_ticks]
    ax.set_yticks(y_ticks);
    ax.set_yticklabels(y_ticks_str);

    if isinstance(hline, int) | (isinstance(hline, float)) :
        ax.axhline(hline, color = 'red', label = 'Intercept Only: y = {}'.format(round(hline)))
        ax.legend();
        
    return fig, ax



def check_and_drop(dataframe):
    """
    ____________________________________________________________________________________________________
    Input: dataframe (working dataframe) - Dataframe
    ____________________________________________________________________________________________________
    Output: dataframe (new dataframe) - Dataframe
    ____________________________________________________________________________________________________
    Determine whether to remove rows or columns based on the number of missing values in the row or column
    Return the new dateframe and display the action that it took
    """
    print('Number of Missing Values: {}'.format(dataframe.isna().sum().values.sum()))
          
    has_na = [column for column in dataframe.columns if dataframe[column].isna().sum() > 0]
    for column in has_na:    ## Check if missing data or NaN
        if dataframe[column].isna().sum()/len(dataframe) > .5:
            print('Dropping column: {}'.format(column))
            dataframe.drop(column, axis = 1, inplace = True)
        else:
            print('Dropping rows: {}'.format(column))
            dataframe.dropna(subset= column, axis = 0, inplace= True )
    
    num = dataframe.duplicated().sum()
    print('Number of duplicates: {}'.format(num))
    
    if dataframe.duplicated().sum() > 0:    ## Check if their are duplicates
        dataframe.drop_duplicates(inplace = True)
        print('Removed {} duplicates'.format(num - dataframe.duplicated().sum()))
   
    return dataframe

def outliers_remove(dataframe, column):
    """
    ____________________________________________________________________________________________________
    Input: dataframe (working dataframe) - Dataframe,
           column (column's name) - string 
    ____________________________________________________________________________________________________
    Output: dataframe (new dataframe) - Dataframe
    ____________________________________________________________________________________________________
    
    Take a dataframe and return a subset with the outlier removed from the given column name.
    Default to removing 3 standard deviation away as outliers.
    """
    if (isinstance(dataframe,pd.DataFrame)) & (isinstance(column,str)):
        original = len(dataframe)
        new_df = dataframe[abs(dataframe[column]) < dataframe[column].std()*3]
        print('{} observations were removed. '.format(original - len(new_df)))
        return new_df
    else:
        print('Not a valid dataset or string input')
        return None
    
def correlation_with(dataframe, column):
    """
    ____________________________________________________________________________________________________
    Input: dataframe (working dataframe) - Dataframe,
           column (column's name) - string 
    ____________________________________________________________________________________________________      
    Output: best_pairs (Pairs of Correlations - Tuple
    ____________________________________________________________________________________________________
    Return the correlation of a given column with all the columns.
    Make it sorted and readable to decide which column to use. 
    Currently used for positive correlations 
    
    
    """
    df_cc = zip(dataframe.corrwith(dataframe[column]).index,dataframe.corrwith(dataframe[column]).values)
    best_pairs = {x:y for x, y in df_cc if (abs(y) > 0) and (y < 1)}
    best_pairs = sorted(best_pairs.items(), key = lambda x: x[1], reverse = True)
    
    return best_pairs