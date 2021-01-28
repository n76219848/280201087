class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height

  def get_radius(self):
    return self.radius

  def set_radius(self,radius):
    self.radius = radius

  def get_height(self):
    return self.height

  def set_height(self,height):
    self.height = height
  
  def base_area(self):
    b_area = self.radius**2*3.14
    return b_area

  def surface_area(self):
    s_area = 2*3.14*self.radius*self.height + 2*self.base_area()
    return s_area

  def area(self):
    Area = 2*self.base_area()+self.surface_area()
    return Area

  def Volume(self):
    return self.base_area()*self.height

figure1 = Cylinder(3,5)

print('The area of figure is ',figure1.area())
print('The volume of figure is ', figure1.Volume())
