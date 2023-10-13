#!/usr/bin/python3

"""This module contains a class Rectangle
    that defines a rectangle by: (based on 5-rectangle.py)
"""


class Rectangle:
    """This class defines a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init the rectangle and Incremented the variable
            number_of_instances during each new instance
            instantiation.

        Keyword Arguments:
            width (int) -- width (default: {0})
            height (int) -- height (default: {0})
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Returns the rectangle width.

        Returns:
            Int -- width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the rectangle width subject to certain conditions.

        Arguments:
            value (int) -- value of rectangle width.

        Raises:
            TypeError: width must be an integer.
            TypeError: width must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the rectangle height.

        Returns:
            Int -- height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the rectangle height subject to certain conditions.

        Arguments:
            value (int) -- value of rectangle height.

        Raises:
            TypeError: height must be an integer.
            TypeError: height must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle.

        Returns:
            Int -- area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle
            subject to certain conditions.

        Returns:
            Int -- perimeter of the rectangle.
        """
        if 0 in [self.__height, self.__width]:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str -- representation of the rectangle.
        """
        rectangle = ""
        if 0 not in [self.__width, self.__height]:
            for i in range(self.__height):
                if i == self.__height-1:
                    rectangle += "#" * self.__width
                else:
                    rectangle += "#" * self.__width + "\n"
        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle to be able to
            recreate a new instance by using eval().

        Returns:
            str -- representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted and
            decremented a variable number_of_instances during each instance
            deletion.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
