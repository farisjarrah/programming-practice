package main

import (
  "strconv"
  "fmt"
  "reflect"
)

func main() {
  strVar := "100"
  intVar, _ := strconv.Atoi(strVar)
  fmt.Println(reflect.TypeOf(strVar), reflect.TypeOf(intVar))

  strVar1 := "-52541"
  intVar1, _ := strconv.ParseInt(strVar1, 10, 32)
  fmt.Println(reflect.TypeOf(strVar1), reflect.TypeOf(intVar1))

  strVar2 := "101010101010101010"
  intVar2, _ := strconv.ParseInt(strVar2, 10, 64)
  fmt.Println(reflect.TypeOf(strVar2), reflect.TypeOf(intVar2))
}
