import pandas as pd
import sklearn as sk
data = pd.read_table('wine.data',header=None,index_col=False,sep=',',names=['Class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
                                                                    'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
                                                                    'Color intensity','Hue','OD280/OD315 of diluted wines','Proline'])
Y = data['Class']
X = data[data.columns[1:14]]
gen = sk.model_selection.KFold(n_splits=5,shuffle=True,random_state=0)
estimate = sk.neighbors.KNeighborsClassifier()
ev = sk.model_selection.cross_val_score(estimate,X,Y,cv=gen)
print(ev)