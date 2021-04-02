d=['Bit','Byte','Kilobyte','Megabyte','Gigabyte','Terabyte','Petabyte','Exabyte','Zettabyte','Yottabyte',]

# ,first_unit

def other_to_bit(num,second_unit):
    if second_unit == d[1]:
        return num*8
    elif second_unit == d[2]:
        return num*8*1024
    elif second_unit == d[3]:
        return num*8*1024*1024
    elif second_unit == d[4]:
        return num*8*1024*1024*1024
    elif second_unit == d[5]:
        return num*8*1024*1024*1024*1024
    elif second_unit == d[6]:
        return num*8*1024*1024*1024*1024*1024
    elif second_unit == d[7]:
        return num*8*1024*1024*1024*1024*1024*1024
    elif second_unit == d[8]:
        return num*8*1024*1024*1024*1024*1024*1024*1024
    elif second_unit == d[9]:
        return num*8*1024*1024*1024*1024*1024*1024*1024*1024

print(other_to_bit(4,d[6]))
