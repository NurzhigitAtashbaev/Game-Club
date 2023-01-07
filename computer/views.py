from .models import Computer

from django.shortcuts import render, redirect
from .form import ComputerForm


def base(request):
    """ При входе на главную страницу redirect на general_computers"""
    return redirect('general')


def general_computers(request):
    """Все компьютеры общего зала"""
    computers = Computer.objects.filter(category='general')
    return render(request, 'html/general.html', {'computers': computers})


def vip_computer(request):
    """Все компьютеры вип зала"""
    computer = Computer.objects.filter(category='VIP')
    return render(request, 'html/vip.html', {'computers': computer})


def manage_computer(request, pk):
    """Добавление игрового врмени, доступ к включению компьютера"""
    computer = Computer.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('general')
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'html/computer_details.html', {'form': form})


def search(request):
    """Поиск компьютера по его номеру"""
    number = request.GET.get('number')
    computers = Computer.objects.filter(number=number)
    return render(request, 'html/computer_details.html', {'computers': computers})
