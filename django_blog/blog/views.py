from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Update,Medicine
import speech_recognition as sr
from django.views.generic import (
    ListView,
    
    DetailView,
)
from django.urls import reverse_lazy,reverse
from .forms import CustomerForm
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)



class UpdateDetailView(DetailView):
    model = Update

class MedicineDetailView(DetailView):
    model = Medicine

class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["date_posted"]
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)
        updates = Update.objects.filter(title__contains = searched)
        medicines = Medicine.objects.filter(title__contains = searched)

        return render(request,'blog/search.html',{'searched':searched,'posts':posts,'updates':updates,'medicines':medicines})
    else:
        return render(request,'blog/search.html',{})

def about(request):
    return render(request, "blog/about.html", {"title": "About"})

def thank_you(request):
    template = 'thanks.html'
    context = {}
    return render(request, template, context)

def updates(request):
    context = {"updates": Update.objects.all()}
    return render(request, "blog/updates.html", context)


def medicines(request):
    context = {"medicines": Medicine.objects.all()}
    return render(request, "blog/medicines.html", context)

def speech_to_text(request):
    data = request.POST.get('record')
    

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)

    try:
        output = " " + r.recognize_google(audio)
    except sr.UnknownValueError:
        output = "Could not understand audio"
    except sr.RequestError as e:
        output = "Could not request results; {0}".format(e)
    data =output

    return render(request,'blog/base.html',{'data':data})
    
 
def contact(request):
	
	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
            
        	
	context = {'form':form}
	return render(request, 'blog/email.html', context)
