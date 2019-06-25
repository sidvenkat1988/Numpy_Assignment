#Problem 9
#Swapping columns 1 and 2 in an array(ref : https://stackoverflow.com/questions/41188901/swap-columns-of-an-ndarray)
arr = np.arange(9).reshape(3,3)
arr
arr = arr[:,[1,0,2]]
arr