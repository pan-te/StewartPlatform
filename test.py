#!/usr/bin/python3.8

import mathematics as mt

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

givenLengths = (1300, 1300, 1300, 1300, 1300, 1300)
print(f'Calculate plane for given lengths: {givenLengths}')
result = mt.inverseTransform(platformBase, platformMoving, givenLengths)

print('Result is:')
result.printAll()

print('Checking if calculation is correct...')

platformMoving.transform(result)
lengths = mt.calculateLength(platformBase, platformMoving)

print(f'Result is: {lengths}')
print()

print('Now try reversed:')

destPlane = mt.Plane((100, 45, -1200), (0.1, 0.2, 0.1))

print('Given plane is:')
destPlane.printAll()

platformMoving.transform(destPlane)

lengths = mt.calculateLength(platformBase, platformMoving)

print(f'Lengths are: {lengths}')
print('Inverse transform:')
inversedPlane2 = mt.inverseTransform(platformBase, platformMoving, lengths)
inversedPlane2.printAll()

