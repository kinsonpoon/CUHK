import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

X_train = [[5.3], [7.2], [10.5], [14.7], [18], [20]]
y_train = [[7.5], [9.1], [13.2], [17.5], [19.3], [19.5]]

X_test = [[6], [8], [11], [22]]
y_test = [[8.3], [12.5], [15.4], [19.6]]

poly = PolynomialFeatures(degree=5) #order 5 feature constructor
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
#linear
lr_model=LinearRegression()
lr_model.fit(X_train,y_train)
lr_score=lr_model.score(X_test, y_test)
#print("Linear regression (order 1) score is:",lr_score)
#poly
# some code here
pr_model= LinearRegression()
pr_model.fit(X_train_poly,y_train)
pr_score=pr_model.score(X_test_poly, y_test)
print("y1=",pr_model.intercept_[0], end='')
for i in range(len(pr_model.coef_[0][1:])):
    print (pr_model.coef_[0][i+1], end='')
    for j in range(i):
        print("x*", end='')
    print("x", end='')
    try:
        if(float(pr_model.coef_[0][i+2])>0):
            print("+", end='')
    except:
        pass
print("")
print("Linear regression (order 5) score is:",pr_score)
#
xx = np.linspace(0, 26, 100)
xx_poly = poly.transform(xx.reshape(xx.shape[0], 1))
yy_poly = pr_model.predict(xx_poly)
#
# some code here
plt.plot(xx,yy_poly,  color='black', linewidth=5)
plt.plot(X_test, y_test, color='blue', linewidth=8)
#plt.xlabel("x")
#plt.ylabel("y")
plt.xticks(())
plt.yticks(())
plt.title('Linear regression (order 5) result', color='black')
plt.show()
#Ridge
ridge_model = Ridge(alpha=1, normalize=False)
ridge_model.fit(X_train_poly, y_train)

# some code here
print("y2=",ridge_model.intercept_[0],"+",end="")
#print(ridge_model.coef_[0])
for i in range(len(ridge_model.coef_[0][1:])):
    print (ridge_model.coef_[0][i+1], end='')
    for j in range(i):
        print("x*", end='')
    print("x", end='')
    try:
        if(float(ridge_model.coef_[0][i+2])>0):
            print("+", end='')
    except:
        pass
print("")
ridgescore=ridge_model.score(X_test_poly, y_test)
print("Ridge regression (order 5) score is:",ridgescore)
yy_ridge = ridge_model.predict(xx_poly)#get predictions for xx_poly

#PLOT
plt.plot(xx,yy_ridge,  color='black', linewidth=5)
plt.plot(X_test, y_test, color='blue', linewidth=5)
#plt.xlabel("x")
#plt.ylabel("y")
plt.xticks(())
plt.yticks(())
plt.title('Ridge regression (order 5) result', color='black')
plt.show()
#
'''
#try bonus
pr_score=0
rd_score=0
pr_count=0
rd_count=0
for i in range(50):
    poly = PolynomialFeatures(degree=i) #order 5 feature constructor
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    #linear
 #   pr_model= LinearRegression()
    pr_model.fit(X_train_poly,y_train)
    
#    ridge_model = Ridge(alpha=1, normalize=False)
    ridge_model.fit(X_train_poly, y_train)
    print(ridge_model.intercept_[0])
    if(ridge_model.score(X_test_poly, y_test)>rd_score):
        rd_count=i
    rd_score=max(rd_score,ridge_model.score(X_test_poly, y_test))
    
    
    if(pr_model.score(X_test_poly, y_test)>pr_score):
        pr_count=i
    pr_score=max(pr_score,pr_model.score(X_test_poly, y_test))
#print("Linear regression (order",pr_count,") score is:",pr_score)
#print("Linear regression (order",rd_count,") score is:",rd_score)

'''

