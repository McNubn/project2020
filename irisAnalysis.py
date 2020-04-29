# Brian Doheny
# This program is part of Brian Doheny's Programming and Scripting 2020 module at GMIT.
# This program takes in Fisher's Iris Data Set (iris_csv.csv) and will generate various plots.
# You can find the respective plots in the /plots folder in this repository.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Setting the CSV to be a global variable. This means that the program could be adapted to other files more easily.
csv = 'iris_csv.csv'

# Saving the csv into a Pandas data frame. I'm setting the index to be the type column.
# This is so that I can iterate over the other columns a bit more easily. 
# I'll reset the index later for Seaborn plots, as the type can be used to influence the hue.
df = pd.read_csv(csv, index_col = "type")

# Creating a function to format the column names so that they can be used for titles etc. 
# The first word in each column ends with "l", so I can use that to separate the two words.
def nameFormat(name):
    """ Edits the name of the column so that it is properly formatted with a space between the words, and each word capitalized."""
    space = name.find("l") + 1
    firsthalf = name[:space]
    secondhalf = name[space:]
    name = firsthalf.capitalize() + " " + secondhalf.capitalize()
    return name


# Plotting histograms onto 1 png file.
fig, ax = plt.subplots(2, 2, figsize = (8,8), sharex = True, sharey = True)
# This n will be used to determine which on the figure each plot will be. 
# The 0-4, with 0 being the upper left plot, and 4 the lower right.
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
fig.savefig("plots/histograms/originalHistograms.png")
fig.clf()


# Splitting the dataframe up by Iris type. This allows me to differentiate between them on the plots.
# Picked up this tip from:
# https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
iris_setosa=df.loc["Iris-setosa"]
iris_virginica=df.loc["Iris-virginica"]
iris_versicolor=df.loc["Iris-versicolor"]

# Doing Histograms again, but now with different colours for each iris type. 
# This will let us see the differences between each type and their respective trends.
fig, ax = plt.subplots(2, 2, figsize = (8,8), sharex = True, sharey = True)
n = 0
for measurement in df.columns:
    binsizes = np.arange(0, 8, 0.25)
    ax = ax.flatten()
    # Going to give each iris type its own colour, add an edgecolor to make the boundaries clearer to see.
    # Also used alpha to make them translucent so that we can see overlaps.
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
fig.savefig("plots/histograms/seperatedHistograms.png")
plt.clf()
plt.close()

# Outputting some summary statistics of the dataframe to a text file.
# Using https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html 
# This is providing some data points I can ouput from the columns, e.g. median, mean.
f = open("analysis.txt","w")
f.write ("Summary Statistics for the Iris Data Set\n")
for measurement in df.columns:
    name = nameFormat(measurement)
    f.write("\n" + name + " Summary\n"
        "The median measurement of " + name + " is " + str(df[measurement].median()) + ".\n"
        "The minimum measurement of " + name + " is " + str(df[measurement].min()) + ".\n"
        "The maximum measurement of " + name + " is " + str(df[measurement].max()) + ".\n"
        "The standard deviation of " + name + " is " + str(round(df[measurement].std(), 2)) + ".\n"
        "The mean of " + name + " is " + str(round(df[measurement].mean(),2)) + ".\n")
# Idea to get summary statistics from each iris type:
# https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40
irisgrouped = df.groupby('type').agg(['median','min','max','std','mean'])
f.write("\n Petal Length Summary Statistics by Iris Type\n" + 
        str(irisgrouped['petallength']) + "\n")
f.write("\n Petal Width Summary Statistics by Iris Type\n" + 
        str(irisgrouped['petalwidth']) + "\n")
f.write("\n Sepal Length Summary Statistics by Iris Type\n" + 
        str(irisgrouped['sepallength']) + "\n")
f.write("\n Sepal Width Summary Statistics by Iris Type\n" + 
        str(irisgrouped['sepalwidth']) + "\n")
# I'm also going to plot the Pearson's Correlation Coefficient matrix for each iris type.
f.write("\nPearson Correlation Coefficients\n"
    "Iris Setosa\n" + str(iris_setosa.corr()))
f.write("\n\nIris Veriscolor\n" + str(iris_versicolor.corr()))
f.write("\n\nIris Virginica\n" + str(iris_virginica.corr()))
f.close()

# I will use a While loop to generate the scatter plots. As such I'm definiting Scatter methods that the loop can use.
# This means that at as x and y are changed in the next loop, it'll do a scatter plot of df.columns[x] vs df.columns[y].
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
    fig.savefig('plots/scatterplots/' + xaxis + "Vs" + yaxis + ".png")
    fig.clf()


# Similar to the histograms, the program will now plot each iris type separately with its own corresponding colour.
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
    fig.savefig("plots/scatterplots/separated" + xaxis + "Vs" + yaxis + ".png")
    plt.clf()
    plt.close()

# These three variables are to be used in the While loop. 
# x and/or y will increase after each call of the scatter and scatter2 methods.
x = 0
y = 1
z = len(df.columns)

