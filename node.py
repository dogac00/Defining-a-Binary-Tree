class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  def insert(self, data):
    if(data < self.data):
      if not self.left:
        self.left = Node(data)
      else:
        self.left.insert(data)
    else:
      if not self.right:
        self.right = Node(data)
      else:
        self.right.insert(data)
        
  def remove(self, data, parent):
    if(data<self.data):
      if(self.left):
        self.left.remove(data, self)
    elif(data>self.data):
      if(self.right):
        self.right.remove(data,self)
    else:
      if(self.left and self.right):
        self.data = self.right.getMin()
        self.right.remove(self.data, self)
      elif(parent.left == self)
        if(self.left):
          temp = self.left
        else:
          temp = self.right
        parent.left = temp
       elif(parent.right==self):
        if(self.left):
          temp=self.left
        else:
          temp=self.right
        parent.right=temp
  
  def getMin(self):
    if(self.left is None):
      return self.data
    else:
      return self.left.getMin()
  
  def getMax(self):
    if(self.right is None):
      return self.data
    else:
      return self.right.getMax()
      
  def traverseInOrder(self):
    if(self.left):
      self.left.traverseInOrder()
    print(self.data)
    if(self.right):
      self.right.traverseInOrder()
