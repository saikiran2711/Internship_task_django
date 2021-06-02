from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskUploadForm
from .models import TaskUpload
from faker import Faker

# Create your views here.
def uploadFakeData(request):
    faker = Faker()
    for i in range(0, 50):
        obj = TaskUpload(uid = request.user, task_title = faker.text(max_nb_chars=15), task_description = faker.sentence(nb_words=40) , create_timestamp = faker.date_time())
        obj.save()

@login_required()
def upload(request):
    form = TaskUploadForm()
    if request.method == 'POST':
        form = TaskUploadForm(request.POST, request.FILES)
        if form.is_valid():

            s = form.save(commit= False)
            s.uid = request.user
            s.save()

            a = TaskUpload.objects.filter(uid = request.user).order_by('-create_timestamp')
            print(a[0])
            print(a[0].task_title)
            return redirect('home')
        else:
            print("Form not valid")
            messages.error(request, "Form Validation Failed , please try again!")

    return render(request,'task_app/task_upload.html', {'form' : form})




@login_required()
def display(request):
    #uploadFakeData(request)  #this function is used only once at first tiem when this page is rendered and later on is not needed.
    movies = TaskUpload.objects.filter(uid = request.user)  # queryset containing all movies we just created
    paginator = Paginator(movies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="task_app/display.html", context={'tasks': page_obj})
