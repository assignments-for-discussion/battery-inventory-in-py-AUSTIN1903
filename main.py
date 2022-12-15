
def count_batteries_by_usage(counts):
  for c in counts:
    if(c<310):
       print("lowCount=",lc++) 
    elseif(c>=310&&c<=929):
       print("mediumCount=",mc++)
    else(c>=930):
      print("highCount++",hc++)
  return {
    "lowCount",
    "mediumCount",
    "highCount"
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  #assert(counts["lowCount"] == 2)
  #assert(counts["mediumCount"] == 3)
  #assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
