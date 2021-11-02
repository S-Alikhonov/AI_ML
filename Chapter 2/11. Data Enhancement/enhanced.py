import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline,Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder,StandardScaler,PowerTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from time import time
from sklearn.metrics import mean_absolute_error,mean_squared_error

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor


data = pd.read_csv('data/london_merged.csv')
np.random.seed(0)

#new feature generation, because it gives more correlation with label, ~0.4, while t1,t2 ~0.36
data['new']= data['t1'] * data['t2']

#additional features
data['months'] = data['timestamp'].apply(lambda x: int(x.split('-')[1]))
data['hours'] = data['timestamp'].apply(lambda x: int(x.split()[1][:2]))
data['years'] = data['timestamp'].apply(lambda x: int(x[:4]))
data.drop('timestamp',axis=1,inplace=True)


def augmentation(data):
    """
    function takes data set as argument, using standard deviation of each column, it changes values of numerical data,
    and returns augmented version of dataset.
    """
    synt_data = data.copy()
    for month in synt_data['months'].unique():

        #storing standard deviation of individual numerical features
        t1_std = synt_data[synt_data['months']==month]['t1'].std()
        t2_std = synt_data[synt_data['months']==month]['t2'].std()
        hum_std = synt_data[synt_data['months']==month]['hum'].std()
        wind_std = synt_data[synt_data['months']==month]['wind_speed'].std()

        #it groups values of the feature according to the month, because those values highly coorelated to the particular month
        for i in synt_data[synt_data['months']==month].index:
            if np.random.randint(2) == 1:
                synt_data['t1'].values[i] += t1_std/5
            else:
                synt_data['t1'].values[i] -= t1_std/5
            
            if np.random.randint(2) == 1:
                synt_data['t2'].values[i] += t2_std/5
            else:
                synt_data['t2'].values[i] -= t2_std/5

            if np.random.randint(2) == 1:
                synt_data['hum'].values[i] += hum_std/5
            else:
                synt_data['hum'].values[i] -= hum_std/5

            if np.random.randint(2) == 1:
                synt_data['wind_speed'].values[i] += wind_std/5
            else:
                synt_data['wind_speed'].values[i] -= wind_std/5
    return synt_data

#creation of augmented dataset
augmented = augmentation(data)

#Chososing features and label
x,y = data.drop('cnt',axis=1),data['cnt']

#splitting into train and test samples
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=0)
#picking 25% of augmented dataset(exactly 25% percent of orginal dataset)
extra_sample = augmented.sample(augmented.shape[0]//4)
#merging synthetic and original train samples
x_train = pd.concat((x_train,extra_sample.drop('cnt',axis=1)),axis=0)
y_train = pd.concat((y_train,extra_sample['cnt']),axis=0)
#making distribution of labels more likely normal, otherwise it's skewed(high variance)
transformer = PowerTransformer()
y_train = transformer.fit_transform(y_train.values.reshape(-1,1))
y_test = transformer.transform(y_test.values.reshape(-1,1))


num_cols = ['t1','t2','hum','wind_speed','new']
cat_cols = ['weather_code','is_holiday','is_weekend','season','months','years','hours']
num_imputer = SimpleImputer(strategy='constant',fill_value=-999)
cat_imputer =SimpleImputer(strategy='constant',fill_value='missing value')
cat_encoder = OrdinalEncoder(handle_unknown='ignore')
#numerical preprocessing pipline
num_pipe = Pipeline([('num_imputer',num_imputer)])
#categorical preprocessing pipeline
cat_pipe = Pipeline([('cat_imputer',cat_imputer),('cat_encoder',cat_encoder)])
#merging both num and categoricals into column transformer
prep_pro = ColumnTransformer([('numerical',num_pipe,num_cols),('categorical',cat_pipe,cat_cols)],remainder='drop')



trees = {
        'Decision Tree': DecisionTreeRegressor(),
        'Random Forest': RandomForestRegressor(),
        'Extra Trees': ExtraTreesRegressor(),
        'Ada Boost': AdaBoostRegressor(),
        'XGB Regressor': XGBRegressor(),
        'LGBM Regressor': LGBMRegressor(),
        'CatBoost Regressor': CatBoostRegressor(verbose=False),
        'Sklearn Gradient Boost' : GradientBoostingRegressor()
}

#creation of pipelines with different models
pipes = {name: make_pipeline(prep_pro,model) for name,model in trees.items()}
results=[]
for name,model in trees.items():
        start = time()
        model.fit(x_train,y_train)
        tot_time = time() - start

        pred = model.predict(x_test)

        results.append({
                'name': name,
                'MSE':  mean_squared_error(y_test,pred),
                'MAE': mean_absolute_error(y_test,pred),
                'fitting time': tot_time
        })
#storing results into dataframe
res= pd.DataFrame(results)
res = res.sort_values(by='MSE')
print(res)