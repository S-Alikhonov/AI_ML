from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import AdaBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from catboost import CatBoostClassifier
from sklearn.svm import SVC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import without_aug as he

X_train, X_test, y_train, y_test = he.data_preprocessing("new_data.csv")
X_train_scaled, X_test_scaled, ct = he.column_transformer(X_train, X_test)
clf_tuned_models = {
    'SVC': SVC(),
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'GradientBoosting': GradientBoostingClassifier(max_depth=1, n_estimators=250),
    'AdaBoostClassifier': AdaBoostClassifier()
}

tuned_scores_aug = he.get_scores(clf_tuned_models)
print("Without Aug")
print("*"*20)
print(he.tuned_scores_no_aug)
print("With Aug")
print("*"*20)
print(tuned_scores_aug)
