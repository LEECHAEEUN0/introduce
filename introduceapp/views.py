from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request, 'bootstrap.html')

def department(request):
    return render(request, 'department.html')

def flex(request):
    return render(request, 'flex.html')

def table(request):
    return render(request, 'table.html')

def test(request):
    return render(request, 'test.html')

def base(request):
    return render(request, 'base.html')    