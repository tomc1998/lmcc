import re
import lexeme
import token

class MultipleStartStatesError(Exception):
  pass

class StateNotDefinedError(Exception):
  pass


class FSMStatePath:
  def __init__(self, rule, output, resultState):
    self.rule = rule
    self.output = output
    self.resultState = resultState

class FSMState:
  def __init__(self, is_final):
    # paths is an array of FSMStatePaths.
    self.paths = []
    self.is_final = is_final

# Gets the path associated with the str token given, or None if not found
  def get_path_from_token(self, token):
    for path in self.paths:
      if (re.match(path.rule, token) != None):
        return path
    return None


    # Make sure to call restart_machine after setting the start state before
# running.
class FSM:
  def __init__(self):
    self.__start_state = None
    self.__states = []
    self.__curr_state = None

  def add_start_state(self, state):
    if (self.__start_state != None):
      raise MultipleStartStatesError("""Only one starting state can \
          be defined per finite state machine.""")
    else:
      self.__start_state = state
      self.__states.append(state)

  def remove_start_state(self):
    self.__states.remove(self.__start_state)
    self.__start_state = None

  def add_state(self, state):
    self.__states.append(state)

# Resets the FSM current state to the starting state
  def restart_machine(self):
    self.__curr_state = self.__start_state

# Step the FSM on 1 char, returns the output of the step, None if no output.
  def step(self, token):
    if (self.__curr_state == None):
      raise StateNotDefinedError("""You need to reset the FSM to a valid state \
          before stepping""")
    elif (len(token) > 1):
      token = token[0]
    print("Token: ", token)
    path = self.__curr_state.get_path_from_token(token)
    if (path == None):
      return "ERROR"
    else:
      self.__curr_state = path.resultState
      return path.output

  def is_final(self):
    if (self.__curr_state == None):
      raise StateNotDefinedError("You need to reset the FSM to a valid state")
    return self.__curr_state.is_final

# Run the FSM on a string until the string ends
  def run(self, tokens):
    outputs = []
    curr_lexeme = lexeme.Lexeme("")
    for c in tokens:
      output = self.step(c)
      if (output != None):
        outputs.append(token.Token(curr_lexeme, output))
        curr_lexeme = lexeme.Lexeme("")
      if (curr_lexeme.val != "" or re.match("\s", c) == None):
        curr_lexeme.val += c;
    return outputs



