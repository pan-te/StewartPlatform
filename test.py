#!/usr/bin/python3.8

import mathematics as mt

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

destPlane = mt.Plane((320, 80, -480), (-1.45, -0.82, 0.94))
platformMoving.transform(destPlane)
lengths = mt.calculateLength(platformBase, platformMoving)

for i in lengths:
	print(i)