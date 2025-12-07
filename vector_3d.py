import numbers
import math

class Vector3D:    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Unsupported operand type(s) for +: 'Vector3D' and '{}'".format(type(other).__name__))
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Unsupported operand type(s) for -: 'Vector3D' and '{}'".format(type(other).__name__))
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __pow__(self, power):
        if isinstance(power, Vector3D):
            return self.cross_product(power)
        else:
            raise TypeError("Unsupported operand type(s) for **: 'Vector3D' and '{}'".format(type(power).__name__))
    
    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.dot_product(other)
        if isinstance(other, numbers.Number):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector3D' and '{}'".format(type(other).__name__))
        
    def __truediv__(self, scalar):
        if not isinstance(scalar, numbers.Number):
            raise TypeError("Unsupported operand type(s) for /: 'Vector3D' and '{}'".format(type(scalar).__name__))
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __abs__(self):
        return self.magnitude()
    
    def __eq__(self, other):
        if not isinstance(other, Vector3D):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def cross_product(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Unsupported operand type(s) for cross product: 'Vector3D' and '{}'".format(type(other).__name__))
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def dot_product(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Unsupported operand type(s) for dot product: 'Vector3D' and '{}'".format(type(other).__name__))
        return self.x * other.x + self.y * other.y + self.z * other.z
    
if __name__ == "__main__":
    # Example usage of Vector3D
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v3 = Vector3D(1, 2, 3)

    v_sum = v1 + v2
    print("sum:", v_sum) # Output: Vector3D(5, 7, 9)

    v_diff = v1 - v2
    print("diff:", v_diff) # Output: Vector3D(-3, -3, -3)

    v_dot = v1 * v2
    print("dot product:", v_dot) # Output: 32

    v_cross = v1 ** v2
    print("cross product:", v_cross) # Output: Vector3D(-3, 6, -3)

    v_scaled = v1 * 2
    print("scaled:", v_scaled) # Output: Vector3D(2, 4, 6)

    v_divided = v1 / 2
    print("divided:", v_divided) # Output: Vector3D(0.5, 1.0, 1.5)

    v_magnitude = abs(v3)
    print("magnitude:", v_magnitude) # Output: 3.7416573867739413

    v_equality = v1 == v3
    print("equal:", v_equality) # Output: True

    v_equality2 = v1 == v2
    print("equal:", v_equality2) # Output: False