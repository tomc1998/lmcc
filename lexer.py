import fsm
import token

# Call methods on the fsm passed in to set up the correct states.
def __init_states(machine):
   # Create states
  start      = fsm.FSMState(False)
  identifier = fsm.FSMState(False)
  plus       = fsm.FSMState(False)
  minus      = fsm.FSMState(False)
  equals     = fsm.FSMState(False)
  number     = fsm.FSMState(False)
  separator  = fsm.FSMState(True)
  error      = fsm.FSMState(True)

# Keyword states 
  keyword_i   = fsm.FSMState(False)
  keyword_in  = fsm.FSMState(False)
  keyword_o   = fsm.FSMState(False)
  keyword_ou  = fsm.FSMState(False)
  keyword_out = fsm.FSMState(False)
  keyword_l   = fsm.FSMState(False)
  keyword_le  = fsm.FSMState(False)
  keyword_let = fsm.FSMState(False)

# Add states to FSM
  machine.add_start_state(start)
  machine.add_state(identifier)
  machine.add_state(plus)
  machine.add_state(minus)
  machine.add_state(equals)
  machine.add_state(number)
  machine.add_state(separator)
  machine.add_state(error)
  machine.add_state(keyword_i)
  machine.add_state(keyword_in)
  machine.add_state(keyword_o)
  machine.add_state(keyword_ou)
  machine.add_state(keyword_out)
  machine.add_state(keyword_l)
  machine.add_state(keyword_le)
  machine.add_state(keyword_let)

# Insert paths
  Digit = r"[0-9]"
  Letter = r"[A-Za-z]"
  Whitespace = r"\s"

# start
  start.paths.append(fsm.FSMStatePath(Digit, None, number))
  start.paths.append(fsm.FSMStatePath(Whitespace, None, start))
  start.paths.append(fsm.FSMStatePath("i", None, keyword_i))
  start.paths.append(fsm.FSMStatePath("o", None, keyword_o))
  start.paths.append(fsm.FSMStatePath("l", None, keyword_l))
  start.paths.append(fsm.FSMStatePath("\+", None, plus))
  start.paths.append(fsm.FSMStatePath("-", None, minus))
  start.paths.append(fsm.FSMStatePath("=", None, equals))
  start.paths.append(fsm.FSMStatePath(";", None, separator))
  start.paths.append(fsm.FSMStatePath(Letter, None, identifier))

# identifier
  identifier.paths.append(fsm.FSMStatePath(Letter, None, identifier))
  identifier.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  identifier.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  identifier.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  identifier.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  identifier.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))

# plus
  plus.paths.append(fsm.FSMStatePath(Letter, token.TokenType.PLUS, identifier))
  plus.paths.append(fsm.FSMStatePath(Digit, token.TokenType.PLUS, number))
  plus.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.PLUS, start))

# minus
  minus.paths.append(fsm.FSMStatePath(Letter, token.TokenType.MINUS, identifier))
  minus.paths.append(fsm.FSMStatePath(Digit, token.TokenType.MINUS, number))
  minus.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.MINUS, start))

# equals
  equals.paths.append(fsm.FSMStatePath(Letter, token.TokenType.EQUALS, identifier))
  equals.paths.append(fsm.FSMStatePath(Digit, token.TokenType.EQUALS, number))
  equals.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.EQUALS, start))

# number
  number.paths.append(fsm.FSMStatePath(Digit, None, number))
  number.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.NUMBER, start))
  number.paths.append(fsm.FSMStatePath("\+", token.TokenType.NUMBER, plus))
  number.paths.append(fsm.FSMStatePath("-", token.TokenType.NUMBER, minus))
  number.paths.append(fsm.FSMStatePath(";", token.TokenType.NUMBER, separator))

# separator
  separator.paths.append(fsm.FSMStatePath(Digit, token.TokenType.SEPARATOR, number))
  separator.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.SEPARATOR, start))
  separator.paths.append(fsm.FSMStatePath("i", token.TokenType.SEPARATOR, keyword_i))
  separator.paths.append(fsm.FSMStatePath("o", token.TokenType.SEPARATOR, keyword_o))
  separator.paths.append(fsm.FSMStatePath("l", token.TokenType.SEPARATOR, keyword_l))
  separator.paths.append(fsm.FSMStatePath("\+", token.TokenType.SEPARATOR, plus))
  separator.paths.append(fsm.FSMStatePath("-", token.TokenType.SEPARATOR, minus))
  separator.paths.append(fsm.FSMStatePath("=", token.TokenType.SEPARATOR, equals))
  separator.paths.append(fsm.FSMStatePath(";", token.TokenType.SEPARATOR, separator))
  separator.paths.append(fsm.FSMStatePath(Letter, token.TokenType.SEPARATOR, identifier))

##############
## KEYWORDS ##
##############
# IN KEYWORD
  keyword_i.paths.append(fsm.FSMStatePath("n", None, keyword_in))
  keyword_i.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_i.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_i.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  keyword_i.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_i.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_i.paths.append(fsm.FSMStatePath(Letter, None, identifier))

  keyword_in.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.KEYWORD, start))
  keyword_in.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_in.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_in.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_in.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_in.paths.append(fsm.FSMStatePath(Letter, None, identifier))
# OUT KEYWORD
  keyword_o.paths.append(fsm.FSMStatePath("u", None, keyword_ou))
  keyword_o.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_o.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_o.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  keyword_o.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_o.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_o.paths.append(fsm.FSMStatePath(Letter, None, identifier))

  keyword_ou.paths.append(fsm.FSMStatePath("t", None, keyword_out))
  keyword_ou.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_ou.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_ou.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  keyword_ou.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_ou.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_ou.paths.append(fsm.FSMStatePath(Letter, None, identifier))

  keyword_out.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.KEYWORD, start))
  keyword_out.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_out.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_out.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_out.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_out.paths.append(fsm.FSMStatePath(Letter, None, identifier))
# LET KEYWORD
  keyword_l.paths.append(fsm.FSMStatePath("e", None, keyword_le))
  keyword_l.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_l.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_l.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  keyword_l.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_l.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_l.paths.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_le.paths.append(fsm.FSMStatePath("t", None, keyword_let))
  keyword_le.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_le.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_le.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.IDENTIFIER, start))
  keyword_le.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_le.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_le.paths.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_let.paths.append(fsm.FSMStatePath(Whitespace, token.TokenType.KEYWORD, start))
  keyword_let.paths.append(fsm.FSMStatePath("\+", token.TokenType.IDENTIFIER, plus))
  keyword_let.paths.append(fsm.FSMStatePath("-", token.TokenType.IDENTIFIER, minus))
  keyword_let.paths.append(fsm.FSMStatePath("=", token.TokenType.IDENTIFIER, equals))
  keyword_let.paths.append(fsm.FSMStatePath(";", token.TokenType.IDENTIFIER, separator))
  keyword_let.paths.append(fsm.FSMStatePath(Letter, None, identifier))

# Restart machine
  machine.restart_machine()

# Converts a program's source code into a list of tokens
def lex(program):
  machine = fsm.FSM()
  __init_states(machine)
  outputs = machine.run(program)
  for output in outputs:
    print("{}\t{}".format(output.lexeme.val, str(output.token_type)))



