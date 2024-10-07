def is_path_crossing(path: str) -> bool:
  location = [0, 0]
  history = {f'{location}': 1}
  if 1 <= len(path) <= 10 ** 4:
    for i in path:
      if i == 'N':
        location[1] += 1
      elif i == 'S':
        location[1] -= 1
      elif i == 'E':
        location[0] += 1
      elif i == 'W':
        location[0] -= 1
      if i in 'NSEW':
        if f'{location}' not in history:
          history[f'{location}'] = 0
        else:
          history[f'{location}'] += 1
    for value in history.values():
      if value > 1:
        return True
  return False
  

def main():

  assert is_path_crossing("NES") == False
  print('1-pass')
  assert is_path_crossing("NESWW") == True
  print('2-pass')
  print('ok')

main()