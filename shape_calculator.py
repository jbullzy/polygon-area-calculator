
# creating object - Rectangle. Methods 'get_area', 'get_perimeter', 'set_width', 
# 'set_height', 'get_diagonal', 'get_picture', 'get_amount_inside'
class Rectangle:

  # Initialization. take two arguments (width, height).
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # Naming of the object. Will return the string shown with the given width and height variables.
  def __str__(self): 
    return f"Rectangle(width={self.width}, height={self.height})"

  # get_area method - returns the area (width * height)
  def get_area(self):
    return (self.width * self.height)
  
  # get_perimeter method - returns the perimeter (width * 2 + height * 2)
  def get_perimeter(self):
    return (self.width * 2 + self.height * 2)
  
  # Takes new width argument and sets it to width
  def set_width(self, newidth):
    self.width = newidth
    return self.__str__ 

  # Same as above but for height
  def set_height(self, newheight):
    self.height = newheight
    return self.__str__

  # Returns the diagonal measurement. ** is the exponential operator. 
  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  # get_picture method. ASCII representation of the rectangle.
  def get_picture(self):
    # prevents shapes over 50 units from being printed.
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ((self.width * "*") + '\n') * self.height
    return picture 

  # get_amount_inside method. Takes another rectangle or square as argument and
  # returns the amount of times it could fit in the initial shape.
  def get_amount_inside(self, other_shape):
    # Floor division (//) returns the integer amount of times the divisor divides the dividend
    width_fit = self.width // other_shape.width
    height_fit = self.height // other_shape.height

    return width_fit * height_fit

# Create the object 'Square' inheriting all the properties from 'Rectangle
class Square(Rectangle):

  # Square will only take 1 argument, the 'side' and asssign it to width and height
  def __init__(self, side):
    self.width = side
    self.height = side

  # Redefining __str__(self) to only display 'side'
  def __str__(self): 
    return f"Square(side={self.width})"

  # Adding 'set__side' method to Square. Resets both width and height
  def set_side(self, newside):
    self.width = newside
    self.height = newside

# rectangle1 = Rectangle(20, 30)

# print(rectangle1.get_picture())

# rectangle1.set_height(10)
# rectangle1.set_width(15)

# print(rectangle1.get_picture())