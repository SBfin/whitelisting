# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:25:34 2022

@author: silvi
"""

import pandas as pd
import numpy as np
import json
import requests
import traceback
import time
import matplotlib.pyplot as plt
import seaborn as sns
import networkx

raw = pd.read_excel("tables/follower_raw.xlsx")
pivot = pd.read_excel("tables/pivot.xlsx")
pivot.set_index("profileId", inplace = True)

sns.set()
sns.heatmap(pivot, cmap="YlGnBu", cbar=False)
plt.show()
