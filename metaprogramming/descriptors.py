# Descriptors are used to create customized processing
# of attribute access
# The gist:

class Descriptor:
	def __init__(self, name=None):
		self.name = name
	def __get__(self, instance, cls):
		...
	def __set__(self, instance, value):
		...
	def __delete__(self, instance):
		...


# A descriptor is intercepting the calls to the dot operations
# Example: A normal descriptor
class Field:
	def __init__(self, name=None):
		self.name = name

	def __set__(self, instance, value):
		instance.__dict__[self.name] = value

	def __get__(self, instance, cls):
		return instance.__dict__[self.name]

	def __delete__(self, instance):
		del instance.__dict__[self.name]

class A:
	a = Field('a')


# Type checking with descriptors
class Typed(Field):
	ty = object    # expected type
	def __set__(self, instance, value):
		if not isinstance(value, self.ty):
			raise TypeError('Expected {}'.format(self.ty))
		super().__set__(instance, value)

class Integer(Type):
	ty = int

class Float(Typed):
	ty = float

class String(Typed):
	ty = float

class Positive(Field):
	def __set__(self, instance, value):
		if value < 0:
			raise ValueError('Must be >= 0')
		super().__set__(instance, value)

class PositiveInteger(Integer, Positive):
	pass
