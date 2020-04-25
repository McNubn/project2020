# Brian Doheny
# Three main parts:
   # 1. Research the data set online and write a summary about it in the README (using markdown for formatting).
  #  2. Download the data set and add it to the repo. - Done
  #  3. Write a program called analysis.py that:
      #  a. outputs a summary of each file to a single text file - done
      #  b. saves a histogram of each variable to png files, - Done
      #  c. outputs a scatter plot of each pair of variables. - Done

# Minimum Viable Project:
    # Standard repo that contains a README, a Python script, a summary text file and images. 
    # The README should contain a summary of the data set and my investigations into it.
    # It should also clearly document how to run the Python code and what the code does.
    # Remember to referece everything - e.g. where I found a code snippet.

 #Week 4 (ending Sunday April 5th) - MVP achieved & next steps
      #  Achieve the Minimum Viable Project conditions.
     #   Research other analyses of this data set - started
    
 #   Week 5 (ending Sunday April 12th) - Further analyses
    #    Ensure README accounts for this research.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Setting csv to be a global variable, will mean program can be adapted to other files.
csv = 'iris_csv.csv'

# Save the csv to a pandas data frame. I'm setting the index to be the class column.
# This is so that I can iterate over the other columns a bit more easily. 
# I'll reset the index later for Seaborn.
df = pd.read_csv(csv, index_col = "type")

# Creating a function to format the column names so that they can be used for titles etc. 
# First word in each column ends with "l", so I can use that to separate the two words.
def nameFormat(name):
    """ Edits the name of the column so that it is properly formatted with a space between the words, and each word capitalized."""
    space = name.find("l") + 1
    firsthalf = name[:space]
    secondhalf = name[space:]
    name = firsthalf.capitalize() + " " + secondhalf.capitalize()
    return name

fig, ax = plt.subplots(2, 2, figsize = (8,8), sharex = True, sharey = True)
n = 0
# Got the idea to iterate through column names from: 
# https://www.marsja.se/how-to-get-the-column-names-from-a-pandas-dataframe-print-and-list/#3_Get_Column_Names_by_Iterating_of_the_Columns
for measurement in df.columns:
    binsizes = np.arange(0, 8, 0.25)
    # ax.flatten() picked up from:
    # https://stackoverflow.com/questions/37967786/axes-from-plt-subplots-is-a-numpy-ndarray-object-and-has-no-attribute-plot
    ax = ax.flatten()
    ax[n].hist(df[measurement], bins=binsizes, facecolor = 'blue', edgecolor='black')
    name = nameFormat(measurement)
    ax[n].set_xlabel(name + ' (cm)')
    ax[n].set_ylabel ("Frequency")
    ax[n].set_title("Histogram of " + name + " Frequency")
    n += 1
fig.tight_layout()
fig.savefig("plots/originalHistograms.png")
fig.clf()


# Splitting the dataframe up by Iris type. This allows me to differentiate between them on the plots.
# Picked up this tip from:
# https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
iris_setosa=df.loc["Iris-setosa"]
iris_virginica=df.loc["Iris-virginica"]
iris_versicolor=df.loc["Iris-versicolor"]

# Doing Histograms again, but now with different colours for each Iris type. 
# This will let us see the differences between each type and their respective trends.
fig, ax = plt.subplots(2, 2, figsize = (8,8), sharex = True, sharey = True)
n = 0
for measurement in df.columns:
    binsizes = np.arange(0, 8, 0.25)
    ax = ax.flatten()
    # Going to give each flower its own colour, add an edgecolor to make the boundaries clearer to see
    # and used alpha to make them translucent so that we can see overlaps.
    ax[n].hist(iris_setosa[measurement], facecolor='b', edgecolor = 'k', label='Setosa', alpha =0.3, bins=binsizes)
    ax[n].hist(iris_virginica[measurement], facecolor='g', edgecolor = 'k', label = 'Virginica', alpha = 0.3, bins = binsizes)
    ax[n].hist(iris_versicolor[measurement], facecolor='r', edgecolor = 'k', label = 'Versicolor', alpha = 0.3, bins = binsizes)
    name = nameFormat(measurement)
    ax[n].set_xlabel(name + ' (cm)')
    ax[n].set_ylabel ("Frequency")
    ax[n].set_title("Histogram of " + name + " Frequency")
    ax[n].legend()
    n +=1
