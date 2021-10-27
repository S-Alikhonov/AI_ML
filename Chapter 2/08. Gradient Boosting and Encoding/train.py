
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pandas as pd
from time import time
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRFRegressor
import catboost
import xgboost
import data_handler as dh

forest = RandomForestRegressor()
tree = DecisionTreeRegressor()
boosted_sk = GradientBoostingRegressor()
cat_booster = CatBoostRegressor(verbose=False)
lgmb_booster  =LGBMRegressor()
xg_booster = XGBRFRegressor()

x_train, x_test, y_train, y_test = dh.get_data("./insurance.csv")
def best_model(X):
    models = {'Decision Tree model':
                {
                    'model': tree,
                    'params': {
                        #'criterion':['squared_error','poisson'],
                        'max_depth':[None,5,10,20],
                        'min_samples_leaf':[1,2,10]
                    }
                },
            'Random Forest model':
                {
                    'model': forest,
                    'params': {
                        'n_estimators':[100,200],
                        'max_depth':[1,5,10]

                    }
        
                },
            'LGBost':
            {
                'model': lgmb_booster,
                'params': {
                    'n_estimators':[10,100,300],
                    'learning_rate':[0.05,0.1]
                }

            },
            'Sklearn Gradient boost':
            {
                'model': boosted_sk,
                'params': {
                    'n_estimators':[100,300],
                    'learning_rate':[0.05,0.01],
                    'max_depth':[3,5,10]

                }

            },
            'XG boost':
            {
                'model': xg_booster,
                'params': {
                    'n_estimators':[10,100,300],
                    #'learning rate':[0.01,0.05,0.1], #it 's giving warning
                    'max_depth':[1,5,10]

                }

            }

    }
    scores = []
    for model_name,param in models.items():
        grid_clf = GridSearchCV(param['model'],param['params'])
        grid_clf.fit(x_train,y_train)
        pred = grid_clf.predict(X)
        acc = grid_clf.score(x_test,y_test)
        


        print(f'{model_name} model has completed fitting process')
        scores.append(
            {
                'name':model_name,
                'model': param['model'],
                'best_score':grid_clf.best_score_,
                'best_parameters':grid_clf.best_params_,
                'accuracy_on_test':acc,
                'prediction':pred
                
            }
        )
    sorted_df = pd.DataFrame(scores).sort_values(by=['best_score'],ascending=False)
    print(sorted_df[['name','accuracy_on_test','prediction']])

