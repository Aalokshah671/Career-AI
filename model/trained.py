import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression


data = pd.read_csv('utils/data/training_data.csv')

x=data[['match_score']]
y=data['selected']

model=LogisticRegression()
model.fit(x,y)

pickle.dump(model, open("model/model.pkl", "wb"))

print("model trained")