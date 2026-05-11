#!/usr/bin/env python

from scipy.optimize import curve_fit
import numpy as np
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.arange(1,25).reshape(-1,1)
y = [ 100, 98, 94, 92, 90, 85, 80, 75, 72, 70, 65, 70, 72, 74, 76, 80, 82, 85, 90, 92, 94, 96, 98, 100 ]

degrees = [ 3, 4, 5 ]
models={}
predictions={}
r2_scores={}

for degree in degrees:

	poly_features = PolynomialFeatures(degree=degree)
	X_poly = poly_features.fit_transform(X)
	model = LinearRegression().fit(X_poly, y)
	y_pred = model.predict(X_poly)
	r2_scores[degree] = r2_score(y, y_pred)
	models[degree] = model
	predictions[degree] = model.predict(poly_features.transform([[6.5]]))

for degree in degrees:

	print("Degree {}: R2 score = {}, Predicted speed at 6:30 AM = {}".format(degree, r2_scores[degree], predictions[degree]))
