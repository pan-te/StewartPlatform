# coding=utf-8
#Zestaw narzędzi do transformacji
#(C)by Daniel Sadlik
#2020

import math

sqrt3 = math.sqrt(3)


class Matrix3:
	def __init__(self,coordinates):
		self.row1 = coordinates[0]
		self.row2 = coordinates[1]
		self.row3 = coordinates[2]
		
	def printAll(self):
		print(self.row1)
		print(self.row2)
		print(self.row3)
		

class Vector:
	def __init__(self, coordinates):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.z = coordinates[2]
		
	def printAll(self):
		print('[{};\n {};\n {}]'.format(self.x, self.y, self.z))

	def add(vector1, vector2):
		return Vector((vector1.x + vector2.x, vector1.y + vector2.y, vector1.z + vector2.z))

	def sub(vector1, vector2):
		return Vector((vector1.x - vector2.x, vector1.y - vector2.y, vector1.z - vector2.z))
		
		
def multiplyMatrix3ByVector(matrix3, vector):
		result_x = matrix3.row1[0] * vector.x + matrix3.row1[1] * vector.y + matrix3.row1[2] * vector.z
		result_y = matrix3.row2[0] * vector.x + matrix3.row2[1] * vector.y + matrix3.row2[2] * vector.z
		result_z = matrix3.row3[0] * vector.x + matrix3.row3[1] * vector.y + matrix3.row3[2] * vector.z
		return Vector((result_x, result_y, result_z));
		

class Plane:
	def __init__(self, pos, rot):
		self.position = Vector(pos)
		self.rotation = Vector(rot)
		
	def printAll(self):
		self.position.printAll()
		self.rotation.printAll()		
		
class Platform:
	def __init__(self, dim_a, dim_b, thickness):
		self.jackVector = [None] * 6
		self.jackVectorRotated = [None] * 6
		self.jackVectorTransformed = [None] * 6
		self.jackVector[0] = Vector((-dim_b / 2, (dim_a / 3 - dim_b / 2) * sqrt3, thickness))
		self.jackVector[1] = Vector((dim_b / 2, (dim_a / 3 - dim_b / 2) * sqrt3, thickness))
		self.jackVector[2] = Vector(((dim_a - dim_b) / 2, (-dim_a / 3 + dim_b) * sqrt3 / 2, thickness))
		self.jackVector[3] = Vector((dim_a / 2 - dim_b, -dim_a * sqrt3 / 6, thickness))
		self.jackVector[4] = Vector((dim_b - dim_a / 2, -dim_a * sqrt3 / 6, thickness)) 
		self.jackVector[5] = Vector(((dim_b - dim_a) / 2, (-dim_a / 3 + dim_b) * sqrt3 / 2, thickness))
	
	def createTransformation(self,rotationVector):
		sinphi = math.sin(rotationVector.x)
		cosphi = math.cos(rotationVector.x)
		sinpsi = math.sin(rotationVector.y)
		cospsi = math.cos(rotationVector.y)
		sinthe = math.sin(rotationVector.z)
		costhe = math.cos(rotationVector.z)
		
		row1 = (costhe * cospsi, sinthe * sinphi * cospsi - cosphi * sinpsi, cosphi * sinthe * cospsi + sinphi * sinpsi)
		row2 = (costhe * sinpsi, sinphi * sinthe * sinpsi + cosphi * cospsi, cosphi * sinthe * sinpsi - sinphi * cospsi)
		row3 = (-sinthe, sinphi * costhe, cosphi * costhe)
		
		return Matrix3((row1,row2,row3))
		
	def transform(self, plane):
		transformationMatrix = self.createTransformation(plane.rotation)
		for i in (0, 1, 2, 3, 4, 5):
			self.jackVectorRotated[i] = multiplyMatrix3ByVector(transformationMatrix, self.jackVector[i])
			self.jackVectorTransformed[i] = Vector.add(self.jackVectorRotated[i], plane.position)
			
			
