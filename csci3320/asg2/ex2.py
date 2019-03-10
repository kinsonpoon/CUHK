import os.path
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from sklearn.decomposition import PCA

def load_data(digits, num):
    '''
    Loads all of the images into a data-array.

    The training data has 5000 images per digit,
    but loading that many images from the disk may take a while.  So, you can
    just use a subset of them, say 200 for training (otherwise it will take a
    long time to complete.

    Note that each image as a 28x28 grayscale image, loaded as an array and
    then reshaped into a single row-vector.

    Use the function display(row-vector) to visualize an image.
    
    '''
    totalsize = 0
    for digit in digits:
        totalsize += min([len(next(os.walk('train%d' % digit))[2]), num])
    print('We will load %d images' % totalsize)
    X = np.zeros((totalsize, 784), dtype = np.uint8)   #784=28*28
    for index in range(0, len(digits)):
        digit = digits[index]
        print('\nReading images of digit %d' % digit)
        for i in range(num):
            pth = os.path.join('train%d' % digit,'%05d.pgm' % i)
            image = misc.imread(pth).reshape((1, 784))
            X[i + index * num, :] = image
        print('\n')
    return X

def plot_mean_image(X, digits = [0]):
    ''' example on presenting vector as an image
    '''
    plt.close('all')
    meanrow = X.mean(0)
    # present the row vector as an image
    plt.imshow(np.reshape(meanrow,(28,28)))
    plt.title('Mean image of digit ' + str(digits))
    plt.gray(), plt.xticks(()), plt.yticks(()), plt.show()

def main():
    digits = [0, 1, 2]
    # load handwritten images of digit 0, 1, 2 into a matrix X
    # for each digit, we just use 500 images
    # each row of matrix X represents an image
    X = load_data(digits, 500)
    # plot the mean image of these images!
    # you will learn how to represent a row vector as an image in this function
    plot_mean_image(X, digits)
   # print(len(X))
    #print(len(X[1499]))
    ####################################################################
    # plot the eigen images, eigenvalue v.s. the order of eigenvalue, POV
    # v.s. the order of eigenvalue
    # you need to
    #   1. do the PCA on matrix X;
    #
    #   2. plot the eigenimages (reshape the vector to 28*28 matrix then use
    #   the function ``imshow'' in pyplot), save the images of eigenvectors
    #   which correspond to largest 9 eigenvalues. Save them in a single file
    #   ``eigenimages.jpg''.
    #
    #   3. plot the POV (the Portion of variance explained v.s. the number of
    #   components we retain), save the figure in file ``digit_pov.jpg''
    #
    #   4. report how many dimensions are need to preserve 0.9 POV, describe
    #   your answers and your undestanding of the results in the plain text
    #   file ``description.txt''
    #
    #   5. remember to submit file ``eigenimages.jpg'', ``digit_pov.jpg'',
    #   ``description.txt'' and ``ex2.py''.
    # YOUR CODE HERE!

    ####################################################################
    n_components = 784
    pca = PCA(n_components=n_components, svd_solver='randomized',whiten=True).fit(X)
    eigenimages = pca.components_.reshape((n_components, 28, 28))
    #print(len(eigenimages),len(eigenimages[0]))
    
    for i in range(9):
        plt.imshow(eigenimages[i])
        plt.title(i+1)
        plt.gray(), plt.xticks(()), plt.yticks(()), plt.show()
        
    #X_pca = pca.transform(X)
    #3
    
    pov = np.cumsum(pca.explained_variance_ratio_)
    var_exp=sorted(pov)
    #cum_var_exp = np.cumsum(var_exp)
    plt.bar(range(784), var_exp, alpha=0.5, align='center',label='individual explained variance')
   # plt.step(range(9), cum_var_exp, where='mid',
          #   label='cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal components')
    plt.title('the Portion of variance explained v.s. the number of components we retain')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    for i in range(len(var_exp)):
        if var_exp[i] >0.9:
            print("Number of dimensions:",i+1)
            print("Values:",var_exp[i])
            break
if __name__ == '__main__':
    main()