# You can see the planning for this loop in planning/2columns.txt
# I was getting an error because y was becoming greater than the number of columns. 
# For now I will use a try and except to get past this, as its expected.
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
# Learned about using pass in the except section here: 
# https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
except:
    pass

# I'll now be trying some Seaborn plots. As such I'm making a new dataframe with the index reset. 
# This will let me use the "type" column to determine hue.
# df2 workaround bassed off of: 
# https://stackoverflow.com/questions/49834883/scatter-plot-form-dataframe-with-index-on-x-axis
df2 = df.reset_index()


# Using seaborn documentation to create catplots 
# https://seaborn.pydata.org/tutorial/distributions.html
# This is mostly the sam as the histogram FOR loop from before.
# Key difference is the IF statement to ensure that "type" isn't attempted.
for measurement in df2.columns:
    name = df2[measurement].name
    # The "type" column was causing errors, so this will now only plot if the column is not "type"
    if name != "type":
        measurementname = nameFormat(measurement)
        sns_plot = sns.catplot(x="type", y=measurement, data=df2)
        # Found how to label axes on facetgrids on Seaborn's documentation 
        # https://seaborn.pydata.org/generated/seaborn.FacetGrid.html
        sns_plot.set_axis_labels("Iris Type", measurementname + " (cm)")
        # Title workaround found here: 
        # https://stackoverflow.com/questions/40113860/why-doesnt-set-titles-produced-a-title-seaborn-and-factorplot
        sns_plot.ax.set_title("Catplot of " + measurementname + " for each Iris type")
        sns_plot.savefig('plots/boxViolinCat/' + measurement + "catplot.png")
        plt.clf()
        plt.close()

# Seaborn pairplot shows histograms as well as scatter plots.
# Recreates my first 181 lines of code much more efficiently.
# Will keep in my original plotting as well in order to highlight that I can do it.
sns_plot2 = sns.pairplot(df2, hue = "type")
sns_plot2.savefig("plots/seabornpairplot.png")
plt.clf()
plt.close()

# Seaborn Boxplots to show the range, median and quartiles for each iris type against each measurement type.
# https://seaborn.pydata.org/generated/seaborn.boxplot.html
# FOR loop is mostly the same as the catplots from line 193.
for measurement in df2.columns:
    name = df2[measurement].name
    if name != "type":
        measurementname = nameFormat(measurement)
        fig, ax = plt.subplots()
        sns.boxplot(x = "type", y = measurement, data = df2, ax = ax)
        ax.set_xlabel("Iris Type")
        ax.set_ylabel(measurementname + " (cm)")
        ax.set_title("Boxplot of " + measurementname + " for each Iris type")
        plt.savefig('plots/boxViolinCat/'+ measurement + "boxplot.png")
        plt.clf()
        plt.close()

# Adding Seaborn Violin plot by using their documentation: 
# https://seaborn.pydata.org/generated/seaborn.violinplot.html#seaborn.violinplot
# FOR loop is same as catplots and boxplots.
for measurement in df2.columns:
    name = df2[measurement].name
    measurementname = nameFormat(measurement)
    if name != "type":
        fig, ax = plt.subplots()
        sns.violinplot(x = "type", y = measurement, data = df2, ax = ax)
        ax.set_xlabel("Iris Type")
        ax.set_ylabel(measurementname + " (cm)")
        ax.set_title("Violin Plot of " + measurementname + " for each Iris type")
        plt.savefig('plots/boxViolinCat/'+ measurement + "violinplot.png")
        plt.clf()
        plt.close()

# Heatmap idea from https://levelup.gitconnected.com/pearson-coefficient-of-correlation-using-pandas-ca68ce678c04
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
# As this is a late addition to the program, for now I will create these one by one, rather than tinkering with loops.
fig, ax = plt.subplots(figsize = (8,8))
ax = sns.heatmap(iris_setosa.corr(), annot=True, ax = ax)
# Seems matplotlib introduced an issue for heatmaps whereby half the y axis can get cut off.
# Workaround picked up from : https://stackoverflow.com/questions/56942670/matplotlib-seaborn-first-and-last-row-cut-in-half-of-heatmap-plot 
ax.set_ylim(0, 4)
ax.set_title("Iris Setosa Heat Map showing Pearson's Correlation Coefficient")
plt.savefig("plots/heatmaps/setosaHeatmap.png")
plt.clf()
plt.close()

fig, ax = plt.subplots(figsize = (8,8))
ax = sns.heatmap(iris_virginica.corr(), annot=True, ax = ax)
ax.set_ylim(0, 4)
ax.set_title("Iris Virginica Heat Map showing Pearson's Correlation Coefficient")
plt.savefig("plots/heatmaps/virginicaHeatmap.png")
plt.clf()
plt.close()

fig, ax = plt.subplots(figsize = (8,8))
ax = sns.heatmap(iris_versicolor.corr(), annot=True, ax = ax)
ax.set_ylim(0, 4)
ax.set_title("Iris Versicolor Heat Map showing Pearson's Correlation Coefficient")
plt.savefig("plots/heatmaps/versicolorHeatmap.png")
plt.clf()
plt.close()