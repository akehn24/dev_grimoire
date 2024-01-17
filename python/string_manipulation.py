############################################################################
# String Manipulation in Python
# 
# Removing Leading/Trailing Characters
# Print First/Last Characters
# Capitalize and Lower Case
############################################################################

print()
### Removing Leading/Trailing Characters ###################################
lead_str = "     Removed the leading spaces."
lead_str = lead_str.lstrip(" ")
print(lead_str)

trail_str = "Removed the trailing spaces.   "
trail_str = trail_str.rstrip(" ")
print(trail_str)

print()
### Print First/Last Characters ###########################################
manip_string = "Parasaurolophus"
print(manip_string[3:])
print(manip_string[6:])
print(manip_string[:3])
print(manip_string[:6])

print()
### Capitalize and Lower Case ##############################################
# Caps
all_caps = "capitalize this string"
all_caps = all_caps.upper()
print(all_caps)

# Lower
all_lower = "UNCAPITALIZE THIS STRING"
all_lower = all_lower.lower()
print(all_lower)

# Title
bactrian_case = "capitalize the first letter of each word"
bactrian_case = bactrian_case.title()
print(bactrian_case)

# Title - Fix Apostrophies
apos_broken = "Message's is broken's"
apos_broken = apos_broken.title()
print("Broken:", apos_broken)

apos_fixed = "Message's is fixed's"
apos_fixed = apos_fixed.title().replace("'S", "'s")
print("Fixed:", apos_fixed)

print()
### Count Length ###########################################################
city_in_wales = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
print(f"The length of {city_in_wales}: {len(city_in_wales)}")

num_of_spaces = "           How many spaces were in the lead?"
no_spaces = num_of_spaces.lstrip(" ")
print(f"{no_spaces} There were {len(num_of_spaces) - len(no_spaces)}.")

print()
############################################################################
