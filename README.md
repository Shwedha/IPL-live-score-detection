# IPL LIVE SCORE PREDICTION

A live predictor to predict scores of the match in advance.

## PREREQUISITES:
1. Python
2. Any editor like sublime text or visual editor to view the joblib files

## OVERVIEW: 
Live score predction of the IPL match that took place April 2021 to May 2021
1. DATA SHEET: The data set was taken from https://cricsheet.org/ and I also uploaded the data set in my kaggle account: https://www.kaggle.com/shwedhasrinivasan/ipl-dataset, its used as all_matches.csv in the preprocessing file
2. PREPROCESSING FILE: This python file is responsible for EDA analysis, generation of test and train data thats useful for generating the joblib files to save the model.
3. JOBLIB FILES: There are 5 joblib files for bowler, striker, venue, team and rf(random forest), since random forest classifier joblib file exceede 25MB, it couldnt be uploaded.
4. PREDICTOR FILE: This opens up all the models saved as joblibs and uses them to make predictions. 
5. MAIN FILE: When the user gives the input file it predicts the scores and returns the output.

## PRE-PROCESSING THE DATASETS:

1. Eradicating all the data that does not make sense / duplicates / NaN values.
2. Addition of columns that compute the total number of runs done by each player and also an extra column that adds the total runs secured by the team itself.
3. One hot encoding to perform modelling for venue, batting team, bowling team, striker and bowler.


## MODELLING:

Out of all the models performed only Random forest was the most accurate, so I have only kept that model and again converted to joblob file to run the predictor. Inorder to add more models, you could just add the code for each model under the preprocessing file and make sure to include them in the predictor file as well. 
