# Brian Doheny
# Minimum Viable Project:
    # Standard repo that contains a README, a Python script, a summary text file and images. 
    # The README should contain a summary of the data set and my investigations into it.
    # It should also clearly document how to run the Python code and what the code does.
    # Remember to referece everything - e.g. where I found a code snippet.

# Week 1 (ending Sunday March 15th) - Setup
        # Repo is set up - done.
        # Quality version of the data set is found, and added to repo - done.
        # Started getting data set into Pandas data frames, ready for plotting and manipulation.

import pandas as pd

df = pd.read_csv("iris_csv.csv")
print(df)