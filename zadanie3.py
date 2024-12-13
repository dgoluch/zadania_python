from decimal import Decimal

def generate_decimal_list(start, end, step):
    #zamiana liczb na typ decimal
    start = Decimal(start)
    end = Decimal(end)
    step = Decimal(step)

    #wygenerowanie listy liczb z podanego zakresu i danym krokiem 
    result = []
    while start <= end:
        result.append(start)
        start += step

    return result

#przykład 
start = 2
end = 5.5
step = 0.5

decimal_list = generate_decimal_list(start, end, step)
print(decimal_list)