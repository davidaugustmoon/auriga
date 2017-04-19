class TestClass:
    def foo(self, bird):
        print(bird)


obj = TestClass()
meth_ptr = obj.foo
func_ptr = TestClass.foo

print("obj.foo == TestClass.foo? ", meth_ptr == func_ptr)
print("obj.foo: ", meth_ptr)
print("TestClass.foo: ", func_ptr)
meth_ptr("albatri")
func_ptr(obj, "albatri2")
