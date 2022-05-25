# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:52:22 2022

@author: silvio
"""
import requests
import json
import pandas as pd

a = list(map(hex, range(pow(2,8) - 1)))
b = [elem[0:2]+"0"+elem[2:] for elem in a][0:8]
bjson = json.dumps(b)

start = 0x000
end = 0xFFF
hex_list = ['0x{:02X}'.format(x) for x in range(int(start), int(end+1))][0:100]
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
profiles = profiles.explode("attributes")

dict_cols = ["stats", "picture", "coverPicture", "followModule", "attributes"]
lst = []
lst.append(profiles.reset_index(drop = True))
for col in dict_cols: 
    lst.append(pd.json_normalize(profiles[col].reset_index(drop = True)))

profiles.drop(dict_cols, axis = 1, inplace = True)
profiles_final = pd.concat(lst, axis = 1).drop(dict_cols, axis = 1)
profiles_final.to_excel("profiles.xlsx")
