from enum import Enum
import lexeme

class TokenType (Enum):
  IDENTIFIER  = 1
  NUMBER      = 2
# Keywords are: "out", "in", "let"
  KEYWORD     = 3
  PLUS        = 4
  MINUS       = 5
  EQUALS      = 6
  SEPARATOR   = 7
  ERROR       = 8
  
class Token:
  def __init__(self, lexeme, token_type):
    self.lexeme = lexeme
    self.token_type = token_type

