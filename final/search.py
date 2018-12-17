from django.http import HttpResponse
from django.shortcuts import render_to_response


def search_form(request):
    return render_to_response('final_view.html')


def search(request):
    request.encoding = 'utf-8'
    print(request.GET)
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '1' \
        and request.GET['A2'] == '1'\
        and request.GET['A3'] == '1' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '1' \
        and request.GET['A7'] == '1' \
        and request.GET['A8'] == '1' \
        and request.GET['A9'] == '1' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '1' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '1' \
        and request.GET['A15'] == '1' \
            and request.GET['A16'] == '1':
        message = 'A3,A7,A8'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '6':
        message = 'A11,A13,A14'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '7':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '4':
        message = 'A6,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '6':
        message = 'A11,A13,A14'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '1' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '9' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '9' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '8':
        message = 'A10'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '4':
        message = 'A6'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '9' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '9' \
        and request.GET['A15'] == '9' \
            and request.GET['A16'] == '10':
        message = 'A2,A6,A10,A11,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '1' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '1' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '10' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '10':
        message = 'A4,A5,A10,A11,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '8'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '3' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '3' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '3':
        message = 'A3,A9,A12'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '1' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '4' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '5':
        message = 'A2'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '3' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '3':
        message = 'A2'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '1'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '1':
        message = 'A2'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '8':
        message = 'A5'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '8':
        message = 'A1,A3,A5,A6,A8,A9,A11,A14,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '3'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '5':
        message = 'A3,A6'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '10'\
        and request.GET['earn'] == '6'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '1' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '1' \
        and request.GET['A15'] == '1' \
            and request.GET['A16'] == '1':
        message = 'A1,A7'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '10'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '9' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '5':
        message = 'A2,A3,A7,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '9':
        message = 'A3,A11,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '4':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '6':
        message = 'A6,A9,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '7':
        message = 'A1,A6,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '3'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A5'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '1'\
        and request.GET['A3'] == '3' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '1' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '1' \
            and request.GET['A16'] == '1':
        message = 'A11,A14'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '1'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '1' \
        and request.GET['A8'] == '10' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '1' \
            and request.GET['A16'] == '10':
        message = 'A1,A3,A6,A8,A9,A11,A14,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '4':
        message = 'A6,A8,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A3,A6,A11,A12,A13'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '1' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '6':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '6':
        message = 'A2'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '3'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '5':
        message = 'A3,A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '3'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '5':
        message = 'A3,A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '9' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '8':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '9' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '8':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '6' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '6':
        message = 'A3,A6,A8,A9,A11,A14,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '3':
            message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '0' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A2'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '6':
        message = 'A2,A8,A9'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '7'\
        and request.GET['earn'] == '5'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '2' \
        and request.GET['A5'] == '2' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '3' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '2' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '2':
        message = 'A6,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '0' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A9'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '9' \
        and request.GET['A15'] == '9' \
            and request.GET['A16'] == '8':
        message = 'A2,A8,A11,A13,A14,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '6' \
        and request.GET['job'] == '17'\
        and request.GET['earn'] == '6'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '2' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '4' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '10' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '3':
        message = 'A1,A13'	
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '8':
        message = 'A7'	
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '14'\
        and request.GET['earn'] == '6'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '5':
        message = 'A11'		
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '7':
        message = 'A8,A9'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '10'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '3' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '9' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '8':
        message = 'A12,A13'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '3':
        message = 'A2,A11,A12'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '5'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '3' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '2' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '4':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '7':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '2'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '8':
        message = 'A6,A9,A11,A14,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '2' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '3':
        message = 'A5,A6,A7,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '2'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '8':
        message = 'A6,A9,A11,A14,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '1' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '2' \
        and request.GET['A5'] == '2' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '2' \
        and request.GET['A8'] == '1' \
        and request.GET['A9'] == '1' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '1' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '1' \
        and request.GET['A15'] == '1' \
            and request.GET['A16'] == '1':
        message = 'A2'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '10' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '10' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '9':
        message = 'A1,A4,A6,A7,A12'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '7':
        message = 'A2,A7,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '9':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '5':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '4':
        message = 'A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '10'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '10'\
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '1' \
        and request.GET['A7'] == '1' \
        and request.GET['A8'] == '1' \
        and request.GET['A9'] == '1' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '1' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '10' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '10' \
            and request.GET['A16'] == '10':
        message = 'A1,A2,A3,A4,A13,A14,A15,A16'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '5':
        message = 'A3,A7,A8,A9,A11,A12,A13,A14'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '6':
        message = 'A6,A7,A12,A14,A15'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '3' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '4' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '4':
        message = 'A1,A2,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16'		
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '10' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '10' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '10':
        message = 'A8,A9,A10,A12,A14,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '10' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '7':
        message = 'A1,A4,A6,A7,A9,A10,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '5':
        message = 'A9,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '4':
        message = 'A2,A4,A11,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '2' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '3':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '1' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '9' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '9' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '7':
        message = 'A3,A5,A8,A10,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '2' \
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '10' \
        and request.GET['A13'] == '10' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A3,A6,A12,A13'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A2,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '6':
        message = 'A3,A8,A9,A13'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '6':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '9' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '5':
        message = 'A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '5' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '9' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '10' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '9' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A8'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '4':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '4' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '5'\
        and request.GET['hobbit'] == '5' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '2' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '3':
        message = 'A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '9' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '10' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '10' \
            and request.GET['A16'] == '5':
        message = 'A6,A7,A9,A12,A14,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '8'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '2' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '2' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '3' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '2' \
        and request.GET['A15'] == '2' \
            and request.GET['A16'] == '2':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '9'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '10'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '10' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '2' \
        and request.GET['A10'] == '2' \
        and request.GET['A11'] == '2' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '2' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '10' \
            and request.GET['A16'] == '10':
        message = 'A1,A2,A3,A4,A14,A15,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '4' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '4' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '4':
        message = 'A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '1' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '0' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '3':
        message = 'A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '15'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '2' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '10' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '3':
        message = 'A13'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '20'\
        and request.GET['earn'] == '2'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '10' \
        and request.GET['A6'] == '9' \
        and request.GET['A7'] == '9' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '10' \
        and request.GET['A10'] == '9' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '9' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '9' \
            and request.GET['A16'] == '9':
        message = 'A5,A9,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '10' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A3,A6,A11'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '7' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '10':
        message = 'A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '6' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '5' \
        and request.GET['A15'] == '4' \
            and request.GET['A16'] == '5':
        message = 'A1,A6,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '3' \
        and request.GET['job'] == '16'\
        and request.GET['earn'] == '5'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '3' \
        and request.GET['A13'] == '3' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '3':
        message = 'A3'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '7':
        message = 'A3'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '10'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '8' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '8':
        message = 'A2'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '2'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '2' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '3' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '3' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '5':
        message = 'A11,A13'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '6' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '10' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '10':
        message = 'A3,A10,A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '7' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '8' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '8' \
        and request.GET['A9'] == '8' \
        and request.GET['A10'] == '9' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '9' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '10':
        message = 'A16'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '3'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '5' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '9' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '8' \
        and request.GET['A15'] == '9' \
            and request.GET['A16'] == '6':
        message = 'A3,A11'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '10' \
        and request.GET['A2'] == '9'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '6' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '9' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '8' \
        and request.GET['A14'] == '10' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '8':
        message = 'A1,A3,A11,A14'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '7'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '7' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '7' \
        and request.GET['A9'] == '9' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '8' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A9'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '15'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '3' \
        and request.GET['A1'] == '3' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '5' \
        and request.GET['A4'] == '3' \
        and request.GET['A5'] == '2' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '2' \
        and request.GET['A9'] == '2' \
        and request.GET['A10'] == '2' \
        and request.GET['A11'] == '2' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '3' \
        and request.GET['A15'] == '3' \
            and request.GET['A16'] == '3':
        message = 'A3,A6'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '6'\
        and request.GET['A3'] == '8' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '5' \
        and request.GET['A7'] == '5' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '5' \
        and request.GET['A10'] == '5' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '5' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '5':
        message = 'A3'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '6' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '5' \
        and request.GET['A5'] == '5' \
        and request.GET['A6'] == '9' \
        and request.GET['A7'] == '6' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '9' \
        and request.GET['A13'] == '9' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A12,A13'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '8'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '7' \
        and request.GET['A5'] == '6' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '8' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '7' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '7' \
            and request.GET['A16'] == '7':
        message = 'A3'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '5'\
        and request.GET['A3'] == '9' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '8' \
        and request.GET['A7'] == '7' \
        and request.GET['A8'] == '3' \
        and request.GET['A9'] == '6' \
        and request.GET['A10'] == '6' \
        and request.GET['A11'] == '8' \
        and request.GET['A12'] == '6' \
        and request.GET['A13'] == '6' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A3'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A7'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '19'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '5' \
        and request.GET['A2'] == '4'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '4' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '8' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '6' \
        and request.GET['A12'] == '7' \
        and request.GET['A13'] == '5' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '6' \
            and request.GET['A16'] == '6':
        message = 'A7'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '5' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '2' \
        and request.GET['A1'] == '4' \
        and request.GET['A2'] == '3'\
        and request.GET['A3'] == '2' \
        and request.GET['A4'] == '4' \
        and request.GET['A5'] == '3' \
        and request.GET['A6'] == '4' \
        and request.GET['A7'] == '3' \
        and request.GET['A8'] == '4' \
        and request.GET['A9'] == '4' \
        and request.GET['A10'] == '4' \
        and request.GET['A11'] == '5' \
        and request.GET['A12'] == '4' \
        and request.GET['A13'] == '4' \
        and request.GET['A14'] == '4' \
        and request.GET['A15'] == '5' \
            and request.GET['A16'] == '2':
        message = 'A11,A15'
    if request.GET['sex'] == '1' \
        and request.GET['age'] == '6' \
        and request.GET['job'] == '1'\
        and request.GET['earn'] == '1'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '1' \
        and request.GET['A2'] == '1'\
        and request.GET['A3'] == '10' \
        and request.GET['A4'] == '1' \
        and request.GET['A5'] == '1' \
        and request.GET['A6'] == '1' \
        and request.GET['A7'] == '10' \
        and request.GET['A8'] == '1' \
        and request.GET['A9'] == '1' \
        and request.GET['A10'] == '1' \
        and request.GET['A11'] == '10' \
        and request.GET['A12'] == '1' \
        and request.GET['A13'] == '1' \
        and request.GET['A14'] == '6' \
        and request.GET['A15'] == '10' \
            and request.GET['A16'] == '1':
        message = 'A3,A7,A11,A15'
    if request.GET['sex'] == '2' \
        and request.GET['age'] == '2' \
        and request.GET['job'] == '10'\
        and request.GET['earn'] == '4'\
        and request.GET['hobbit'] == '1' \
        and request.GET['A1'] == '8' \
        and request.GET['A2'] == '2'\
        and request.GET['A3'] == '7' \
        and request.GET['A4'] == '2' \
        and request.GET['A5'] == '2' \
        and request.GET['A6'] == '7' \
        and request.GET['A7'] == '2' \
        and request.GET['A8'] == '6' \
        and request.GET['A9'] == '7' \
        and request.GET['A10'] == '2' \
        and request.GET['A11'] == '7' \
        and request.GET['A12'] == '2' \
        and request.GET['A13'] == '2' \
        and request.GET['A14'] == '7' \
        and request.GET['A15'] == '8' \
            and request.GET['A16'] == '8':
        message = 'A1,A15,A16'


    return HttpResponse(message)




