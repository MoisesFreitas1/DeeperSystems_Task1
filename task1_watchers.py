#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:36:24 2020

@author: Moises
"""

import pandas as pd
import json

df_json = pd.read_json('source_file_2.json')
df_json = df_json.sort_values(by ='priority')
df_json = pd.concat([df_json], ignore_index=True)

watchers = df_json['watchers'].to_frame()
watchers = pd.concat([watchers], ignore_index=True)

watchersSTR = []
for row in range(len(watchers)):
    sets = watchers.iloc[row].to_string().replace('watchers    ', '')
    sets = sets.replace('[', '')
    sets = sets.replace(']', '')
    sets = sets.replace(' ', '')
    
    if("," in sets):
        manSet = sets.split(',')
        for i in range(0, len(manSet)):
            watchersSTR.append(manSet[i])
    else:
        watchersSTR.append(sets)
        
watchersSets = pd.DataFrame(watchersSTR).drop_duplicates()

watchers_List_Col = watchersSets.iloc[:,0].to_list()

listProjects = [[]]
for i in range(1,len(watchers_List_Col)):
    listProjects.append([])
    
listProjects[1]
for i in range(len(df_json)):
    for j in range(len(watchersSets)):
        if(watchersSets.iloc[j].to_string().replace(str(0) + "    ", "") in df_json.loc[i,'watchers']):
            col = watchersSets.iloc[j].to_string().replace(str(0) + "    ", "")
            listProjects[j].append(df_json.loc[i,'name'])

watchersDF = pd.DataFrame([listProjects], columns = watchers_List_Col)
watchersDict = watchersDF.to_dict(orient='list')

with open('watchers.json', 'w') as fp:
    json.dump(watchersDict, fp)