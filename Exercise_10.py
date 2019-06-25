#Problem 10
#Swapping rows 1 and 2 in an array
arr = np.arange(9).reshape(3,3)
arr

arr = arr[[1,0,2],:]
arr