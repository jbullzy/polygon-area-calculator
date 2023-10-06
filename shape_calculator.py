class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self): 
    return f"Rectangle(width={self.width}, height={self.height})"

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (self.width * 2 + self.height * 2)

  def set_width(self, newidth):
    self.width = newidth
    return self.__str__ 

  def set_height(self, newheight):
    self.height = newheight
    return f"{self.__str__} (width = {self.width} height = {self.height}"

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ((self.width * "*") + '\n') * self.height
    return picture 

  def get_amount_inside(self, other_shape):
    width_fit = self.width // other_shape.width
    height_fit = self.height // other_shape.height

    return width_fit * height_fit


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self): 
    return f"Square(side={self.width})"

  def set_side(self, newside):
    self.width = newside
    self.height = newside
