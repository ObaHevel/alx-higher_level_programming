#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:

    """
    Rectangle Class
    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle object attributes initialization method.
        Args:
            width (int): width of Rectangle.
            heigth (int): heigth of Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter width method.
        Returns:
            width: Private widith attribute value.
        """
        return self.__width

     @width.setter
     def width(self, value):
         """
         Setter width method.
         Args:
         value: width value to be setted.
         Raises:
            TypeError: when width is not a integer.
            ValueError: when width is less than zero.
         """
         if type(value) != int:
             raise TypeError("width must be an integer")
         if value < 0:
             raise ValueError("width must be >= 0")
         self.__width = value

    @property
    def height(self):
         """
         Getter height method.
         Returns:
            height: Private height attribute value.
         """
         return self.__height

     @height.setter
     def height(self, value):
         """
         Setter height method.
         Args:
            value: height value is not an integer.
         Raises:
            TypeError: when height is not an integer.
            value Error: when  height is less than zero.
         """
         if type(value) != int:
             raise TypeError("height must be an integer")
         if value < 0:
             raise valueError("height must be >= 0")
         self._height = value
