#EXAMPLE
class Numstring:
    def __int__(self, value):
        self.value = str(value)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __add__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

#KEYWORDS

# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other)
# object.__matmul__(self, other)
# object.__truediv__(self, other)
# object.__floordiv__(self, other)
# object.__mod__(self, other)
# object.__divmod__(self, other)
# object.__pow__(self, other[, modulo])
# object.__lshift__(self, other)
# object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method, x.__add__(y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__(). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported.

# If one of those methods does not support the operation with the supplied arguments, it should return NotImplemented.

# object.__radd__(self, other)
# object.__rsub__(self, other)
# object.__rmul__(self, other)
# object.__rmatmul__(self, other)
# object.__rtruediv__(self, other)
# object.__rfloordiv__(self, other)
# object.__rmod__(self, other)
# object.__rdivmod__(self, other)
# object.__rpow__(self, other[, modulo])
# object.__rlshift__(self, other)
# object.__rrshift__(self, other)
# object.__rand__(self, other)
# object.__rxor__(self, other)
# object.__ror__(self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation 3 and the operands are of different types. 4 For instance, to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.

# Note that ternary pow() will not try calling __rpow__() (the coercion rules would become too complicated).

# Note If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different implementation of the reflected method for the operation, this method will be called before the left operand’s non-reflected method. This behavior allows subclasses to override their ancestors’ operations.
# object.__iadd__(self, other)
# object.__isub__(self, other)
# object.__imul__(self, other)
# object.__imatmul__(self, other)
# object.__itruediv__(self, other)
# object.__ifloordiv__(self, other)
# object.__imod__(self, other)
# object.__ipow__(self, other[, modulo])¶
# object.__ilshift__(self, other)
# object.__irshift__(self, other)
# object.__iand__(self, other)
# object.__ixor__(self, other)
# object.__ior__(self, other)
