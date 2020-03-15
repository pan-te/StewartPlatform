# coding=utf-8
#Prosty test biblioteki mathematics.py
#(C) Daniel Sadlik
#2020

import mathematics as mt

platformBase = mt.Base(16, 2)
platformMoving = mt.Platform(14, 2 , 0)

destPlane = mt.Plane((0.0, 0.0, -16.0), (0, 0, 0))
platformMoving.transform(destPlane)
lengths = mt.calculateLength(platformBase, platformMoving)

for i in range(6):
	print(lengths[i])