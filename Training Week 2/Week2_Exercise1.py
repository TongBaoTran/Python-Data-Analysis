import re

def integers_in_brackets(x):
      xfilter=re.findall(r'[\d+-]+', x)
      return xfilter

print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43a ]tt [+12]xxx"))


