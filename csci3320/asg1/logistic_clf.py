import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import linear_model, datasets
from sklearn.cross_validation import train_test_split


n_samples = 10000

centers = [(-1, -1), (1, 1)]
X, y = make_blobs(n_samples=n_samples, n_features=2, cluster_std=1.8,
                  centers=centers, shuffle=False, random_state=42)

y[:n_samples // 2] = 0
y[n_samples // 2:] = 1

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
log_reg = linear_model.LogisticRegression()

# some code here
log_reg.fit(X_train,y_train)
predit=log_reg.predict(X_test)

#check 3.1
for item in predit:
    if(item!=0 and item!=1):
        print(item)
#plot\


area = np.pi * (15 )**2
plt.scatter(X_test[:, 0],X_test[:, 1], c=predit, edgecolors='k', cmap=plt.cm.Paired)
plt.title("Classification with Logistic Regression.")
plt.show()
count=0
for i in range(len(predit)):
    if(predit[i]!=y_test[i]):
        count=count+1
        
print("Number of wrong predictions is:",count)