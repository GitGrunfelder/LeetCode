# Given a standard time string such as '07:05:13PM' ,
# return time in military format '19:05:13'

def time_conversion(s):
    if s[:2] == '12' and s[-2:] == 'PM':
        updated = '12:'+s[3:-2]
    elif s[:2] == '12' and s[-2:] == 'AM':
        updated = '00:'+s[3:-2]
    elif 'p' in s.lower():
        updated = str(int(s[0:2]) + 12) + s[2:-2]
    else:
        updated = s[:-2]
    return updated
    
print(time_conversion('12:43:20PM'))

def time_conversion_v2(s):
    if 'p' in s.lower():
        if s[:2] == '12':
            return s[:-2]
        return str(int(s[0:2]) + 12) + (s[2:-2])
    else:
        if s[:2] == '12':
            return '00' + (s[2:-2])
        return s[:-2]

print(time_conversion_v2('12:00:01aM'))
