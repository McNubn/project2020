# Fisher's Iris Data Set Analysis

# Introduction

This repo contains the famous Fisher's Iris Data set (iris_csv.csv), a program that will create a number of plots (the .png files) alongside summary statistics (analysis.txt), and the aforementioned files created by the program.

## How to use this GitHub repository?
- this README will introduce you to the data set, my observations from the plots I have performed, as well as referencing research on this data set by others.
- [how to run the program and navigate]

## What is Fisher's Iris Data set?

Fisher's Iris Data Set is a set of data that contains the measurements of the sepeal length, sepal width, petal length and petal width of three types of Iris flower - Iris Setosa, Iris Virginica and Iris Versicolor. Although this data set was made famous by Ronald Fisher's paper "The use of multiple measurements in taxonomic problems", it was actually gathered by Edgar Anderson. The data set contains the aforementioned measurements for 150 Iris flowers, with 50 in each of the 3 Iris categories.

## Why is this data set used?

This data set is often used to introduce students to multivariate data analysis, as well as for machine learning studies, as it is a relatively small data set at 150 observations, while still being just large enough for skills building. Meanwhile the limited number of variants (i.e. the four measurements on each flower) alongside the small set of categories (i.e. the three types of Iris flower measured) allow students to practice various plotting techniques with real data. Finally, Ronald Fisher himself was a well respected statistician and his impact on the field of statistics is still felt today.

## Any controversies regarding this data set?

While studying this data set, it became apparently that there is some mild controversy in the field of botany regarding the defintion of sepals and petals in the case of Iris flowers ([as can be seen here](https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data)). That said, this particular controversy does not spill over into the field of statistics, data analysis or machine learning, and so doesn't impact this particular project. 

# Creation of the program

## Libraries used & why

For this project, I have used the following Python Libraries:

* Pandas - Pandas is a library made specifically for creating and manipulating data frames in Python. These two dimensional data structures (i.e. they have rows as well as columns) allow data scientists to select and manipulate the data to their equirements. This allows for easier plotting, whether that be Panda's own plotting functionality, or via other libraries. In this project, Pandas has been used to create the iris_csv.csv file, and then structure the dataframe so that I could make the desired plots.
* Matplotlib.pyplot - Matplotlib is the most popular library for creating plots in Python, and in fact numerous other libraries for plotting are based off the functionality of Matplotlib. In this project I have used matplotlib.pyplot to create histograms and scatter plots for the various measurements in the data set.
* Seaborn - Seaborn is another popular library for creating plots in Python, and is based on the functionality introduced by Matplotlib. Seaborn introduces a few new plot types, as well as some more aesthetically pleasing default settings for those plots. In this project I've used Seaborn for Cat Plots, Box Plots, Violin Plots and a Pair Plot.



## Plots used & evolution of those plots in my code

Histograms - Total Data > Histograms by Iris type
Scatter Plot - Total Date > Colouring by Iris type
Boxplots - 
Catplot - 
Pairplot - 

Mention use of for loops, if statements, dataframe slicing (to create the 3 categories of Iris), function (nameFormat & scatter), file management (writing to analysis.txt). Discuss why I used these for this purpose.

## References and resources used for this

Medium post - 
StackOverflow - 
Geekforgeeks - 
DataCamp - name courses

# Analysis - Findings

## Various plots and what we can read from them

Talk through each plot and what it shows. Highlight what we see in the initial histograms and scatter plots versus the newer ones.

## Summary of overall picture from above points

What do all of these tell us? How can we be sure we're looking at a particular type of Iris.

# Research conducted by others

## Their findings & how it aligns/doesn't with mine

