from django.shortcuts import render

def hotel_list(request):
    return render(request, 'hotel/hotel_list.html', {})

