# from django.shortcuts import render
from django.http import JsonResponse
from .models import Asserted_Pesels

# Create your views here.
invalidmonths = {'13', '14', '15', '16', '17', '18', '19', '20',
                 '33', '34', '35', '36', '37', '38', '39', '40',
                 '53', '54', '55', '56', '57', '58', '59', '60',
                 '73', '74', '75', '76', '77', '78', '79', '80',
                 '93', '94', '94', '96', '97', '98', '99', '00'}


def display_message(request):
    return JsonResponse({'MESSAGE': 'This is Rafal\'s final project for postgraduate \'Python Developer\' studies.'})


def validate_pesel(request):
    peseltovalidate = request.GET.get('pesel', None)
    validation_result = True
    if len(peseltovalidate) == 11 and str(peseltovalidate).isnumeric():
        if str(peseltovalidate)[2:4] in invalidmonths:
            validation_result = False
        else:
            splittedpesel = tuple(peseltovalidate)
            controldigit = 10 - ((int(splittedpesel[0]) * 1 % 10) + (int(splittedpesel[1]) * 3 % 10) +
                                 (int(splittedpesel[2]) * 7 % 10) + (int(splittedpesel[3]) * 9 % 10) +
                                 (int(splittedpesel[4]) * 1 % 10) + (int(splittedpesel[5]) * 3 % 10) +
                                 (int(splittedpesel[6]) * 7 % 10) + (int(splittedpesel[7]) * 9 % 10) +
                                 (int(splittedpesel[8]) * 1 % 10) + (int(splittedpesel[9]) * 3 % 10)) % 10
            if controldigit != int(splittedpesel[10]):
                validation_result = False
        return JsonResponse({'PESEL': peseltovalidate, 'result': validation_result})
    else:
        return JsonResponse({'PESEL': peseltovalidate, 'result': False, 'MESSAGE': 'Pesel must be exactly 11 digits '
                                                                                   'long.'}, status=400)


def list_asserted_pesels(request):
    assertions = Asserted_Pesels.objects.all()
    data = list(assertions.values('stamp', 'pesel', 'assertion_result'))
    return JsonResponse({'Asserted PESELs': data})
