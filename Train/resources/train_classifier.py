
# Train logistic regression model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump, load
import os
import pandas as pd
import json

def train(clf):
    #data_repo = os.path.join('hello-world/Data preprocessing/' "data.json") #os.environ['DATA_REPO']
    #print(data_repo)
    #data_repo = "hello-world\Data preprocessing\resources\data.json"
    df = pd.read_json(r"Data preprocessing\data.json", orient="split")

    # Select features
    X = df.loc[:, df.columns != 'labels']

    # Select label
    y = df['labels']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.9)

    #train model
    clf = LogisticRegression().fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_pred, y_test)
    dump(clf, 'clf.joblib')
    return json.dumps({'message': 'The model was saved locally.',
                       'accuracy test':  accuracy}, sort_keys=False, indent=4), 200

    """
    clf_api = os.environ['CLF_API']
    if clf_api:
        clf.save(os.path.join(clf_api), "classifier")

    if type(classifier) == LogisticRegression:
        return 'Logistic regression model is trained'
        """

