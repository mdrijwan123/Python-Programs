import re

txt = "jemmimiller@gmail.com"

x = re.search(".+@gmail\.com$",txt)
print(x.group())