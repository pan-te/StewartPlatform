# coding=utf-8
#Prosty test biblioteki mathematics.py
#(C) Daniel Sadlik
#2020

import mathematics as mt

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

destPlane = mt.Plane((0.0, 0.0, -1000), (0, 0, 0))
platformMoving.transform(destPlane)
lengths = mt.calculateLength(platformBase, platformMoving)

mt.printValues(lengths)