from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from upload.forms import FileFieldForm
from upload.utils import flac_upload_handler


# Create Your Views Here

@login_required()
def file_upload_form(request):
    form = FileFieldForm(request.POST, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for file in files:
                if file.name.endswith('.flac'):
                    flac_upload_handler(file)

                elif file.name.endswith('mp3'):
                    pass
        return render(request, 'upload/successful/index.html')
    elif request.method == "GET":
        if request.user.is_superuser:
            form = FileFieldForm()

    return render(request, 'upload/index.html', {'form': form})
