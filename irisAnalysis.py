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

# Save the csv to a pandas data frame. I'm setting the index to be the class column.
df = pd.read_csv("iris_csv.csv", index_col = "class")

plt.scatter(df['sepallength'],df['sepalwidth'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width (cm)")
plt.savefig("sepalLengthVsWidth.png")
plt.clf()

plt.scatter(df['sepallength'],df['petallength'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Sepal Length vs Petal Length (cm)")
plt.savefig("sepalLengthVsPetalLength.png")
plt.clf()

plt.scatter(df['sepallength'],df['petalwidth'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Sepal Length vs Petal Width (cm)")
plt.savefig("sepalLengthVsPetalwidth.png")
plt.clf()

plt.scatter(df['sepalwidth'],df['petallength'])
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Sepal Width vs Petal Length (cm)")
plt.savefig("sepalWidthVsPetalLength.png")
plt.clf()

plt.scatter(df['sepalwidth'],df['petalwidth'])
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Sepal Width vs Petal Width (cm)")
plt.savefig("sepalWidthVsPetalWidth.png")
plt.clf()

plt.hist(df['sepalwidth'])
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Width Frequency")
plt.savefig("sepalWidthHist.png")
plt.clf()

plt.hist(df['sepallength'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length Frequency")
plt.savefig("sepalLengthHist.png")
plt.clf()

plt.hist(df['petalwidth'])
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Petal Width Frequency")
plt.savefig("petalWidthHist.png")
plt.clf()

plt.hist(df['petallength'])
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Petal Length Frequency")
plt.savefig("petalLengthHist.png")
plt.clf()