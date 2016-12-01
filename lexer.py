import fsm

# Call methods on the fsm passed in to set up the correct states.
def __init_states(fsm):
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
  fsm.add_start_state(start)
  fsm.add_state(identifier)
  fsm.add_state(plus)
  fsm.add_state(minus)
  fsm.add_state(equals)
  fsm.add_state(number)
  fsm.add_state(separator)
  fsm.add_state(error)
  fsm.add_state(keyword_i)
  fsm.add_state(keyword_in)
  fsm.add_state(keyword_o)
  fsm.add_state(keyword_ou)
  fsm.add_state(keyword_out)
  fsm.add_state(keyword_l)
  fsm.add_state(keyword_le)
  fsm.add_state(keyword_let)

# Insert rules
  Digit = r"[0-9]"
  Letter = r"[A-Za-z]"
  Whitespace = r"\s"

# start
  start.rules.append(fsm.FSMStatePath(Digit, None, number))
  start.rules.append(fsm.FSMStatePath(Whitespace, None, start))
  start.rules.append(fsm.FSMStatePath("i", None, keyword_i))
  start.rules.append(fsm.FSMStatePath("o", None, keyword_o))
  start.rules.append(fsm.FSMStatePath("l", None, keyword_l))
  start.rules.append(fsm.FSMStatePath("+", None, plus))
  start.rules.append(fsm.FSMStatePath("-", None, minus))
  start.rules.append(fsm.FSMStatePath("=", None, equals))
  start.rules.append(fsm.FSMStatePath(";", None, separator))
  start.rules.append(fsm.FSMStatePath(Letter, None, identifier))

# identifier
  identifier.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  identifier.rules.append(fsm.FSMStatePath("+", "IDENTIFIER", plus))
  identifier.rules.append(fsm.FSMStatePath("-", "IDENTIFIER", minus))
  identifier.rules.append(fsm.FSMStatePath(Whitespace, "IDENTIFIER", start))
  identifier.rules.append(fsm.FSMStatePath("=", "IDENTIFIER", equals))
  identifier.rules.append(fsm.FSMStatePath(";", "IDENTIFIER", separator))

# plus
  plus.rules.append(fsm.FSMStatePath(Letter, "PLUS", identifier))
  plus.rules.append(fsm.FSMStatePath(Digit, "PLUS", number))
  plus.rules.append(fsm.FSMStatePath(Whitespace, "PLUS", start))

# minus
  minus.rules.append(fsm.FSMStatePath(Letter, "MINUS", identifier))
  minus.rules.append(fsm.FSMStatePath(Digit, "MINUS", number))
  minus.rules.append(fsm.FSMStatePath(Whitespace, "MINUS", start))

# equals
  equals.rules.append(fsm.FSMStatePath(Letter, "EQUALS", identifier))
  equals.rules.append(fsm.FSMStatePath(Digit, "EQUALS", number))
  equals.rules.append(fsm.FSMStatePath(Whitespace, "EQUALS", start))

# number
  number.rules.append(fsm.FSMStatePath(Digit, None, number))
  number.rules.append(fsm.FSMStatePath(Whitespace, "NUMBER", start))
  number.rules.append(fsm.FSMStatePath("+", "NUMBER", plus))
  number.rules.append(fsm.FSMStatePath("-", "NUMBER", minus))
  number.rules.append(fsm.FSMStatePath(";", "NUMBER", separator))

# separator
  separator.rules.append(fsm.FSMStatePath(Digit, "SEPARATOR", number))
  separator.rules.append(fsm.FSMStatePath(Whitespace, "SEPARATOR", start))
  separator.rules.append(fsm.FSMStatePath("i", "SEPARATOR", keyword_i))
  separator.rules.append(fsm.FSMStatePath("o", "SEPARATOR", keyword_o))
  separator.rules.append(fsm.FSMStatePath("l", "SEPARATOR", keyword_l))
  separator.rules.append(fsm.FSMStatePath("+", "SEPARATOR", plus))
  separator.rules.append(fsm.FSMStatePath("-", "SEPARATOR", minus))
  separator.rules.append(fsm.FSMStatePath("=", "SEPARATOR", equals))
  separator.rules.append(fsm.FSMStatePath(";", "SEPARATOR", separator))
  separator.rules.append(fsm.FSMStatePath(Letter, "SEPARATOR", identifier))

##############
## KEYWORDS ##
##############
# IN KEYWORD
  keyword_i.rules.append(fsm.FSMStatePath("n", None, keyword_in))
  keyword_i.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_in.rules.append(fsm.FSMStatePath(Whitespace, "KEYWORD", start))
# OUT KEYWORD
  keyword_o.rules.append(fsm.FSMStatePath("u", None, keyword_ou))
  keyword_o.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_ou.rules.append(fsm.FSMStatePath("t", None, keyword_out))
  keyword_ou.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_out.rules.append(fsm.FSMStatePath(Whitespace, "KEYWORD", start))
# LET KEYWORD
  keyword_l.rules.append(fsm.FSMStatePath("e", None, keyword_le))
  keyword_l.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_le.rules.append(fsm.FSMStatePath("t", None, keyword_let))
  keyword_le.rules.append(fsm.FSMStatePath(Letter, None, identifier))
  keyword_let.rules.append(fsm.FSMStatePath(Whitespace, "KEYWORD", start))

# Restart machine
  fsm.restart_machine()

# Converts a program's source code into a list of tokens
def lex(program):
  fsm = fsm.FSM()
  __init_states(fsm)
  print(fsm.run(program))



