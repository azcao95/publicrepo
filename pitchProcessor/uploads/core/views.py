from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document, FileData
from uploads.core.forms import DocumentForm

import re


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', {'documents': documents})


def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            try:
                file_lines = myfile.read().decode("utf-8").split("\n")

                file_data = FileData()
                data = file_data.process_file(file_lines)
            except Exception as e:
                return render(request, 'core/simple_upload.html', {
                    'error_msg': 'Error reading file',
                    'error': e
                })

            if data != None:
                try:
                    fs = FileSystemStorage()
                    filename = fs.save(myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)
                except:
                    return render(request, 'core/simple_upload.html', {
                        'error_msg': 'Error saving file',
                        'error': e
                    })
                return render(request, 'core/simple_upload.html', {
                    'uploaded_file_url': uploaded_file_url,
                    'data': data
                })
            else:
                return render(request, 'core/simple_upload.html', {
                    'error_msg': 'File doesn\'t seem to be a PITCH file',
                })
    except Exception as e:
        return render(request, 'core/simple_upload.html', {
            'error_msg': 'Error loading file',
            'error': e
        })

    return render(request, 'core/simple_upload.html')
