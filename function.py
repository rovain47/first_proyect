
def ask_operator():
  ans = input('Please scan serial number').upper()
  if ans[0] == 'F':
    print('Site is foxcon')
  elif ans[0] == 'J':
    print('Site is Jabil')
  else:
    print('Site is not defined')
