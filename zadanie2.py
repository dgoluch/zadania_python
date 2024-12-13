def find_missing_elements(elements, n):
    #pusta lista dla brakujących elementów
    missing = []
    #iterowanie od 1 do n+1
    for number in range(1, n + 1):
        #jeżeli liczba nie znajdyje się w podanej liście elements, dodawana jest do listy missing
        if number not in elements:
            missing.append(number)
    return missing

#przykład
elements = [2, 3, 7, 4, 9]
n = 10
missing_elements = find_missing_elements(elements, n)
print(missing_elements)