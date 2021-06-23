import csv
import statistics as st
import pandas as pd

df  = pd.read_csv('SOCR-HeightWeight.csv')
height = df["Weight(Pounds)"].tolist()
mean = st.mean(height)
print(mean)
median = st.median(height)
print(median)
mode = st.mode(height)
print(mode)