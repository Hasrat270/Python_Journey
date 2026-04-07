import re

text = "Roll No: CS-105"

match = re.search(r"([A-Z]{2})-(\d{3})", text)
# r mtlb text ko exact aisa hi treat kro
# Example WITHOUT r: match = re.search("([A-Z]{2})-(\\d{3})", "CS-105")
# 2 \\ lagany prh rahe

if match:
    print(match.group(0)) # full match by default
    print(match.group(1)) # ([A-Z]{2}) sirf iska match
    print(match.group(2)) # (\d{3}) sirf iska match
else:
    print("No Match")