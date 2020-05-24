package main

import (
  "fmt"
  "reflect"
  "strconv"
)

func main() {
  var i int64 = -654
  fmt.Println(reflect.TypeOf(i))
  fmt.Println(i)

  var s string = strconv.FormatInt(i, 10)
  fmt.Println(reflect.TypeOf(s))
  fmt.Println(s)
}
