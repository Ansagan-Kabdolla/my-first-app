from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from .forms import PdfForm
from .models import *
import os
from django.http import HttpResponse



class PdfCreateView(CreateView):
    model=Filepdf
    template_name = 'publication/add.html'
    form_class = PdfForm
    success_url = '/p'

def index(request):
    return render(request, "publication/zhurnal.html")

def show(request):
    ps = Filepdf.objects.all()
    return render(request, "publication/publ.html", {'ps': ps})

def only(request,pk):
    q = get_object_or_404(Filepdf, pk=pk)
    return render(request, 'publication/only.html', {'q': q})

def download(request,fn):
   # fp = open(path, "rb")
   # response = HttpResponse(fp.read())
   # fp.close()
    file = Filepdf.objects.get(file=fn)
    name = file.file
    path_to_file = os.path.realpath("media/{}".format(name))
    f = open(path_to_file, 'rb')
    response = HttpResponse(f, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + str(name)
    return response


def contact(request):
    return render(request, "publication/Contact.html")


def gid(request):
    return render(request, "publication/Gid.html")


def zhurnal(request):
    return render(request, 'publication/index.html')


def etic(request):
    return render(request, 'publication/Etic.html')

def all_files(request):
    files = Filepdf.objects.all()
    return render(request, 'publication/Pdf_files.html',{'files':files})