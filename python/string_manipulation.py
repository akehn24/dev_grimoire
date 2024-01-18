############################################################################
# String Manipulation in Python
# 
# TOC:
#   Strings are Arrays
#   Multiline Strings
#   Removing Leading/Trailing Characters
#   Capitalize and Lower Case
#   Count Length
#   Start and End of Strings
#   Character Replacement
#   Concatenating Strings
#   Escape Characters
# 
# Credits:
#   Nicole van der Hoeven's Fork My Brain: https://notes.nicolevanderhoeven.com/Fork+My+Brain
#   W3Schools: https://www.w3schools.com/python/python_strings.asp
#   W3Schools List of String Methods: https://www.w3schools.com/python/python_ref_string.asp
############################################################################

print("\nStrings are Arrays:")
### Strings are Arrays ######################################################
string_array = "Strings can be indexed."
print(f"{string_array}: {string_array[1]}")
print(f"{string_array}: {string_array[0:5]}")
print(f"{string_array}: {string_array[5:10]}")
print(f"{string_array} sliced from the start: {string_array[:10]}")
print(f"{string_array} sliced from the end: {string_array[15:]}")
print(f"{string_array} sliced from the start in reverse: {string_array[-10:]}")
print(f"{string_array} sliced from the end in reverse: {string_array[:-5]}")

string_array = "Loop"
for char in string_array:
    print(char)

# check if substring in string
if "oo" in string_array:
    print(f"There are double o's in {string_array}.")
if "ii" not in string_array:
    print(f"There are not double i's in {string_array}.")
############################################################################


print("\nMultiline Strings:")
### Multiline Strings ######################################################
multiline_string = """Use three
double or single quotes
to make multiline
strings."""
print(multiline_string)
############################################################################


print("\nRemoving Leading/Trailing Characters:")
### Removing Leading/Trailing Characters ###################################
lead_str = "     Removed the leading spaces."
lead_str = lead_str.lstrip(" ")
print(lead_str)

trail_str = "Removed the trailing spaces.   "
trail_str = trail_str.rstrip(" ")
print(trail_str)

both_ends = "    Removed the extra spaces from both ends.     "
both_ends = both_ends.strip()
print(both_ends)
############################################################################


print("\nCapitalize and Lower Case:")
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
############################################################################


print("\nCount Length:")
### Count Length ###########################################################
city_in_wales = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
print(f"The length of {city_in_wales}: {len(city_in_wales)}")

num_of_spaces = "           How many spaces were in the lead?"
no_spaces = num_of_spaces.lstrip(" ")
print(f"{no_spaces} There were {len(num_of_spaces) - len(no_spaces)}.")
############################################################################

print("\nStart and End of Strings:")
### Start and End of Strings ###############################################
check_start_end = "Does this string start with a D?"
if check_start_end.startswith("D"):
    print("String starts with the letter D.")

if check_start_end.endswith("A") == False:
    print("String does not end with an A.")

range_string = "Parasaurolophus"
print(f"{range_string[0:8]} ends with saur: {range_string.endswith('saur', 0, 8)}")
print(f"{range_string[8:15]} ends with saur: {range_string.endswith('saur', 8, 15)}")
############################################################################


print("\nCharacter Replacement:")
### Character Replacement ##################################################
dino_string = "Parasaurolophus"
print(dino_string)
firsthalf_dino = dino_string.replace("Para", "Tyrana")
print(firsthalf_dino)
secondhalf_dino = firsthalf_dino.replace("olophus", "us-Rex")
print(secondhalf_dino)
############################################################################


print("\nConcatenating Strings:")
### Concatenating Strings ##################################################
print("Para" + "saur")
print("Para" + " " + "saur")
print("Para", "saur")
print("Para" + str(23), "saur")
para = "Para"
saur = "saur"
num = 23
print(f"There are {num} {para}{saur} at my school.")   # this is more secure than format
print("{0} is a {1} year old {2}.".format(para, num, saur))
############################################################################


print("\nEscape Characters:")
### Escape Characters ######################################################
print("""This is how you use \"double quotes\"
      in your multiline string.""")
escape_chars = """
\'  single quote
\"  double quote
\n  newline
\\  backslash
\r  carriage return
\t  tab
\b  backspace
\f  form feed"""
print(escape_chars)
############################################################################
