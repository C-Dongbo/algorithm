def maxArea(height):
  max_area = 0
  max_r = len(height) - 1
  i = 0
  while(i < max_r):
    max_area = max(max_area, min(height[i], height[max_r]) * (max_r-i))
    if height[i] < height[max_r]:
      i += 1
    else:
      max_r -= 1
  return max_area


if __name__ == '__main__':
  input = [1,8,6,2,5,4,8,3,7]
  print(maxArea(input))