package main

import (
  "fmt"
  "faris-fun/khan-academy/arithmetic"
  "faris-fun/khan-academy/placevalue"
)

func main() {
  //result := arithmetic.Multiply(16, -20)
  //result := arithmetic.Divide(4, 2)
  //result := arithmetic.Add(6, 3)
  //result := arithmetic.Subtract(14, 8)
  result := placevalue.PositionValue(208)
  fmt.Println(result)
}
