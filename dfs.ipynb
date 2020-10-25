# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:09:56 2020

@author: matth
"""

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
1. Salary Data Pull

Save as csv from DK website

"""
df = pd.read_csv('DKSalaries.csv',
                index_col='Name').replace({"^\s*|\s*$":""}, regex=True)
df.index = df.index.str.rstrip() #dksalaries some names have trailing white space

df['Team'] = df['TeamAbbrev']

#Strip opponent from 'Game Info' column
df['Opp'] = df['Game Info'].str.split(' ', n=1, expand=True)[0]
df['Opp'] = df['Opp'].replace(df['Team'],'', regex = True)
df['Opp'] = df['Opp'].str.replace('@','')

df.drop(['Name + ID','ID','TeamAbbrev','Roster Position','Game Info','AvgPointsPerGame'], axis=1, inplace=True)

"""
2. Weekly player stats download

https://www.fantasypros.com/nfl/reports/leaders/ppr.php?year=2020

Select Week
Select PPR
Note, does not include DK bonus like 300pa or 100yds
Download csv by week and name "Week1" etc.

"""

CURRENT_WEEK = 6

WEEKS = ['Week' + str(i+1) for i in range(CURRENT_WEEK)]


d = {}
for wk in WEEKS:
    d[wk] = pd.read_csv(str(wk + '.csv'), index_col='Player').replace({"^\s*|\s*$":""}, regex=True)

"""
3. Data Clean on merge sources

DKSalaries does not use the same name conventions with Fantasy Pros 
for the following major cases
"""

#replace df / DKSalaries name with the name used in fantasypros
df = df.rename(index={'Patrick Mahomes':'Patrick Mahomes II'})
df = df.rename(index={'Chris Herndon':'Chris Herndon IV'})
df = df.rename(index={'DJ Chark Jr.':'D.J. Chark Jr.'})
df = df.rename(index={'DJ Moore':'D.J. Moore'})
df = df.rename(index={'DK Metcalf':'D.K. Metcalf'})
df = df.rename(index={'Duke Johnson':'Duke Johnson Jr.'})
df = df.rename(index={'Dwayne Haskins Jr.':'Dwayne Haskins'})
df = df.rename(index={'John Ross III':'John Ross'})
df = df.rename(index={'La\'Mical Perine':'Lamical Perine'})
df = df.rename(index={'Ray-Ray McCloud III':'Ray-Ray McCloud'})
df = df.rename(index={'Steven Sims Jr.':'Steven Sims'})
df = df.rename(index={'La\'Mical Perine':'Lamical Perine'})

df['Team'] = df['Team'].replace(['JAX'],'JAC')
df['Opp'] = df['Opp'].replace(['JAX'],'JAC')

### NEED TO CHECK PLAYER NAMES OF TEAMS NOT ON SLATE: 

### MIA BAL IND NYG PHI CHI MIN LAR

### Also check that team abbrev matches

### A player that hasn't shown up with points on fantasy points may also
### slip through the cracks!

### Every week check the wkly salaries for a quick scan

#replace DST names of df / DKSalaries to what fantasypros uses
fp_dsts = d['Week1'][d['Week1']['Position'] == 'DST']

df = df.rename(index=lambda x: 
               fp_dsts[fp_dsts['Team'] == df.loc[x]['Team']].index[0]
               if str(df.loc[x]['Position']) == 'DST' 
               else x)

"""
4. HOW TO ACCESS

DATAFRAMES

df              // current week salaries
d['Week1']      // Week 1 player,team,position,points
"""

"""
5. Add best week
"""

#Get player's score from a single week
def get_week_score(player: str, wk: pd.DataFrame):
    try:
        x = d[wk].loc[player]['Points']
    except KeyError:
        x = np.nan
    return x

#nan = strictly bye or IR
#0 = active, no relevance
def get_week_scores(player):
    return [get_week_score(player,wk) for wk in WEEKS]
        
df['All Scores'] = df.index.map(get_week_scores)
df['Best Score'] = df['All Scores'].map(max)
df['Best / Sal'] = round(df['Best Score']*1000 / df['Salary'], 2)

df = df.sort_values(by=['Best / Sal'], ascending=False)

print(df.head())