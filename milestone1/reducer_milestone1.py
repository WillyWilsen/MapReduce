#!/home/bigdata/anaconda3/bin/python
import sys

result = {
  "Consumer Electronics": 0,
  "Toys": 0
}

for line in sys.stdin:
  data = line.strip().split("\t")
  item, price = data
  if len(data) == 2:
    # Check if Consumer Electronics is substring of item
    if "Consumer Electronics" in item:
      result["Consumer Electronics"] += float(price)
    # Check if Toys is substring of item
    elif "Toys" in item:
      result["Toys"] += float(price)

for item in result:
  print("{0}\t{1}".format(item, result[item]))