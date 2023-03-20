def isValid(s):
      my_stack = []
      for c in s:
          if c in "([{":
              my_stack.append(c)
          if c in ")]}":
              if (len(my_stack) == 0):
                  return False
              last = my_stack.pop()
              if (last + c) not in ["()", "[]", "{}"]:
                  return False
      return not (len(my_stack) > 0)
