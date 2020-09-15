package arithmetic

func Add(nums ...float64) float64 {
  total := 0.0
  for _, num := range nums {
    total += num
  }
  return total
}

func Subtract(nums ...float64) float64 {
  total := nums[0]
  for i, num := range nums {
    if i == 0 {
      continue
    } else {
    total -= num
    }
  }
  return total
}

func Multiply(nums ...float64) float64 {
  total := nums[0]
  for i, num := range nums {
    if i == 0 {
      continue
    } else {
      total *= num
    }
  }
  return total
}

func Divide(nums ...float64) float64 {
  total := nums[0]
  for i, num := range nums {
    if i == 0 {
      continue
    } else {
      total /= num
    }
  }
  return total
}
