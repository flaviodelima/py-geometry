import numbers
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Unsupported operand type(s) for +: 'Vector2D' and '{}'".format(type(other).__name__))
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Unsupported operand type(s) for -: 'Vector2D' and '{}'".format(type(other).__name__))
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.dot_product(other)
        if self._is_number(other):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector2D' and '{}'".format(type(other).__name__))
        
    def __pow__(self, power):
        if isinstance(power, Vector2D):
            # this is notation abused for cross product in 2D
            return self.cross_product(power)
        if self._is_number(power):
            return Vector2D(self.x ** power, self.y ** power)
        else:
            raise TypeError("Unsupported operand type(s) for **: 'Vector2D' and '{}'".format(type(power).__name__))
    
    def __truediv__(self, scalar):
        if not self._is_number(scalar):
            raise TypeError("Unsupported operand type(s) for /: 'Vector2D' and '{}'".format(type(scalar).__name__))
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def __abs__(self):
        return self.magnitude()

    def _is_number(self, value):
        return isinstance(value, numbers.Number) and \
            not isinstance(value, bool) and \
            not math.isnan(value) and \
            value != complex('nan')

    def cross_product(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Unsupported operand type(s) for cross product: 'Vector2D' and '{}'".format(type(other).__name__))
        return self.x * other.y - self.y * other.x

    def dot_product(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError("Unsupported operand type(s) for dot product: 'Vector2D' and '{}'".format(type(other).__name__))
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    
if __name__ == "__main__":
    # Example usage
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)
    v3 = Vector2D(3, 4)
    v4 = Vector2D(2, 3)

    v_sum = v1 + v2
    print("sum:", v_sum) # Output: Vector2D(6, 8)

    v_diff = v1 - v2
    print("diff:", v_diff) # Output: Vector2D(-2, -2)

    v_dot = v1 * v2
    print("dot product:", v_dot) # Output: 23

    v_cross = v1 ** v2
    print("cross product:", v_cross) # Output: -2

    v_scaled = v1 * 2
    print("scaled:", v_scaled) # Output: Vector2D(4, 6)

    v_divided = v1 / 2
    print("divided:", v_divided) # Output: Vector2D(1.0, 1.5)

    v_magnitude = abs(v3)
    print("magnitude:", v_magnitude) # Output: 5.0

    v_equality = v1 == v3
    print("equal:", v_equality) # Output: False

    v_equality2 = v1 == v4
    print("equal:", v_equality2) # Output: True
    