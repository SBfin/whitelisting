# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:15:48 2022

@author: silvio
"""
"""
Whitelisting profiles ID based on trustable followers
We have a list of profiles who we trust to be real. They do not follow bots.
"""
import pandas as pd
import numpy as np
import json
import requests
import traceback
import time
import matplotlib.pyplot as plt
import seaborn as sns


"""
Download df with 10000 rows
extract profiles
"""



#pivot.to_excel("tables/pivot.xlsx")
#does_follow.to_excel("tables/follower_raw.xlsx")


df = pd.read_excel("tables/all_profiles.xlsx")
owners_id = df[["ownedBy", "id"]]
owners_id = owners_id.drop_duplicates()


dct = {}
addresses = list(owners_id["ownedBy"])

for j in range(719, len(addresses)):
        print(j)

        query =    '''
                         query Following {
                          following(request: { 
                                        address: "''' + addresses[j] + '''"
                                     }) {
                            items {
                              profile {
                                id
                                
                            }
                          }
                        }
                    }
                                                                  
                                                  
                    '''

       
            
        url = 'https://api.lens.dev'
        
        try:
            r = requests.post(url, json={'query': query})
            content = r.json()
            df_whitelisted = pd.DataFrame(content["data"]["following"]["items"])
        except:
            j = j - 1
            time.sleep(30)
            
            pass
        
        time.sleep(0.05)
        
        if df_whitelisted.size > 0:
            df_whitelisted["address"] = addresses[j]
            df_whitelisted["profile"] = df_whitelisted["profile"].apply(pd.Series)
            dct.update({ j : df_whitelisted})
        

"""
does_follow_merged = does_follow.merge(owners_id, left_on = "followerAddress", right_on = "ownedBy", how = "left")
does_follow_merged = does_follow_merged[["profileId", "id", "follows"]]
pivot = pd.pivot_table(does_follow_merged, values = "follows", index = "profileId", columns = "id")
"""


