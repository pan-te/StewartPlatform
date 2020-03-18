#!/usr/bin/python3.8

import mathematics as mt

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

destPlane = mt.Plane((0, 0, -1040), (0, 0, 0))
givenLengths = (1300, 1300, 1300, 1300, 1300, 1300)
print(f'Calculate plane for given lengths: {givenLengths}')
result = mt.inverseTransform(platformBase, platformMoving, givenLengths)

print('Result is:')
result.printAll()

print('Checking if calculation is correct...')

platformMoving.transform(result)
lengths = mt.calculateLength(platformBase, platformMoving)

print(f'Result is: {lengths}')
