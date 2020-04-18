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
      #  Consider other methods of plotting or analysing this data set - started
      #  Consider other libraries that might help here - done
    
 #   Week 5 (ending Sunday April 12th) - Further analyses
    #    Utilise research from week 3 in new plots - started
    #    Ensure README accounts for this research.
    #    Ensure commenting in the files is descriptive and accurate.

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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

for measurement in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df[measurement], bins=30, facecolor = 'blue', edgecolor='black')
    name = nameFormat(measurement)
    ax.set_xlabel(name + ' (cm)')
    ax.set_ylabel ("Frequency")
    ax.set_title("Histogram of " + name + " Frequency")
    fig.savefig(measurement +"Hist.png")
    fig.clf()

x = 0
y = 1
z = len(df.columns)

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
f.close()

# Since my while loop was reusing this code, I've made scatter into a function.
#def scatter(x,y):
 #   """ Plots the columns x and y onto a scatter plot, while adding text to the axis and title."""
  #  fig, ax = plt.subplots()
   # xaxis = df.columns[x]
    #yaxis = df.columns[y]
    #ax.scatter(df[xaxis],df[yaxis])
  #  xaxisName = nameFormat(xaxis)
 #   yaxisName = nameFormat(yaxis)
 #   ax.set_xlabel(xaxisName + " (cm)")
  #  ax.set_ylabel(yaxisName + " (cm)")
 #   ax.set_title(xaxisName + " Vs " + yaxisName + " (cm)")
  #  fig.savefig(xaxis + "Vs" + yaxis + ".png")
  #  fig.clf()

# I was getting an error because y was becoming greater than the number of columns. For now I will use a try and except to get past this, as its expected.
# Learned about using pass in the except section here - https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
#try:
    #while x < z:
      #  if y < z:
                #put code here
        #    scatter(x,y)
        #    y += 1
      #  elif y == z:
       #     x += 1
       #     y = x + 1
            # put code here
        #    scatter(x,y)
       #     y += 1
#except:
  #  pass

#tip picked up from median blog
iris_setosa=df.loc["Iris-setosa"]
iris_virginica=df.loc["Iris-virginica"]
iris_versicolor=df.loc["Iris-versicolor"]

for measurement in df.columns:
    fig, ax = plt.subplots()
    ax.hist(iris_setosa[measurement], color='b', label='Setosa', alpha =0.3)
    ax.hist(iris_virginica[measurement], color='g', label = 'Virginica', alpha = 0.3)
    ax.hist(iris_versicolor[measurement], color='r', label = 'Versicolor', alpha = 0.3)
    name = nameFormat(measurement)
    ax.set_xlabel(name + ' (cm)')
    ax.set_ylabel ("Frequency")
    ax.set_title("Histogram of " + name + " Frequency for each Iris Type")
    ax.legend()
    fig.savefig("separated" + measurement + "Hist.png")
    plt.clf()
    plt.close()

x = 0
y = 1
z = len(df.columns)

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
    ax.scatter(iris_setosa[setosa_x],iris_setosa[setosa_y], color='b', label='Setosa')
    ax.scatter(iris_virginica[virginica_x],iris_virginica[virginica_y], color='g', label = 'Virginica')
    ax.scatter(iris_versicolor[versicolor_x],iris_versicolor[versicolor_y], color='r', label = 'Versicolor')
    xaxisName = nameFormat(xaxis)
    yaxisName = nameFormat(yaxis)
    ax.set_xlabel(xaxisName + " (cm)")
    ax.set_ylabel(yaxisName + " (cm)")
    ax.legend()
    ax.set_title(xaxisName + " Vs " + yaxisName + " (cm)")
    fig.savefig("separated" + xaxis + "Vs" + yaxis + ".png")
    plt.clf()
    plt.close()

try:
    while x < z:
        if y < z:
                #put code here
            scatter2(x,y)
            y += 1
        elif y == z:
            x += 1
            y = x + 1
            # put code here
            scatter2(x,y)
            y += 1
except:
    pass


#trying seaborn plots now
# df2 workaround bassed off of https://stackoverflow.com/questions/49834883/scatter-plot-form-dataframe-with-index-on-x-axis
df2 = df.reset_index()

# using seaborn documentation - https://seaborn.pydata.org/tutorial/distributions.html
for measurement in df2.columns:
    name = df2[measurement].name
    if name != "type":
        sns_plot = sns.catplot(x="type", y=measurement, data=df2)
        sns_plot.savefig(measurement + "catplot.png")
        plt.clf()
        plt.close()


sns_plot2 = sns.pairplot(df2, hue = "type")
sns_plot2.savefig("seabornpairplot.png")
plt.clf()
plt.close()


#box plot wasn't allowing me to savefig, so using this https://stackoverflow.com/questions/35839980/how-to-save-picture-boxplot-seaborn
for measurement in df2.columns:
    name = df2[measurement].name
    if name != "type":
        fig, ax = plt.subplots()
        sns.boxplot(x = "type", y = measurement, data = df2, ax = ax)
        plt.savefig(measurement + "boxplot.png")
        plt.clf()
        plt.close()