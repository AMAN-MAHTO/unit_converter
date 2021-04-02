p=['Bar','Pascal','Pound per square inch','Standard atmosphere','Torr']

def bar_to_other(num,second_unit):
    if second_unit == p[1]:
        return num*(10**5)
    elif second_unit == p[2]:
        return num*14.504
    elif second_unit == p[3]:
        return num*0.986923
    elif second_unit == p[4]:
        return num*750.062
    else:
        return num

def other_to_bar(num,first_unit):
    if first_unit == p[1]:
        return num/(10**5)
    elif first_unit == p[2]:
        return num/14.504
    elif first_unit == p[3]:
        return num/0.986923
    elif first_unit == p[4]:
        return num/750.062
    else:
        return num

def pressure(num,first_unit,second_unit):
    if first_unit == p[0]:
        return bar_to_other(num,second_unit)
    else:
        return bar_to_other(other_to_bar(num,first_unit),second_unit)

if __name__ == '__main__':
    num = float(input('Enter number: '))
    first_unit = input('Enter number unit: ')
    second_unit = input('Enter in what unit convert: ')
    print(f'{num} {first_unit} = {pressure(num,first_unit,second_unit)} {second_unit}')