l=['Kilomater','Meter','Centimeter','Milimeter','Micrometer','Nanometer',
        'Mile','Yard','Foot','Inch','Nactical mile']

def k_t_o(num,second_unit):
    #!1km = 1000m = 100000cm = 1e + 6 mm = 1e+9 um = 1e+12 nm =
    #!0.621371 m = 1093.61 y = 3280.84 f = 39370.1 in = 0.539957 Nm
    if second_unit == l[1]:
        return num*1000
    elif second_unit == l[2]:
        return num*100000
    elif second_unit == l[3]:
        return num*(10**6)
    elif second_unit == l[4]:
        return num*(10**9)
    elif second_unit == l[5]:
        return num*(10**12)
    elif second_unit == l[6]:
        return num*0.621371
    elif second_unit == l[7]:
        return num*1093.61
    elif second_unit == l[8]:
        return num*3280.84
    elif second_unit == l[9]:
        return num*39370.1
    elif second_unit == l[10]:
        return num*0.539957
    else:
        return num
    
def o_t_k(num,first_unit):
    if first_unit == l[1]:
        return num/1000
    elif first_unit == l[2]:
        return num/100000
    elif first_unit == l[3]:
        return num/(10**6)
    elif first_unit == l[4]:
        return num/(10**9)
    elif first_unit == l[5]:
        return num/(10**12)
    elif first_unit == l[6]:
        return num/0.621371
    elif first_unit == l[7]:
        return num/1093.61
    elif first_unit == l[8]:
        return num/3280.84
    elif first_unit == l[9]:
        return num/39370.1
    elif first_unit == l[10]:
        return num/0.539957
    else:
        return num

def length(num,first_unit,second_unit):
    if first_unit == l[0]:
        return k_t_o(num,second_unit)
    else:
        return k_t_o(o_t_k(num,first_unit),second_unit)

if __name__ == '__main__':
    num = float(input('enter number: '))
    first_unit = input('Enter number unit: ')
    second_unit = input('Enter in what unit convert: ')
    print(f'{num} {first_unit} = {length(num,first_unit,second_unit)} {second_unit}')