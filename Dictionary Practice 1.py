# Create a dictionary
# Keys on the left, their associated value is on the right

month_conversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(month_conversions["Nov"])  # Refer to the key, and it will return its value
print(month_conversions.get("FOV", "Not valid key"))
