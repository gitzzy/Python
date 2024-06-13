import re

players = "The rain mainly rains in spain in plains"
match = re.search(r"\ain\b",players)
if match:
    print("Found : ",match.group())
else:
    print("No result found")

matches = re.findall(r"\spani\b",players)
print(matches)

sub1 = re.sub(r"ain","123",players)
print(sub1)