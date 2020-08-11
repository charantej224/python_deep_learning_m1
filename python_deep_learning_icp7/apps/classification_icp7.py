from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer()

X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = clf.predict(X_test_tfidf)

print("Score without bigram")
print(metrics.accuracy_score(twenty_test.target, predicted))

counter = 0
faults = 0

for i in range(len(twenty_test.target)):
    if twenty_test.target[counter] != predicted[counter]:
        faults += 1
    counter += 1

print("failed {} out of total {}".format(faults, len(twenty_test.target)))
print("passed {} out of total {}".format(len(twenty_test.target) - faults, len(twenty_test.target)))
print("passed % {}".format((len(twenty_test.target) - faults)/len(twenty_test.target)))
