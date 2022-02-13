import csv
import pandas as pd
from pathlib import Path  
import streamlit as st

# Day Range Input
input_range = st.number_input("How many days do you want to see?", min_value=1, max_value=999999999)
# input_range = int(input("how many days do you want to see?"))

# Creating Number of Days, Running Total and Amount to Deposit Columns
total = 0
run_total = []
num_days = []
deposit = []
for x in range(1,(input_range+1)):
    days = x
    y = x * 2
    total = y + total
    run_total.append(total)
    num_days.append(days)
    deposit.append(y)

# Creating Dataframe    
savings = {'Deposit':deposit,'Running Total':run_total} 
compound = pd.DataFrame(data=savings, index=num_days)

#Showing Dataframe in table
my_table = st.table(compound)

# Creating a button for the user to download the table as a csv file
@st.cache
def convert_df(compound):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return compound.to_csv().encode('utf-8')

csv = convert_df(compound)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='Compound_Savings.csv',
     mime='text/csv',
 )

# filepath = Path('/Users/porsheaellis/Desktop/bank_com.csv') 
# compound.to_csv(filepath)