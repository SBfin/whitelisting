# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:52:22 2022

@author: silvio

Whitelisting procedure:
    1) Removing obvious bots
    2) Whitelisting people based on a list of "premium users"
        --> "premium users" are supposed to follow high quality profile
        --> If stani follows a profile, then it is not a bot

"""

"""
General profiles metrics (25k profiles)
- most used interactions
- most used posts 

Umami metrics
- site views
- most viewed posts
- which parts of the site are viewed the most

Bot estimation
- back of the envelope # of bots / real profiles

Social network analysis --> clusters of users
"""
import requests
import json
import pandas as pd
import numpy as np
import time
import traceback
from variables import TRUSTABLE_FOLLOWERS
import seaborn as sns
import matplotlib.pyplot as plt

def get_profiles_from_list(hex_list):
    hex_listjson = json.dumps(hex_list)

    query = """query Profiles {
          profiles(request: { profileIds: """ + hex_listjson + """, limit: 50 }) {
              items {
              id
              name
              bio
              attributes {
                displayType
                traitType
                key
                value
              }
              metadata
              isDefault
              picture {
                ... on NftImage {
                  contractAddress
                  tokenId
                  uri
                  verified
                }
                ... on MediaSet {
                  original {
                    url
                    mimeType
                  }
                }
                __typename
              }
              handle
              coverPicture {
                ... on NftImage {
                  contractAddress
                  tokenId
                  uri
                  verified
                }
                ... on MediaSet {
                  original {
                    url
                    mimeType
                  }
                }
                __typename
              }
              ownedBy
              dispatcher {
                address
                canUseRelay
              }
              stats {
                totalFollowers
                totalFollowing
                totalPosts
                totalComments
                totalMirrors
                totalPublications
                totalCollects
              }
              followModule {
                ... on FeeFollowModuleSettings {
                  type
                  amount {
                    asset {
                      symbol
                      name
                      decimals
                      address
                    }
                    value
                  }
                  recipient
                }
                ... on ProfileFollowModuleSettings {
                 type
                }
                ... on RevertFollowModuleSettings {
                 type
                }
              }
            }
            pageInfo {
              prev
              next
              totalCount
            }
          }
        }"""
    
    
    url = 'https://api.lens.dev'
    r = requests.post(url, json={'query': query})
    content = r.json()
    
    profiles = pd.DataFrame(content["data"]["profiles"]["items"])
    #sprofiles = profiles.explode("attributes")
    
    return profiles

def hex2(n):
  x = '%x' % (n,)
  return ('0' * (len(x) % 2)) + x

def iterate_get_profile():
    step = 50
    hex_list = ["0x" + hex2(i) for i in range(1, 25000)]
    dct = {}
    
    for i in range(0, len(hex_list), step):
        print(i)
        time.sleep(0.00000002)
        try:
            profiles = get_profiles_from_list(hex_list[i : i + step])
        except Exception as e:
            print(e)
            pass
        dct.update({i : profiles})
    profiles = pd.concat(dct.values(), ignore_index=True)
    
    dict_cols = ["stats", "picture", "coverPicture", "followModule"]
    lst = []
    lst.append(profiles.reset_index(drop = True))
    for col in dict_cols: 
        lst.append(pd.json_normalize(profiles[col].reset_index(drop = True)))
    
    profiles.drop(dict_cols, axis = 1, inplace = True)
    profiles_final = pd.concat(lst, axis = 1).drop(dict_cols, axis = 1)
    #profiles_final.to_excel("profiles.xlsx")
    
    return profiles_final


df = iterate_get_profile()
df.to_excel("tables/all_profiles.xlsx")