class Base:
	def __init__(self, dim_a, dim_b):
		self.jackOrigin = [None] * 6
		self.jackOrigin[0] = Vector((-dim_a / 2 + dim_b, dim_a * sqrt3 / 6, 0))
		self.jackOrigin[1] = Vector((-dim_b + dim_a / 2, dim_a * sqrt3 / 6, 0)) 
		self.jackOrigin[2] = Vector(((dim_a - dim_b) / 2, (dim_a / 3 - dim_b) * sqrt3 / 2, 0))
		self.jackOrigin[3] = Vector((dim_b / 2, (-dim_a / 3 + dim_b / 2) * sqrt3, 0))
		self.jackOrigin[4] = Vector((-dim_b / 2, (-dim_a / 3 + dim_b / 2) * sqrt3, 0))
		self.jackOrigin[5] = Vector(((-dim_a + dim_b) / 2, (dim_a / 3 - dim_b) * sqrt3 / 2, 0))
		

def calculateLength(origin, destination):
	length = [None] * 6
	lengthValue = [None] * 6
	for i in (0, 1, 2, 3, 4, 5):
		length[i] = Vector.sub(destination.jackVectorTransformed[i],origin.jackOrigin[i])
		lengthValue[i] = (math.sqrt(length[i].x ** 2 + length[i].y ** 2 + length[i].z ** 2))
	return lengthValue
	
def inverseTransform(origin, destination, lengthValue, accuracy, iterations):
	halfXYZ = max(lengthValue) / 2
	bestValues = [[halfXYZ, halfXYZ, -halfXYZ], [0, 0, 0]]
#	accuracy = 8
	positionRange = [None] * 2
	angleRange = [None] * 2
	positionRange[0] = halfXYZ
	positionRange[1] = halfXYZ / accuracy
	angle = 0.5236 #pi/6
	angleRange[0] = angle
	angleRange[1] = angle / accuracy
	for iter in range(iterations):		
		minError = 1000000
		minI = bestValues[0][0] - positionRange[0]
		minJ = bestValues[0][1] - positionRange[0]
		minK = bestValues[0][2] - positionRange[0]
		minL = bestValues[1][0] - angleRange[0]
		minM = bestValues[1][1] - angleRange[0]
		minN = bestValues[1][2] - angleRange[0]
		maxI = bestValues[0][0] + positionRange[0]
		maxJ = bestValues[0][1] + positionRange[0]
		maxK = bestValues[0][2] + positionRange[0]
		maxL = bestValues[1][0] + angleRange[0]
		maxM = bestValues[1][1] + angleRange[0]
		maxN = bestValues[1][2] + angleRange[0]
		i = minI
		while i < maxI:
			j = minJ
			while j < maxJ:
				k = minK
				while k < maxK:
					l = minL
					while l < maxL:
						m = minM
						while m < maxM:
							n = minN
							while n < maxN:
								tempError = 0
								destination.transform(Plane((i,j,k),(l,m,n)))
								calculatedValue = calculateLength(origin, destination)
								for z in range(6):
									tempError += (calculatedValue[z] - lengthValue[z]) ** 2
								if tempError < minError:
									minError = tempError
									bestValues = [[i,j,k],[l,m,n]]
									bestCalcValue = calculatedValue
								n += angleRange[1]
							m += angleRange[1]
						l += angleRange[1]
					k += positionRange[1]
				j += positionRange[1]
			i += positionRange[1]
		print('Iteration no. {} done.'.format(iter))
		positionRange[0] = positionRange[1]
		positionRange[1] /= accuracy / 2
		angleRange[0] = angleRange[1]
		angleRange[1] /= accuracy / 2
	print('Accurate motors combination is: {}\nTotal error: {}'.format(bestCalcValue, minError))
	return Plane(bestValues[0], bestValues[1])
	
def printValues(source):
	for i in source:
		print('{}'.format(i))
