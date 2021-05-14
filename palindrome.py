def check_pal():
    string = input("Enter a string: ")
    if not string:
        return "empty"
    else:
        reverse = string[::-1]
        if string == reverse:
            return "yes"
        else:
            return "no"


