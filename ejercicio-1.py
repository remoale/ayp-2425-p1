from typing import List

def find_words(words: List[str]) -> List[str]:
  pass

def main():
  assert find_words(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
  print('1-pass')
  assert find_words(["omk"]) == []
  print('2-pass')
  assert find_words(["adsdf", "sfd"]) == ["adsdf", "sfd"]
  print('3-pass')
  print('ok')

main()

