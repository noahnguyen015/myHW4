class Base:
  def __init__(self, x, size):
    self.x = x
    self.size = size

class Circle(Base):
  def __init__(self, x, y, size):
      super().__init__(x, size)
      self.y = y

  def shape(self):
      return 'This is a circle'
  def draw(self):
      return f"""
      ({self.x}, {self.y})\n{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """

  
#def main():
#  s = Circle(1,2,3)
#  print(s.shape())
#  print(s.draw())

#main()
