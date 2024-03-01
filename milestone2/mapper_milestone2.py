#!/home/bigdata/anaconda3/bin/python
import sys

for line in sys.stdin:
  data = line.strip().split("\t")
  date, time, store, item, price, payment = data
  if len(data) == 6:
    print("{0}\t{1}\t{2}".format(store, price, item))