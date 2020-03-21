#!/usr/bin/pypy

import mathematics as mt
import time

platformBase = mt.Base(2000, 100)
platformMoving = mt.Platform(1600, 100, 100)

givenLengths = (1300, 1300, 1300, 1300, 1300, 1320)
print('Calculate plane for given lengths: {}'.format(givenLengths))

timeStart = time.time()

result = mt.inverseTransform(platformBase, platformMoving, givenLengths, 8, 4)

timeStop = time.time() - timeStart

print('Result is:')

result.printAll()

print('Calculated in {} seconds'.format(timeStop))
print('Checking if calculation is correct...')

platformMoving.transform(result)
lengths = mt.calculateLength(platformBase, platformMoving)

print()

print('Now try reversed:')

destPlane = mt.Plane((100, 45, -1200), (0.1, 0.2, 0.1))

print('Given plane is:')
destPlane.printAll()

platformMoving.transform(destPlane)

lengths = mt.calculateLength(platformBase, platformMoving)

print('Inverse transform:')
inversedPlane2 = mt.inverseTransform(platformBase, platformMoving, lengths, 8, 4)
inversedPlane2.printAll()