fig.tight_layout()
fig.savefig("plots/seperatedHistograms.png")
plt.clf()
plt.close()

# Outputting some summary statistics of the dataframe to a text file.
# Using https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html 
# This is providing some data points I can ouput from the columns, e.g. median, mean.
f = open("analysis.txt","w")
f.write ("Data Points Summary\n")
for measurement in df.columns:
    name = nameFormat(measurement)
    f.write("\n" + name + " Summary\n"
        "The median measurement of " + name + " is " + str(df[measurement].median()) + ".\n"
        "The minimum measurement of " + name + " is " + str(df[measurement].min()) + ".\n"
        "The maximum measurement of " + name + " is " + str(df[measurement].max()) + ".\n"
        "The standard deviation of " + name + " is " + str(round(df[measurement].std(), 2)) + ".\n"
        "The mean of " + name + " is " + str(round(df[measurement].mean(),2)) + ".\n")
f.write("\nPearson Correlation Coefficients\n"
    "Iris Setosa\n" + str(iris_setosa.corr()))
f.write("\n\nIris Veriscolor\n" + str(iris_versicolor.corr()))
f.write("\n\nIris Virginica\n" + str(iris_virginica.corr()))
f.close()

#Since my while loop was reusing this code, I've made scatter into a function.
#This means that at as x and y are changed in the next loop, it'll do a scatter plot of df.columns[x] vx df.columns[y].
def scatter(x,y):
    """ Plots the columns x and y onto a scatter plot, while adding text to the axis and title."""
    fig, ax = plt.subplots()
    xaxis = df.columns[x]
    yaxis = df.columns[y]
    ax.scatter(df[xaxis],df[yaxis])
    xaxisName = nameFormat(xaxis)
    yaxisName = nameFormat(yaxis)
    ax.set_xlabel(xaxisName + " (cm)")
    ax.set_ylabel(yaxisName + " (cm)")
    ax.set_title(xaxisName + " Vs " + yaxisName + " (cm)")
    fig.savefig('plots/' + xaxis + "Vs" + yaxis + ".png")
    fig.clf()

def scatter2(x,y):
    """ Like Scatter above, but separate colours for the 3 types of Iris"""
    fig, ax = plt.subplots()
    xaxis = iris_setosa.columns[x]
    yaxis = iris_setosa.columns[y]
    setosa_x = iris_setosa.columns[x]
    setosa_y = iris_setosa.columns[y]
    virginica_x = iris_virginica.columns[x]
    virginica_y = iris_virginica.columns[y]
    versicolor_x = iris_versicolor.columns[x]
    versicolor_y = iris_versicolor.columns[y]
    ax.scatter(iris_setosa[setosa_x],iris_setosa[setosa_y], color='b', label='Setosa', alpha = 0.3)
    ax.scatter(iris_virginica[virginica_x],iris_virginica[virginica_y], color='g', label = 'Virginica', alpha = 0.3)
    ax.scatter(iris_versicolor[versicolor_x],iris_versicolor[versicolor_y], color='r', label = 'Versicolor', alpha = 0.3)
    xaxisName = nameFormat(xaxis)
    yaxisName = nameFormat(yaxis)
    ax.set_xlabel(xaxisName + " (cm)")
    ax.set_ylabel(yaxisName + " (cm)")
    ax.legend()
    ax.set_title(xaxisName + " Vs " + yaxisName + " (cm)")
    fig.savefig("plots/separated" + xaxis + "Vs" + yaxis + ".png")
    plt.clf()
    plt.close()

# I'll now be doing scatter plots with each measurement plotted against each other.
# To do this, I've devised a WHILE loop with IF conditions.
# First I'll need to define three variables for the the above mentioned loop.
x = 0
y = 1
z = len(df.columns)

