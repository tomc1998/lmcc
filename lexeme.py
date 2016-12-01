from enum import Enum

class LexemeType (Enum):
  IDENTIFIER  = 1
  NUMBER      = 2
# Keywords are: "out", "in", "let"
  KEYWORD     = 3
  PLUS        = 4
  MINUS       = 5
  EQUALS      = 6
  SEPARATOR   = 7
  ERROR       = 8
  
class Lexeme:
  def __init__(self, val):
    self.val = val
    self.type = None

