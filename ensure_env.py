# Ensure environment has required libraries
import pandas as pd
import pytest
import unittest
import requests

# Simple pandas test to verify environment works

# Create a simple DataFrame
data = [("Mercury", 1), ("Venus", 2), ("Earth", 3)]
columns = ["Name", "Number"]

df = pd.DataFrame(data, columns=columns)

# Show the DataFrame
print(df)

# Perform a simple operation (count the number of rows)
count = len(df)

# Print the count
print(f"Number of rows in the DataFrame: {count}")