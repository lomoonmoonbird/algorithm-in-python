from sklearn.naive_bayes import GaussianNB

import numpy as np

x = np.array([[-1,7], [1,5], [1,2], [-2,0],[2,3], [-4,0],[-1,1],[1,1],[-2,2],[2,7],[-4,1],[-2,7]])

# y = np.array([3,3,3,3,4,3,3,4,3,4,4,4])

y = np.array([1,1,1,1,1,3,3,4,3,4,4,4])

model = GaussianNB()

model.fit(x, y)

predict = model.predict([[1,2],[3,4]])

print (predict)





