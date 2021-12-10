from django.shortcuts import render
from .models import Sale
from .utils import *


# Create your views here.
def main_view(request):
    context = {}
    return render(request, 'views_html/results.html', context=context)

def secondary_view(request):

    context = {}

    #String with \n per error
    search_helper = search_helper_custom(
        request.GET['class_type'],
        request.GET['eyes'],
        request.GET['mouth'],
        request.GET['back'],
        request.GET['ears'],
        request.GET['horns'],
        request.GET['tail'],
        request.GET['breeds_min'],
        request.GET['breeds_max'],
        request.GET['min_value'],
        request.GET['max_value'],
        request.GET['min_health'],
        request.GET['min_speed'],
        request.GET['min_skill'],
        request.GET['min_morale'],
        request.GET['eye_gene'],
        request.GET['eye_gene_chance_min'],
        request.GET['ear_gene'],
        request.GET['ear_gene_chance_min'],
        request.GET['mouth_gene'],
        request.GET['mouth_gene_chance_min'],
        request.GET['horn_gene'],
        request.GET['horn_gene_chance_min'],
        request.GET['back_gene'],
        request.GET['back_gene_chance_min'],
        request.GET['tail_gene'],
        request.GET['tail_gene_chance_min'],
        request.GET['date_start'],
        request.GET['date_end']
    )

    context['error_message'] = search_helper

    if search_helper == "":# No errors

        # return of chart
        #utf-8  base-64-image??
        """def get_graph():
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            graph = base64.b64encode(image_png)
            graph = graph.decode('utf-8')
            buffer.close()
        return graph"""

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

        context['new_graph'] = chart

        #String with \n per axie
        axies_in_graph = create_custom_search_results()
        context['axies_in_graph'] = axies_in_graph

    return render(request, 'views_html/results.html', context=context)

