from VectorClass.Error import InvalidOperationError
from fractionalClass.RationalFraction import RationalFraction


class Vector:

    def __init__(self, list_objects):
        self.list_objects = list_objects

    def __str__(self):
        return "{" + ", ".join([obj.__str__() for obj in self.list_objects]) + "}"

    def __len__(self):
        return len(self.list_objects)

    @staticmethod
    def check_instance(current, other):
        if isinstance(other, Vector):

            if len(current) != len(other):
                raise ValueError("The vectors have different lengths.")

            for obj in other.list_objects:
                if not (isinstance(obj, RationalFraction)):
                    raise ValueError(
                        "One of the objects is not a RationFraction class.")
            return "vector"

        elif isinstance(other, RationalFraction):
            return "const"

        else:
            raise ValueError(
                "The operand must be a list of RationalFraction objects or a RationalFraction object.")

    @staticmethod
    def create_result(result):
        if isinstance(result, list):
            return " ".join([obj.__str__() for obj in result])
        else:
            return result.__str__()

    def __add__(self, other):

        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            return Vector([self.list_objects[i] + other.list_objects[i]
                           for i in range(len(self.list_objects))])
        elif check_obj == "const":
            return Vector([self.list_objects[i] +
                           other for i in range(len(self.list_objects))])

    __radd__ = __add__

    def __sub__(self, other):
        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            return Vector([self.list_objects[i] - other.list_objects[i]
                           for i in range(len(self.list_objects))])
        elif check_obj == "const":
            return Vector([self.list_objects[i] -
                           other for i in range(len(self.list_objects))])

    def __rsub__(self, other):
        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            return Vector([other.list_objects[i] - self.list_objects[i]
                           for i in range(len(self.list_objects))])
        elif check_obj == "const":
            try:
                raise InvalidOperationError
            except InvalidOperationError as e:
                return e

    def __mul__(self, other):
        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            list_mul = [self.list_objects[i] * other.list_objects[i]
                        for i in range(len(self.list_objects))]
            result = RationalFraction("0")
            for obj in list_mul:
                result = result + obj
            return result
        elif check_obj == "const":
            return Vector([self.list_objects[i] *
                           other for i in range(len(self.list_objects))])

    __rmul__ = __mul__

    def __truediv__(self, other):
        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            list_mul = [self.list_objects[i] / other.list_objects[i]
                        for i in range(len(self.list_objects))]
            result = list_mul[0].__str__()
            for obj in list_mul:
                if result != obj.__str__():
                    try:
                        raise InvalidOperationError
                    except InvalidOperationError as e:
                        return e
            return result
        elif check_obj == "const":
            return Vector([self.list_objects[i] /
                           other for i in range(len(self.list_objects))])

    def __rtruediv__(self, other):
        check_obj = Vector.check_instance(self.list_objects, other)
        if check_obj == "vector":
            list_mul = [other.list_objects[i] / self.list_objects[i]
                        for i in range(len(self.list_objects))]
            result = list_mul[0].__str__()
            for obj in list_mul:
                if result != obj.__str__():
                    try:
                        raise InvalidOperationError
                    except InvalidOperationError as e:
                        return e
            return result
        elif check_obj == "const":
            try:
                raise InvalidOperationError
            except InvalidOperationError as e:
                return e
