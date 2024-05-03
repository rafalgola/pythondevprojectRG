invalidmonths = {'13', '14', '15', '16', '17', '18', '19', '20',
                 '33', '34', '35', '36', '37', '38', '39', '40',
                 '53', '54', '55', '56', '57', '58', '59', '60',
                 '73', '74', '75', '76', '77', '78', '79', '80',
                 '93', '94', '94', '96', '97', '98', '99', '00'}

pesel = '76031807079'
pesel2 = '47092306856'
pesel3 = '45092306856'
pesel4 = '45192306856'


def validatepesel(pesel):
    if pesel[2:4] in invalidmonths:
        return False
    splittedpesel = tuple(pesel)
    print(splittedpesel)
    controldigit = 10 - ((int(splittedpesel[0]) * 1 % 10) + (int(splittedpesel[1]) * 3 % 10) +
                         (int(splittedpesel[2]) * 7 % 10) + (int(splittedpesel[3]) * 9 % 10) +
                         (int(splittedpesel[4]) * 1 % 10) + (int(splittedpesel[5]) * 3 % 10) +
                         (int(splittedpesel[6]) * 7 % 10) + (int(splittedpesel[7]) * 9 % 10) +
                         (int(splittedpesel[8]) * 1 % 10) + (int(splittedpesel[9]) * 3 % 10)) % 10

    # print(controldigit)
    if controldigit != int(splittedpesel[10]):
        return False
    return True


print(validatepesel(pesel))
print(validatepesel(pesel2))
print(validatepesel(pesel3))
print(validatepesel(pesel4))
