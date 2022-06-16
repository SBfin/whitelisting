# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:57:35 2022

@author: silvio
"""

"""
A top down bot estimation based on lens handle finishing with 8 numbers
a lower bound
"""

import pandas as pd
import numpy as np

df = pd.read_excel("tables/all_profiles.xlsx")

"""
num > 8
"""
handles = list(df["handle"])
numbers = [sum(c.isdigit() for c in handle) for handle in handles]
red_flag = [num for num in numbers if num > 7]
perc_of_profiles_flag = len(red_flag)/len(numbers)

"""
publications / day active
"""
df["days_active"] = 25 - df.index / 1000
df["days_active"] = df["days_active"].clip(1)
df["publications / days"] = df["totalPublications"]/df["days_active"]
df_filter = df[df["publications / days"] > 10]
