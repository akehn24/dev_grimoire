############################################################################
# Regex via re.findall()
# 
# re.findall(<pattern>, string)
#   pattern can be:
#       - string
#       - char class code (/w, /s, /d)
#       - regex symbol ($, |, ^)
#   optional args:
#       - start index value
#       - end index value 
#       - flags, etc.
# 
# re.match() - return first match, stops after
# re.search() - matches anywhere in the string
# 
# [<pattern>] - custom char class
# (<pat)(tern>) - group within the pattern
# 
# '<join chars>'.join() - pulls the list values out and separates by
#                         the specified chars
# 
# Credits: 
#   https://notes.nicolevanderhoeven.com/Regular+Expressions+in+Python
#   https://docs.python.org/3/library/re.html
############################################################################

import re


line = '<!-- # https://youtube.com/watch?v=somethinghere -->'
link = re.findall('<!-- # (.+) -->', line)
print('\nSource: ',''.join(link))

time_string = "Appointment times include 7:00 am, 9:30 am, or 1:00 pm."

# \d = unicode decimal digit
appt_times = re.findall("([\d:.]+) (am|pm)?", time_string)
print(f"\nAppointment Times: {appt_times}")

# double join because the above returns a list of tuples - [('7:00', 'am'), ('9:30', 'am'), ...]
print('Appointment Times: ', ', '.join(' '.join(val) for val in appt_times))
