package main

import (
  "fmt"
  "reflect"
)

const PRODUCT string = "Canada"

const PRICE = 500

func main() {
  fmt.Println(PRODUCT)
  fmt.Println(reflect.TypeOf(PRODUCT))
  fmt.Println(PRICE)
  fmt.Println(reflect.TypeOf(PRICE))
}
