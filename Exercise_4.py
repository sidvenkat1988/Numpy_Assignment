#Problem4
#Common items between two numpy arrays(ref : https://stackoverflow.com/questions/1613249/numpy-comparing-elements-in-two-arrays)
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
c