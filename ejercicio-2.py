from typing import List

def find_peaks(mountain: List[int]) -> List[int]:
  result = []
  if 3 <= len(mountain) <= 100:
    for i in range(len(mountain))[1:-1]:
      if 1 <= mountain[i] <= 100:
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
          result.append(i)
  return result

def main():

  assert find_peaks([2,4,4]) == []
  print('1-pass')
  assert find_peaks([1,4,3,8,5]) == [1,3]
  print('2-pass')
  print('ok')

main()
