from typing import List

def find_words(words: List[str]) -> List[str]:
  result = []
  if 1 <= len(words) <= 20:
    for word in words:
      if 1 <= len(word) <= 100:
        rows = {'qwertyuiop': 0, 'asdfghjkl': 0, 'zxcvbnm': 0}
        for char in word.lower():
          if char in 'qwertyuiop':
            rows['qwertyuiop'] += 1
          elif char in 'asdfghjkl':
            rows['asdfghjkl'] += 1
          elif char in 'zxcvbnm':
            rows['zxcvbnm'] += 1
        if (rows['qwertyuiop'] > 0 and rows['asdfghjkl'] == 0 and rows['zxcvbnm'] == 0) or (
        rows['qwertyuiop'] == 0 and rows['asdfghjkl'] > 0 and rows['zxcvbnm'] == 0) or (
        rows['qwertyuiop'] == 0 and rows['asdfghjkl'] == 0 and rows['zxcvbnm'] > 0):
          result.append(word)
  return result

def main():
  assert find_words(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
  print('1-pass')
  assert find_words(["omk"]) == []
  print('2-pass')
  assert find_words(["adsdf", "sfd"]) == ["adsdf", "sfd"]
  print('3-pass')
  print('ok')

main()

