class ASTNode:
  def __init__(self, val):
    self.val = val
    self.children = [];

class AST:
  def __init__(self):
    self.root = ASTNode("")
