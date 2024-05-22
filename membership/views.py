from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from mentor.models import Student,Teacher

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		data = request.POST['role']
		if user is not None:
			if request.POST['role']=='student' and Student.objects.filter(student=user).exists():
				login(request, user)
				return redirect('core:home')
			elif request.POST['role']=='teacher' and Teacher.objects.filter(teacher=user).exists():
				login(request, user)
				return redirect('core:home')

			else:
				messages.error(request,("Please Check your role again is it correct"))
				return redirect('membership:login')                                                                                                                      
      
		
		else:
			messages.error(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('membership:login')	


	else:
		return render(request, 'membership/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('core:home')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			profile_image = request.FILES['profile_image']
			role = request.POST['role']
			if role=='teacher':
				position = request.POST['position']
				about = request.POST['about']
				print(request.POST)
				achievements = request.POST['achievements']
				objectives = request.POST['objectives']
				Teacher.objects.create(teacher=user,position=position,about=about,achievements=achievements,objectives=objectives,image=profile_image)
			if role == 'student':
				Student.objects.create(student=user,image=profile_image)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('core:home')
	else:
		form = RegisterUserForm()

	return render(request, 'membership/register_user.html', {
		'form':form,
		})
