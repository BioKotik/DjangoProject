from django.shortcuts import render, get_object_or_404
from expenses.models import Record
from django.views.generic import ListView

# Create your views here.
def all_records(request):
    a = 10
    records = Record.objects.all()
    return render(request, 'workplace.html', {'records': records})

class RecordListView(ListView):
    queryset = Record.objects.all()
    context_object_name = 'records'
    template_name = 'workplace.html'