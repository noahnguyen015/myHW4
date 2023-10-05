class Base:
  def __init__(self, x, size):
    self.x = x
    self.size = size


class Circle(Base):
  def __init__(self, x, y, size):
      super().__init__(x, size)
      self.y = y

  def shape(self):
      return print('this is a circle')
  def draw(self):
      return print(f"""({self.x},{self.y}) 
{self.size}
          , - ~ ~ ~ - ,
      , '                ' ,
    ,                        ,
   ,                          ,
  ,                            ,
  ,                            ,
  ,                            ,
  ,                            ,
   ,                          ,
    ,                        ,  
      ,                   , '
        ' - ,  _ _ _  , '
                """)
  
def main():
  s = Circle(2,2,1)
  s.shape()
  s.draw()

main()