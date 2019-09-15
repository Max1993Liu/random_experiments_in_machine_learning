import functools


# decorator with optional arguments
def debug(f=None, *, prefix=''):
	if f is None:
		return functools.partial(debug, prefix=prefix)

	msg = prefix + f.__qualname__
	@functools.wraps(f)
	def wrapper(*args, **kwargs):
		print(msg)
		return f(*args, **kwargs)
	return wrapper


# debug all the methods of a class
def debugmethods(cls):
	for key, val in vars(cls).items():
		if callable(val):
			setattr(cls, key, debug(val))
	return cls


# debug all the classes (using metaclasses)
class debugmeta(type):
	def __new__(cls, clsname, bases, clsdict)
	clsobj = super().__new__(cls, clsname, bases, clsdict)
	clsobj = debugmethods(clsobj)
	return clsobj

# class CrapyCode(metaclass=debugmeta)


