# AdaBoost Classification
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
import pickle


#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
#dataframe = pandas.read_csv(url, names=names)
#array = dataframe.values




# Read in muffin and cupcake ingredient data# Read i 
#recipes = pd.read_csv('test_liar_feature.csv')
recipes = pd.read_csv('fulltrain_Guardian_Nyt_binary_shuffled_feature.csv')
#recipes

print("csv load done")













#recipes[['Article_len','Avg_Word_Len','CountOfNumbers','CountofExclamation','adjectives','WordCount','sent_neg','sent_neu','sent_pos']].as_matrix()

X = recipes[['Article_len','Avg_Word_Len','CountOfNumbers','CountofExclamation','adjectives','WordCount','sent_neg','sent_neu','sent_pos']].as_matrix()
y = np.array(recipes['label'])


print("feature load done")



seed = 7
num_trees = 30
#kfold = model_selection.KFold(n_splits=10, random_state=seed)
#model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
clf_adaboost = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
#results = model_selection.cross_val_score(model, X, Y, cv=kfold)
#print(results.mean())



##model save
print("training start.........")
print(".")
print("adaboost start")
clf_adaboost.fit(X, y)
filename = 'adaboost.sav'
pickle.dump(clf_adaboost, open(filename, 'wb'))
print("adaboost done")