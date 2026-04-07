import re

text = "Roll No: CSS-105"

match = re.search(r"([A-Z]{2})-(\d{3})", text)

if match:
    print(match.group(0)) # full match by default
    print(match.group(1)) # ([A-Z]{2}) sirf iska match
    print(match.group(2)) # (\d{3}) sirf iska match
else:
    print("No Match")