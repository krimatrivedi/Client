from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegistration
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalCreateView,
    
)

from .forms import (
    BookModelForm,
    ProjectModelForm,
    CustomAuthenticationForm,
    
)
from .models import Book,Project


#RegisterUser
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'examples/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'examples/register.html', context=context)

#sidebar
@login_required
def dashboard(request):
   
    
    return render(request, 'dashboard.html')

#dashboard
def Dashboard1(request):
    #number of clients
    client_count=Book.objects.all().count
    #number of project's status for pie chart
    pending=Project.objects.filter(workstatus='Pending').count()
    Completed=Project.objects.filter(workstatus='Completed').count()
    OnProgress=Project.objects.filter(workstatus='OnProgress').count()
   
    return render(request, 'Dashboard1.html',{"client_count":client_count,"pending":pending,
    "Completed":Completed,"OnProgress":OnProgress})

#clientpage    
def client(request):
    client_count=Book.objects.all().count
    
    return render(request, 'client.html',{"client_count":client_count})

#projectpage    
def Projects(request):
    project_count=Project.objects.all().count
    status_count = Project.objects.values('workstatus').annotate(count=Count('workstatus')).order_by()
    pending=Project.objects.filter(workstatus='Pending').count()
    Completed=Project.objects.filter(workstatus='Completed').count()
    OnProgress=Project.objects.filter(workstatus='OnProgress').count()

    return render(request, 'Project.html',{"project_count":project_count,"status_count":status_count,
    "pending":pending,"Completed":Completed,"OnProgress":OnProgress})    

#showclientdetailsfull
class Client(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = '_books_table.html'

    def num(request):
         return render(request, 'Client.html')

#showprojectdetails         
class ProjectDetails(generic.ListView):
    model = Project
    context_object_name = 'projectss'
    template_name = 'Projecttable.html'

#showclientdetails   for managerclient
class ClientDetails(generic.ListView):
    model = Project
    context_object_name = 'projectss'
    template_name = 'client_details.html'
   


class BookCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('client')
#addprojct
class ProjectCreateView(BSModalCreateView):
    template_name = 'examples/create_project.html'
    form_class = ProjectModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('client')



class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('client')



def books(request):
    data = dict()
    if request.method == 'GET':
        books = Book.objects.all()
        client_count=Book.objects.all().count
        print(client_count,"count")
        data['table'] = render_to_string(
            '_books_table.html',
            {'books': books,
            'client_count':client_count},
            request=request
        )
        return JsonResponse(data)
