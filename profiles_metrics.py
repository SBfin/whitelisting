# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:56:38 2022

@author: silvio
"""

"""
More than stats

"""
import pandas as pd
import numpy as np

df = pd.read_excel("tables/all_profiles.xlsx")

metrics_cols = ['totalFollowers',
                'totalFollowing', 'totalPosts', 'totalComments', 'totalMirrors',
                'totalPublications', 'totalCollects']

df[metrics_cols] = df[metrics_cols].apply(pd.to_numeric, errors='coerce', axis=1)

kwargs = {"histtype" : "step", "density" : True}

df.hist(["totalFollowers", "totalFollowing", "totalCollects"], 
        bins = range(0, 50, 3), layout = (1,3), **kwargs)

df.hist(["totalPosts", "totalComments", "totalMirrors"], 
        bins = range(0, 50, 3), layout = (1,3), **kwargs)


metrics = df[metrics_cols].describe()

metrics.to_excel("tables/metrics.xlsx")
