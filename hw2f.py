import math 
class MathVector:
	

	def __init__(self, args, *other):
		if isinstance(args, list):
			self.values=args
		else:
			if len(other)==0:
				self.values=[0]*args
			else:
				self.values=[args]
				for var in other:
					self.values.append(var)

		
	def get_el(self,num):
		return self.values[num-1]
	
	def neg(self):
		l=[x*(-1)for x in self.values]
		return MathVector(l)

	def mag(self):
		return (math.sqrt(float(sum(map(lambda x:x*x, self.values)))))

	def dot(self, v2):
		return sum(a*b for a,b in zip(self.values,v2.values))

	def plus(self, v2):
		return MathVector([sum(x) for x in zip (self.values,v2.values)])

	def sp(self, scal):
		return MathVector([x*scal for x in self.values])
	

	def print_me(self):
		print self.values

		# [ ], -(negation), abs(for magnitude), *, +, *, and print

	def __neg__(self):
		return self.neg()

	def __abs__(self):
		return self.mag()

	def __add__(self,other):
		return self.plus(other)
	
	def __mul__(self,other):
		if isinstance(other,MathVector):
			return self.dot(other)
		else: 
			return self.sp(other)

	__rmul__=__mul__

	def __getitem__(self,other):
		return self.get_el(other)

	def __str__(self):
		return str(self.values)



u = MathVector(5)
print "u =",
u.print_me()

v = MathVector([2,3, 6])
print "v =",
v.print_me()
 
w = MathVector(1,2,3)
print "w =",
w.print_me()
 
print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()
 
print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v