# coding=utf-8
#Prosty test biblioteki mathematics.py
#(C) Daniel Sadlik
#2020

import mathematics as mt

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

destPlane = mt.Plane((0.0, 0.0, 140), (1.43, 0.73, -0.67))
platformMoving.transform(destPlane)
lengths = mt.calculateLength(platformBase, platformMoving)

"""for i in lengths:
	print(i)"""

result = mt.reverseTransform(platformBase, platformMoving, 2000, (1300, 1300, 1300, 1300, 1300, 1300))
result.printAll()
#mt.printValues(lengths)