#I was getting an error because y was becoming greater than the number of columns. 
# For now I will use a try and except to get past this, as its expected.
#Learned about using pass in the except section here: 
# https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
try:
    while x < z:
        if y < z:
            scatter(x,y)
            scatter2(x,y)
            y += 1
        elif y == z:
            x += 1
            y = x + 1
            scatter(x,y)
            scatter2(x,y)
            y += 1
except:
    pass

# I'll now be trying some Seaborn plots.
# I was encountering errors with some of the seaborn plots as I was attempting to plot against the index - "type".
# df2 workaround bassed off of: 
# https://stackoverflow.com/questions/49834883/scatter-plot-form-dataframe-with-index-on-x-axis
df2 = df.reset_index()


# Using seaborn documentation to create catplots 
# https://seaborn.pydata.org/tutorial/distributions.html
for measurement in df2.columns:
    name = df2[measurement].name
    # The "type" column was causing errors, so will only plot if its not "type"
    if name != "type":
        measurementname = nameFormat(measurement)
        sns_plot = sns.catplot(x="type", y=measurement, data=df2)
        # Found how to label axes on facetgrids on Seaborn's documentation 
        # https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
        sns_plot.set_axis_labels("Iris Type", measurementname + " (cm)")
        # Title workaround found here: 
        # https://stackoverflow.com/questions/40113860/why-doesnt-set-titles-produced-a-title-seaborn-and-factorplot
        sns_plot.ax.set_title("Catplot of " + measurementname + " for each Iris type")
        sns_plot.savefig('plots/' + measurement + "catplot.png")
        plt.clf()
        plt.close()

# Seaborn pairplot shows histograms as well as scatter plots.
# Recreates my first 100 or so lines of code much more efficiently.
# Will keep in my original plotting as well in order to highlight that I can do it.
sns_plot2 = sns.pairplot(df2, hue = "type")
sns_plot2.savefig("plots/seabornpairplot.png")
plt.clf()
plt.close()


# Seaborn Boxplots to show the range, median and quartiles for each iris type against each measurement type.
for measurement in df2.columns:
    name = df2[measurement].name
    if name != "type":
        measurementname = nameFormat(measurement)
        fig, ax = plt.subplots()
        sns.boxplot(x = "type", y = measurement, data = df2, ax = ax)
        ax.set_xlabel("Iris Type")
        ax.set_ylabel(measurementname + " (cm)")
        ax.set_title("Boxplot of " + measurementname + " for each Iris type")
        plt.savefig('plots/'+ measurement + "boxplot.png")
        plt.clf()
        plt.close()

# Adding Seaborn Violin plot by using their documentation: 
# https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot
for measurement in df2.columns:
    name = df2[measurement].name
    if name != "type":
        fig, ax = plt.subplots()
        sns.violinplot(x = "type", y = measurement, data = df2, ax = ax)
        ax.set_xlabel("Iris Type")
        ax.set_ylabel(measurementname + " (cm)")
        ax.set_title("Violin Plot of " + measurementname + " for each Iris type")
        plt.savefig('plots/'+ measurement + "violinplot.png")
        plt.clf()
        plt.close()




# Heatmap idea from https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
fig, ax = plt.subplots(figsize = (10,10))
ax = sns.heatmap(iris_setosa.corr(), annot=True, ax = ax)
# Seems matplotlib introduced an issue for heatmaps whereby half the y axis can get cut off.
# Workaround picked up from : https://stackoverflow.com/questions/56942670/matplotlib-seaborn-first-and-last-row-cut-in-half-of-heatmap-plot 
ax.set_ylim(0, 4)
plt.savefig("plots/setosaHeatmap.png")
plt.clf()
plt.close()

fig, ax = plt.subplots(figsize = (10,10))
ax = sns.heatmap(iris_virginica.corr(), annot=True, ax = ax)
ax.set_ylim(0, 4)
plt.savefig("plots/virginicaHeatmap.png")
plt.clf()
plt.close()

fig, ax = plt.subplots(figsize = (10,10))
ax = sns.heatmap(iris_versicolor.corr(), annot=True, ax = ax)
ax.set_ylim(0, 4)
plt.savefig("plots/versicolorHeatmap.png")
plt.clf()
plt.close()