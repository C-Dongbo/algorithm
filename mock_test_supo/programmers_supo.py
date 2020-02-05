def solution(answers : list):
  first_pattern = [1,2,3,4,5]
  second_pattern = [2,1,2,3,2,4,2,5]
  third_pattern = [3,3,1,1,2,2,4,4,5,5]
  ans_list = []
  idx = 0
  first_cnt, second_cnt, third_cnt = 0, 0, 0
  for ans in answers:
    if ans == first_pattern[idx]:
      first_cnt += 1
    idx += 1
    if idx == len(first_pattern):
      idx = 0
  idx = 0
  for ans in answers:
    if ans == second_pattern[idx]:
      second_cnt += 1
    idx += 1
    if idx == len(second_pattern):
      idx = 0
  idx = 0
  for ans in answers:
    if ans == third_pattern[idx]:
      third_cnt += 1
    idx += 1
    if idx == len(third_pattern):
      idx = 0
  ans_list.append(first_cnt)
  ans_list.append(second_cnt)
  ans_list.append(third_cnt)
  m = max(ans_list)
  return [i+1 for i, j in enumerate(ans_list) if j == m]


if __name__ == '__main__':
  print(solution([1,3,2,4,2]))