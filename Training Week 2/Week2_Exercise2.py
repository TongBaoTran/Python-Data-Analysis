import re
def file_listing(filename):
  with open(filename) as f:
    array = []
    lines = f.read().splitlines()
    for line in lines:
        """Create tuples here"""
        """line = re.sub(":",' ', line)"""
        line=re.split(' +',re.sub(":",' ', line))
        del line[0:4]
        line=tuple(line)
        array.append(line)
  return array

filename="listing.txt"
print(file_listing(filename))