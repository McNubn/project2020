# Brian Doheny
# Three main parts:
   # 1. Research the data set online and write a summary about it in the README (using markdown for formatting).
  #  2. Download the data set and add it to the repo. - Done
  #  3. Write a program called analysis.py that:
      #  a. outputs a summary of each file to a single text file,
      #  b. saves a histogram of each variable to png files, - Done
      #  c. outputs a scatter plot of each pair of variables. - Done

# Minimum Viable Project:
    # Standard repo that contains a README, a Python script, a summary text file and images. 
    # The README should contain a summary of the data set and my investigations into it.
    # It should also clearly document how to run the Python code and what the code does.
    # Remember to referece everything - e.g. where I found a code snippet.

#     Week 2 (ending Sunday March 22nd) - Plotting
       # Histograms and Scatterplots are setup and working. 
       # Begin formatting these to make them clear to read.
       # Start pushing some analyses to the text file.

import pandas as pd
from matplotlib import pyplot as plt
# Setting csv to be a global variable, will mean program can be adapted to other files.
csv = 'iris_csv.csv'

# Save the csv to a pandas data frame. I'm setting the index to be the class column.
df = pd.read_csv(csv, index_col = "class")

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
    ax.hist(df[measurement])
    name = nameFormat(measurement)
    ax.set_xlabel(name + ' (cm)')
    ax.set_ylabel ("Frequency")
    ax.set_title("Histogram of " + name + " Frequency")
    fig.savefig(measurement +"Hist.png")
    fig.clf()

x = 0
y = 1
z = len(df.columns)

# Since my while loop was reusing this code, I've made scatter into a function.
def scatter(x,y):
    """ Plots the columns x and y onto a scatter plot, while adding text to the axis and title."""
    fig, ax = plt.subplpots()
    xaxis = df.columns[x]
    yaxis = df.columns[y]
    ax.scatter(df[xaxis],df[yaxis])
    xaxisName = nameFormat(xaxis)
    yaxisName = nameFormat(yaxis)
    ax.set_xlabel(xaxisName + " (cm)")
    ax.set_ylabel(yaxisName + " (cm)")
    ax.set_title(xaxisName + " Vs " + yaxisName + " (cm)")
    fig.savefig(xaxis + "Vs" + yaxis + ".png")
    fig.clf()

# I was getting an error because y was becoming greater than the number of columns. For now I will use a try and except to get past this, as its expected.
# Learned about using pass in the except section here - https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
try:
    while x < z:
        if y < z:
                #put code here
            scatter(x,y)
            y += 1
        elif y == z:
            x += 1
            y = x + 1
            # put code here
            scatter(x,y)
            y += 1
except:
    pass

