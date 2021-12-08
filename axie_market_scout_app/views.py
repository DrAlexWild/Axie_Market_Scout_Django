from django.shortcuts import render
from .models import Sale
from .utils import routine_main



# Create your views here.
def main_view(request):
    """Sale.objects.create(item='pizza', price='5')
    Sale.objects.create(item='apple', price='3')
    qs = Sale.objects.all()"""
    #print(qs)
    """x = [x.item for x in qs]
    y = [y.price for y in qs]"""

    """chart = routine_main(
        "Reptile",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        0,
        7,
        0,
        2,
        0,
        0,
        0,
        0,
        "None",
        0,
        "None",
        0,
        "None",
        0,
        "None",
        0,
        "None",
        0,
        "None",
        0,
        "None",
        "None"
    )"""


    #request.session['new_graph'] = chart
    request.session['num'] = 0


    context = {
        #'new_graph': request.session['new_graph'],
        'class_type': "None",
        'eyes': "None",
    }

    return render(request, 'views_html/results.html', context=context)

def secondary_view(request):

    request.session['num'] += 1

    """print("AAAAAAAAAAAAAAAAAAAAAAAA")
    print('eyes' + str(request.GET['eyes']))
    print('class_type' + str(request.GET['class_type']))"""

    chart = routine_main(
        request.GET['class_type'],
        request.GET['eyes'],
        request.GET['mouth'],
        request.GET['back'],
        request.GET['ears'],
        request.GET['horns'],
        request.GET['tail'],
        int(request.GET['breeds_min']),
        int(request.GET['breeds_max']),
        int(request.GET['min_value']),
        int(request.GET['max_value']),
        int(request.GET['min_health']),
        int(request.GET['min_speed']),
        int(request.GET['min_skill']),
        int(request.GET['min_morale']),
        request.GET['eye_gene'],
        int(request.GET['eye_gene_chance_min']),
        request.GET['ear_gene'],
        int(request.GET['ear_gene_chance_min']),
        request.GET['mouth_gene'],
        int(request.GET['mouth_gene_chance_min']),
        request.GET['horn_gene'],
        int(request.GET['horn_gene_chance_min']),
        request.GET['back_gene'],
        int(request.GET['back_gene_chance_min']),
        request.GET['tail_gene'],
        int(request.GET['tail_gene_chance_min']),
        request.GET['date_start'],
        request.GET['date_end']
    )

    request.session['new_graph'] = chart
    context = {
        'class_type': request.GET['class_type'],
        'eyes': request.GET['eyes'],
    }
    context['new_graph'] = request.session['new_graph']

    return render(request, 'views_html/results.html', context=context)

