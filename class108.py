# -*- coding: utf-8 -*-
"""class108.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hRkSINoDdqyouzN3AGyzULm2buchBJbf
"""

import csv
import pandas as pd
import plotly.figure_factory as ff


df=pd.read_csv('18Yearshgwht.csv')
print(df)

fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Result"],show_hist=False)
fig.show()