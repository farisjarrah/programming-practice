// This is the package to name numbers based on what position they are in
// ex: For the number 4321, 1 is in the ones place, 2 is in the tens place,
// 3 is in the hundreds place and 4 is in the thousands place
//package placevalue
//
//import (
//  "fmt"
//  "strconv"
//)
//
//func PositionValue(numInput int) int {
//  var numPositions = map[int]string{
//    0: "ones",
//    1: "tens",
//    2: "hundreds",
//    3: "thousands",
//    4: "ten thousands",
//    5: "hundred thousands",
//    6: "millions",
//    7: "ten millions",
//    8: "hundred millions",
//    9: "billions",
//  }
//  var counter int = 0
//  var numAsString string = strconv.Itoa(numInput)
//  var firstDigit string = string(numAsString[0])
//  var result string
//  if firstDigit == "-" {
//    fmt.Println("This is a negative number")
//    for i := len(numAsString) - 1; i >= 1; i-- {
//       result = numAsString[i] + "is in the" + numPositions[counter] + "position"
//      counter++
//    }
//  } else {
//    for i := len(numAsString) - 1; i >= 0; i-- {
//      result = numAsString[i] + "is in the" + numPositions[counter] + "position"
//      counter++
//    }
//  }
//  return result
//}


package main

import (
  "fmt"
  "strconv"
)

func PositionValue(numInput int) int {
  var numPositions = map[int]string{
    0: "ones",
    1: "tens",
    2: "hundreds",
    3: "thousands",
    4: "ten thousands",
    5: "hundred thousands",
    6: "millions",
    7: "ten millions",
    8: "hundred millions",
    9: "billions",
  }
  var counter int = 0
  var numAsString string = strconv.Itoa(numInput)
  var firstDigit string = string(numAsString[0])
  var result string
  if firstDigit == "-" {
    fmt.Println("This is a negative number")
    for i := len(numAsString) - 1; i >= 1; i-- {
       result = numAsString[i] + "is in the" + numPositions[counter] + "position"
      counter++
    }
  } else {
    for i := len(numAsString) - 1; i >= 0; i-- {
      result = numAsString[i] + "is in the" + numPositions[counter] + "position"
      counter++
    }
  }
  return result
}

func main() {
  fmt.Println(PositionValue(4321))
}
