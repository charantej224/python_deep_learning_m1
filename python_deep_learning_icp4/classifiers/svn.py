import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import time
from sklearn import metrics

data = pd.read_csv("glass.csv")
X_train, X_test = train_test_split(data, test_size=0.4, random_state=int(time.time()))

features = [
    "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe"
]
svc_linear = SVC(kernel='linear')
svc_linear.fit(
    X_train[features].values,
    X_train["Type"]
)

Y_pred = svc_linear.predict(X_test[features])
acc_svc = round(svc_linear.score(X_test[features].values, X_test["Type"]) * 100, 2)
print("svm accuracy is:", acc_svc)

svc_rbf = SVC(kernel='rbf')
svc_rbf.fit(
    X_train[features].values,
    X_train["Type"]
)

Y_pred = svc_rbf.predict(X_test[features])
acc_svc = round(svc_rbf.score(X_test[features].values, X_test["Type"]) * 100, 2)
print("svm accuracy is:", acc_svc)
print("\n")
print(metrics.classification_report(X_test["Type"], Y_pred))
