from matplotlib.pyplot import get
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from joblib import load,dump
import pandas as pd
from images import get_images

#getting images
images = get_images()
#choosing features and labels
X,y = images.iloc[:,:-1],images.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,stratify=y,test_size=0.2,random_state=0)

def get_best_model(X_train,y_train):
#classifiers and parameters
    classifiers = {
        'Decision tree': {
            'model': DecisionTreeClassifier(),
            'params':{
                'max_depth':[None,10]

            }
        },
        'Random Forest': {
            'model': RandomForestClassifier(),
            'params':{
                'n_estimators':[100,200]
            }
        },
        'Ada Boost': {
            'model': AdaBoostClassifier(),
            'params':{
                'n_estimators':[50,100]
                
            }
        },
        'SVC': {
            'model': SVC(),
            'params':{
                'C':[1,10],
                'kernel':['rbf','poly']
                
            }
        },
        'KNN': {
            'model': KNeighborsClassifier(),
            'params':{
                'n_neighbors':[5,10],
                'p':[1,2]
            }
        }
    }
    results = []
    #gridsearch cross validation to choose the best model
    for name,param in classifiers.items():
        grid = GridSearchCV(param['model'],param['params'],cv=3)
        grid.fit(X_train,y_train)
        #pickling each model with best params for later use
        dump(grid,f"{name}_with_{grid.best_score_}_acc.joblib")

        print(f"{name} model fitted with its best parameters saved as {name}_with_{grid.best_score_}_acc.joblib")

        results.append({
            'model':name,
            'best score':grid.best_score_,
            'best parameters':grid.best_params_
        })
        print(f'hyperparameter tuning for {name} has been completed')
    print
    results_df = pd.DataFrame(results)
    print(results_df)

    get_best_model(X_train,y_train)