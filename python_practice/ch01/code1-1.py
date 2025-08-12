import pandas as pd

#converted to panda state
age = pd.Series([25, 34, 19, 45, 60])
age 

type(age)

data = ['spring','summer','fall','winter']
season = pd.Series(data)
season

season.iloc[2]

#DATAFRAME

score = pd.DataFrame([[85, 96, 40, 95],
                     [76, 69, 69, 80],
                     [78, 50, 60, 90]])

score

type(score)
score.index
score.columns

score[1,2]

#NUMPY

import numpy as np

w_np = np.array([65.4, 75.3, np.nan, 57.8])
weight = pd.Series(w_np)
weight
                    
                      