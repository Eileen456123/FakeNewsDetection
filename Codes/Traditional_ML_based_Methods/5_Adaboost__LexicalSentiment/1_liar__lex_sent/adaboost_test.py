import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import pickle
from sklearn.tree import tree


# Read in muffin and cupcake ingredient data# Read i
#recipes = pd.read_csv('test_liar_feature.csv')
recipes = pd.read_csv('liar_test_feature.csv')
#recipes

print("csv load done")

X = recipes[['Article_len','Avg_Word_Len','CountOfNumbers','CountofExclamation','adjectives','WordCount','sent_neg','sent_neu','sent_pos']].as_matrix()
y = np.array(recipes['label'])



print("label load done")
# Feature names
recipe_features = recipes.columns.values[1:].tolist()
print(recipe_features)


##########################
filename = 'adaboost.sav'
loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X, y)
#print(result)



pred = loaded_model.predict(X)

print("###################")
print(".")
print("test results: ")
print("---------adaboost---------------------")
print ("test_accuracy: ")
print (accuracy_score(y, pred))

print ("test_precision: ")
print (precision_score(y, pred, average="weighted"))

print ("test_recall: ")
print (recall_score(y, pred, average="weighted"))

print ("test_f1 ")
print (f1_score(y, pred, average="weighted"))




filename = 'adaboost_pickle.pickle'
pickle.dump((y,pred), open(filename, 'wb'))










