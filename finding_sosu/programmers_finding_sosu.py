from itertools import permutations

def solution(numbers : str):
  num_list = []
  prime_number_cnt = 0
  candi_list = []
  for num in numbers:
    num_list.append(num)
  for i in range(1,len(num_list)+1):
    permute_list = list(permutations(num_list, i))
    for nums in permute_list:
      number = ""
      for num in nums:
        number += num
      if isPrime(int(number)) and int(number) not in candi_list:
        prime_number_cnt += 1
      candi_list.append(int(number))
  return prime_number_cnt




def isPrime(number):
  if number == 0:
    return False
  if number != 1:
    for num in range(2,number):
      if number % num == 0:
        return False
  else:
    return False

  return True


if __name__=='__main__':
  print(solution("011"))
