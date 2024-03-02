#!/home/bigdata/anaconda3/bin/python
import sys

result = {
  "09:01-10:00": 0,
  "10:01-11:00": 0
}

for line in sys.stdin:
  data = line.strip().split("\t")
  time = data[0]
  if len(data) == 1:
    # Check if time is between 09:01-10:00
    if time >= "09:01" and time <= "10:00":
      result["09:01-10:00"] += 1
    # Check if time is between 10:01-11:00
    elif time >= "10:01" and time <= "11:00":
      result["10:01-11:00"] += 1

for time in result:
  print("{0}\t{1}".format(time, result[time]))