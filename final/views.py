from django.shortcuts import render



# Create your views here.
def hello_view(request):
    return render(request, 'final_view.html', {
        'data': "Hello Django ",
    })


def option_1(request):
    return render(request, 'A1.html', {
        'data': "這是A1 ",
    })

