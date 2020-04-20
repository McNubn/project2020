import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Setting csv to be a global variable, will mean program can be adapted to other files.
csv = 'iris_csv.csv'

# Save the csv to a pandas data frame. I'm setting the index to be the class column.
df = pd.read_csv(csv, index_col = "type")

# Got the idea to iterate through column names from https://www.marsja.se/how-to-get-the-column-names-from-a-pandas-dataframe-print-and-list/#3_Get_Column_Names_by_Iterating_of_the_Columns
# Column names without the space looks odd. Figure if I can get past the "l" in Sepal and Petal, and split it into 2 strings with a space in the middle, it'll look neater.
# Since I'll need this again later, I'm turning it into a function called nameFormat.

def nameFormat(name):
    """ Edits the name of the column so that it is properly formatted with a space between the words, and each word capitalized."""
    space = name.find("l") + 1
    firsthalf = name[:space]
    secondhalf = name[space:]
    name = firsthalf.capitalize() + " " + secondhalf.capitalize()
    return name

fig, ax = plt.subplots(2, 2, figsize = (8,8), sharex = True, sharey = True)
n = 0
for measurement in df.columns:
    upper = df[measurement].max()
    binsizes = np.arange(0, 8, 0.25)
    ax = ax.flatten()
    ax[n].hist(df[measurement], bins=binsizes, facecolor = 'blue', edgecolor='black')
    name = nameFormat(measurement)
    ax[n].set_xlabel(name + ' (cm)')
    ax[n].set_ylabel ("Frequency")
    ax[n].set_title("Histogram of " + name + " Frequency")
    n += 1
fig.tight_layout()
fig.savefig(measurement +"Hist.png")
fig.clf()