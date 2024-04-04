from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def result(request):
    if request.GET.get('number1') != '':
        num1 = float(request.GET.get('number1'))
    else:
        num1 = 0
    if request.GET.get('number1') != '':
        num2 = float(request.GET.get('number2'))
    else:
        num2 = 0

    ans = num1 * num2

    return render(request, 'result.html', {'ans': ans})
