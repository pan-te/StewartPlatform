# coding=utf-8
#Zestaw narzędzi do transformacji przejściowej
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
		print(self.x)
		print(self.y)
		print(self.z)

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
		for i in range(6):
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
	for i in range(6):
		length[i] = Vector.sub(destination.jackVectorTransformed[i],origin.jackOrigin[i])
		lengthValue[i] = (math.sqrt(length[i].x * length[i].x + length[i].y * length[i].y + length[i].z * length[i].z))
	return lengthValue