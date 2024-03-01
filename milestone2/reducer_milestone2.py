#!/home/bigdata/anaconda3/bin/python
import sys

result = {
  "Atlanta": {
    "price": 0,
    "item": ''
  },
  "Miami": {
    "price": 0,
    "item": ''
  },
  "San Francisco": {
    "price": 0,
    "item": ''
  }
}

for line in sys.stdin:
  data = line.strip().split("\t")
  store, price, item = data
  if len(data) == 3:
    # Check if store is Atlanta, Miami, or San Francisco
    if store == "Atlanta":
      # Check if price is greater than current price
      if result["Atlanta"]["price"] < float(price):
        result["Atlanta"]["price"] = float(price)
        result["Atlanta"]["item"] = item
    elif store == "Miami":
      # Check if price is greater than current price
      if result["Miami"]["price"] < float(price):
        result["Miami"]["price"] = float(price)
        result["Miami"]["item"] = item
    elif store == "San Francisco":
      # Check if price is greater than current price
      if result["San Francisco"]["price"] < float(price):
        result["San Francisco"]["price"] = float(price)
        result["San Francisco"]["item"] = item

for store in result:
  print("{0}\t{1}\t{2}".format(store, result[store]["price"], result[store]["item"]))