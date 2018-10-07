class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # call cb on the root node
    cb(self.value)
    # check if root node node exist
    if self.left:
      # call dfs on the left node
      self.left.depth_first_for_each(cb)
      #check if the node have right node
    if self.right:
      #call dfs on the right node
      self.right.depth_first_for_each(cb)
  def breadth_first_for_each(self, cb):
    #initiate a queue
    queue = []
    #append our root node to the queue
    queue.append(self)
    #loop through our queue and it not empty
    while len(queue):
      # current_node is the first in the list
      current_node = queue.pop(0)
      # check if current_node has a left node
      if current_node.left:
        # append it to the end of the Queue
        queue.append(current_node.left)
      # if current_node has a right node
      if current_node.right:
        # append it to the end of the Queue
        queue.append(current_node.right)
        # call cb on the current_node 
      cb(current_node.value)



  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
