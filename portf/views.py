from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project(request):
    projects = [
        {
            'title' : 'TravelWorld',
            'url' : 'https://res.cloudinary.com/dq7ldqmy4/image/upload/v1751905369/TravelWorld_oewxwr.png'
            },
            {
            'title' : 'E-commerece',
            'url' : 'https://res.cloudinary.com/dq7ldqmy4/image/upload/v1751905369/ecommerece_lkept6.png'
            },
            {
            'title' : 'Personal-Portfolio',
            'url' : 'https://res.cloudinary.com/dq7ldqmy4/image/upload/v1751905369/portfolio_areoaj.png'
            },
            {
            'title' : 'Simple-User-Authentication',
            'url' : 'https://res.cloudinary.com/dq7ldqmy4/image/upload/v1751905381/simpleuserauthentication_qhkxyw.png '
            },
            {
                'title' : 'Daily Expense Tracker',
            'url' : 'https://res.cloudinary.com/dq7ldqmy4/image/upload/v1752746399/TrakX_cfxooy.png '
            }
            
    ]
    data={
        'projects':projects,
    }
    return render(request, 'project.html', data)

def experience(request):
    experience = [
        {
            'company_name' : 'Suprima Infotech Pvt Ltd',
            'role' : 'Project Intern'

        },
        {
            'company_name' : 'Rotospintech ',
            'role' : 'Project Intern'

        },
        {
            'company_name' : 'ABC',
            'role' :'Intern'

        },

    ]
    data={
        'experience' : experience
    }
    return render(request, 'experience.html',data)


def contact(request):
    return render(request, 'contact.html')

def resume(request):
    resume_path="myapp/amrutresume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,'rb') as resume_file:
            response = HttpResponse(resume_file.read(),content_type = "application/pdf")
            response['Content-Disposition']='attachment';filename="amrutdeshpanderesume.pdf"

            return response
    else:
        return HttpResponse('Not Found')
