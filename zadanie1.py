def generate_postal_codes(start_code, end_code):
    #zamiana tekstu na liczby całkowite
    start = int(start_code.replace("-", ""))
    end = int(end_code.replace("-", ""))

    #lista dla wygwnrowanych kodów pocztowych
    postal_codes = []

    #generowanie kodów pocztowych w podanym zakresie
    for code in range(start, end + 1):
        #zapisanie kodu w formacie xx-xxx
        formatted_code = f"{str(code)[:2]}-{str(code)[2:]}"
        postal_codes.append(formatted_code)

    return postal_codes

#przykład
start_code = "79-900"
end_code = "80-155"
postal_codes = generate_postal_codes(start_code, end_code)
print(postal_codes)