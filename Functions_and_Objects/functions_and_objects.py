class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

ob = MyClass()
# Output: 10
print(MyClass.a)
print(ob.a)
# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
