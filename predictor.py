#!/usr/bin/env python
# coding: utf-8

# In[1]:


def predictRuns(input_data):
    import joblib
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    with open('venue_encoder.joblib','rb') as f:
        venue_encoder = joblib.load(f)
    with open('team_encoder.joblib','rb') as f:
          team_encoder = joblib.load(f)
    with open('rf_encoder.joblib','rb') as f:
          forest = joblib.load(f)
    with open('striker_encoder.joblib','rb') as f:
          striker_encoder = joblib.load(f)
    with open('bowler_encoder.joblib','rb') as f:
          bowler_encoder = joblib.load(f)
    df_read = pd.read_csv(input_data)
    
    dfinput = df_read.rename({'batsmen': 'striker', 'bowlers': 'bowler'}, axis = 1)
    dfinput['striker'] = dfinput['striker'].str.strip('()').str.split(',')
    dfinput['striker'] = dfinput.striker[0][0]
    dfinput['bowler'] = dfinput['bowler'].str.strip('()').str.split(',')
    dfinput['bowler'] = dfinput.bowler[0][0]

    dfinput = dfinput[['venue','innings','batting_team','bowling_team','striker','bowler']]
    dfinput = dfinput.loc[:, 'venue':'bowler']
    current_venues = ['M Chinnaswamy Stadium','Eden Gardens', 'Feroz Shah Kotla', 'MA Chidambaram Stadium','Wankhede Stadium']
    for i in range(0, len(dfinput)):
          if dfinput.loc[i,'venue'] not in current_venues:
                 dfinput.loc[i,'venue'] = 'Others'
       

    dfinput['venue'] = venue_encoder.transform(dfinput['venue'])
    dfinput['batting_team'] = team_encoder.transform(dfinput['batting_team'])
    dfinput['bowling_team'] = team_encoder.transform(dfinput['bowling_team'])
    dfinput['striker'] = striker_encoder.transform(dfinput['striker'])
    dfinput['bowler'] = bowler_encoder.transform(dfinput['bowler'])

    inputarray = dfinput.to_numpy()
    data = inputarray[:,:6]
    data = np.insert(data,2,5.6)
    data = np.array([data])
    prediction = int(forest.predict(data)[0])

    return(prediction)
  

  




