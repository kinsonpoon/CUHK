import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import seaborn; seaborn.set()

# Load the diabetes dataset
diabetes = datasets.load_diabetes()
print(diabetes )
# which feature
i_feature =0
# Get the feature name
feature_names = ['Age', 'Sex', 'Body mass index', 'Average blood pressure', 'S1',
                 'S2', 'S3', 'S4', 'S5', 'S6']

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, i_feature]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
model = linear_model.LinearRegression()

# Train the model using the training sets
model.fit(diabetes_X_train, diabetes_y_train)

# Explained variance score: score=1 is perfect prediction
model_score = model.score(diabetes_X_test, diabetes_y_test)

#print(diabetes.keys())
#print(diabetes.data)
#print(diabetes.target)
print("Number of features in the Diabetes dataset is:",len(diabetes.feature_names))
#print(diabetes.DESCR)
print("Number of samples in the Diabetes dataset is:",len(diabetes.target))

question1b = {}
list1=[]
for num in range(10):
#    print(num)
#    print(feature_names[num])
    i_feature =num
# Get the feature name

# Use only one feature
    diabetes_X = diabetes.data[:, np.newaxis, i_feature]

# Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
    model = linear_model.LinearRegression()

# Train the model using the training sets
    model.fit(diabetes_X_train, diabetes_y_train)

# Explained variance score: score=1 is perfect prediction
    model_score = model.score(diabetes_X_test, diabetes_y_test)
#    print(model_score)
    question1b[model_score]=feature_names[num]
    list1.append(model_score)
list1.sort(reverse=True)
print("Ordered list of feature names is: [",end='')
count=0
for scores in list1:
    count=count+1
    if count == 10:
        print(question1b[scores],end='')
    else:
        print(question1b[scores]+",",end='')
print("]",end='')
print('')
print("Ordered list of model scores is:",list1)
#lose function
i_feature =2
# Get the feature name

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, i_feature]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
#print(diabetes_X_train)
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
loss = linear_model.LinearRegression()

# Train the model using the training sets
loss.fit(diabetes_X_train, diabetes_y_train)

# Explained variance score: score=1 is perfect prediction
loss_score = loss.score(diabetes_X_test, diabetes_y_test)
print("Value of the loss function for the best fitted model is:",np.mean(loss.predict(diabetes_X_test)-diabetes_y_test))
#444444444444444444444444444444444444444
# Plot outputs
print("THE GRAPH:")
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, loss.predict(diabetes_X_test), color='blue', linewidth=3)
plt.xlabel("Body mass index")
plt.ylabel("Disease Progression")
plt.xticks(())
plt.yticks(())

plt.show()
