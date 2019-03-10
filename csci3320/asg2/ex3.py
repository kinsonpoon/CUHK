from __future__ import print_function
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn import metrics

def create_data():
    # Generate sample points
    centers = [[3,5], [5,1], [8,2], [6,8], [9,7]]
    X, y = make_blobs(n_samples=1000,centers=centers,cluster_std=0.5,random_state=3320)
    # =======================================
    # Complete the code here.
    # Plot the data points in a scatter plot.
    # Use color to represents the clusters.
    # =======================================
    list_0_X=[]
    list_0_Y=[]
    list_1_X=[]
    list_1_Y=[]
    list_0_X=[]
    list_2_X=[]
    list_2_Y=[]
    list_3_X=[]
    list_3_Y=[]
    list_4_X=[]
    list_4_Y=[]

    for i in range(len(y)):
        if (y[i]==0):
            list_0_X.append(X[i][0])
            list_0_Y.append(X[i][1])
        elif(y[i]==1):
            list_1_X.append(X[i][0])
            list_1_Y.append(X[i][1])
        elif(y[i]==2):
            list_2_X.append(X[i][0])
            list_2_Y.append(X[i][1])
        elif(y[i]==3):
            list_3_X.append(X[i][0])
            list_3_Y.append(X[i][1])
        elif(y[i]==4):
            list_4_X.append(X[i][0])
            list_4_Y.append(X[i][1])

    plt.scatter(list_0_X,list_0_Y,c='red')
    plt.scatter(list_1_X,list_1_Y,c='blue');
    plt.scatter(list_2_X,list_2_Y,c='black');
    plt.scatter(list_3_X,list_3_Y,c='grey');
    plt.scatter(list_4_X,list_4_Y,c='purple');
    plt.show()

    return [X, y]

def my_clustering(X, y, n_clusters):
    # =======================================
    # Complete the code here.
    # return scores like this: return [score, score, score, score]
    # =======================================
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
    #print(kmeans.labels_)
    list_0_X=[]
    list_0_Y=[]
    list_1_X=[]
    list_1_Y=[]
    list_0_X=[]
    list_2_X=[]
    list_2_Y=[]
    list_3_X=[]
    list_3_Y=[]
    list_4_X=[]
    list_4_Y=[]
    list_5_X=[]
    list_5_Y=[]
    for i in range(len(kmeans.labels_)):
        if (kmeans.labels_[i]==0):
            list_0_X.append(X[i][0])
            list_0_Y.append(X[i][1])
        elif(kmeans.labels_[i]==1):
            list_1_X.append(X[i][0])
            list_1_Y.append(X[i][1])
        elif(kmeans.labels_[i]==2):
            list_2_X.append(X[i][0])
            list_2_Y.append(X[i][1])
        elif(kmeans.labels_[i]==3):
            list_3_X.append(X[i][0])
            list_3_Y.append(X[i][1])
        elif(kmeans.labels_[i]==4):
            list_4_X.append(X[i][0])
            list_4_Y.append(X[i][1])
        elif(kmeans.labels_[i]==5):
            list_5_X.append(X[i][0])
            list_5_Y.append(X[i][1])
    try:
        plt.scatter(list_0_X,list_0_Y,c='red')
        plt.scatter(list_1_X,list_1_Y,c='blue');
        plt.scatter(list_2_X,list_2_Y,c='c');
        plt.scatter(list_3_X,list_3_Y,c='grey');
        plt.scatter(list_4_X,list_4_Y,c='purple');
        plt.scatter(list_5_X,list_5_Y,c='green');
    except:
        pass
    for i in range(len(kmeans.cluster_centers_)):
            plt.scatter(kmeans.cluster_centers_[i][0],kmeans.cluster_centers_[i][1],c="black",marker="o",linewidths=10)
    plt.show()
    ari=metrics.adjusted_rand_score(y, kmeans.labels_)
    mri=metrics.adjusted_mutual_info_score(y, kmeans.labels_)
    v_mea=metrics.v_measure_score(y, kmeans.labels_)   
    sil=metrics.silhouette_score(X, kmeans.labels_, metric='euclidean')
    return [ari,mri,v_mea,sil]  # You won't need this line when you are done

def main():
    X, y = create_data()
    range_n_clusters = [2, 3, 4, 5, 6]
    ari_score = [None] * len(range_n_clusters)
    mri_score = [None] * len(range_n_clusters)
    v_measure_score = [None] * len(range_n_clusters)
    silhouette_avg = [None] * len(range_n_clusters)

    for n_clusters in range_n_clusters:
        i = n_clusters - range_n_clusters[0]
        print("Number of clusters is: ", n_clusters)
        [ari_score[i], mri_score[i], v_measure_score[i], silhouette_avg[i]] = my_clustering(X, y, n_clusters)
        print('The ARI score is: ', ari_score[i])
        print('The MRI score is: ', mri_score[i])
        print('The v-measure score is: ', v_measure_score[i])
        print('The average silhouette score is: ', silhouette_avg[i])

    # =======================================
    # Complete the code here.
    # Plot scores of all four evaluation metrics as functions of n_clusters.
    # =======================================

if __name__ == '__main__':
    main()

