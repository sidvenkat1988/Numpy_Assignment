#Problem 3
#Generating a custom sequence of numbers
#ref : for repeat(https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html), for repeating an arange array(https://stackoverflow.com/questions/41254355/python-numpy-repeating-an-arange-array), for concatenation(http://lagrange.univ-lyon1.fr/docs/numpy/1.11.0/reference/generated/numpy.concatenate.html)
a = np.array([1,2,3])
b = np.repeat(a,3)
c = list(a)*3
d = np.concatenate((b,c))
d