t=['Kelvin','Celsius','Fehrenheit']

def list_of_temp_units():
    return t
def celsius_to_other(num,second_unit):
    if second_unit == t[0]:
        return num+273.15
    elif second_unit == t[2]:
        return num*(9/5) + 32

def other_to_celsius(num,first_unit):
    if first_unit == t[0]:
        return num - 273.15
    elif first_unit == t[1]:
         return (num-32)*(5/9)

def temp(num,first_unit,second_unit):
    if first_unit == t[1]:
        return celsius_to_other(num,second_unit)
    else:
        return celsius_to_other(other_to_celsius(num,first_unit),second_unit)

if __name__ == '__main__':
    num = float(input('Enter number: '))
    first_unit = input('Enter number unit: ')
    second_unit = input('Enter in what unit convert: ')
    print(f'{num} {first_unit} = {temp(num,first_unit,second_unit)} {second_unit}')