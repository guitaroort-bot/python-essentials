def is_year_leap(year):
    result = None
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = True
    else:
        result = False
    return result

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

is_year_leap(yr)

