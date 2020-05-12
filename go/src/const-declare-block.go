package main

import (
  "fmt"
  "reflect"
)

const (
  PRODUCT = "Mobile"
  QUANTITY = 50
  PRICE = 50.50
  STOCK = true
)

func main() {
  fmt.Println(QUANTITY)
  fmt.Println(reflect.TypeOf(QUANTITY))
  fmt.Println(PRICE)
  fmt.Println(reflect.TypeOf(PRICE))
  fmt.Println(PRODUCT)
  fmt.Println(reflect.TypeOf(PRODUCT))
  fmt.Println(STOCK)
  fmt.Println(reflect.TypeOf(STOCK))
}
