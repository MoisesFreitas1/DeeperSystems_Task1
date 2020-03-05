#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:32:59 2020

@author: Moises
"""
import pandas as pd
import json


df_json = pd.read_json('source_file_2.json')
df_json = df_json.sort_values(by ='priority')
df_json = pd.concat([df_json], ignore_index=True)

managers = df_json['managers'].to_frame()
managers = pd.concat([managers], ignore_index=True)

managersSTR = []
for row in range(len(managers)):
    sets = managers.iloc[row].to_string().replace('managers    ', '')
    sets = sets.replace('[', '')
    sets = sets.replace(']', '')
    sets = sets.replace(' ', '')
    if("," in sets):
        manSet = sets.split(',')
        for i in range(0, len(manSet)):
            managersSTR.append(manSet[i])
    else:
        managersSTR.append(sets)

managersSets = pd.DataFrame(managersSTR).drop_duplicates()

managers_List_Col = managersSets.iloc[:,0].to_list()

listProjects = [[]]
for i in range(1,len(managers_List_Col)):
    listProjects.append([])
    
listProjects[1]
for i in range(len(df_json)):
    for j in range(len(managersSets)):
        if(managersSets.iloc[j].to_string().replace(str(0) + "    ", "") in df_json.loc[i,'managers']):
            col = managersSets.iloc[j].to_string().replace(str(0) + "    ", "")
            listProjects[j].append(df_json.loc[i,'name'])

managersDF = pd.DataFrame([listProjects], columns = managers_List_Col)
managersDict = managersDF.to_dict(orient='list')

with open('managers.json', 'w') as fp:
    json.dump(managersDict, fp)