#Problem 8
#Supressing scientific notations and setting the precision to 6(ref : https://stackoverflow.com/questions/9777783/suppress-scientific-notation-in-numpy-when-creating-array-from-nested-list and https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html)
np.set_printoptions(suppress=True)
np.set_printoptions(precision=6)
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
rand_arr