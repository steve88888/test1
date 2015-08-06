from django.shortcuts import render, RequestContext, render_to_response, Http404
from .forms import ContactForm, SignUpForm, SearchForm
from django.contrib.auth.models import User
from .models import SignUp
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.contrib.auth import get_user_model

#@login_required
def edit_profile(request):
	title = "Edit Profile"
	signup, created = SignUp.objects.get_or_create(user = request.user)
	form = SignUpForm(request.POST or None, request.FILES or None, instance = signup)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		title = "Profile has been sucessfully updatted"
		#return redirect("single_user")
	context ={
		"form": form,
		"title": title,
		}
	return render(request, "update_profile.html", context)




	#user = request.user
	
	#picture = UserPicture.objects.get(user=user)
	#try:
	#	signup = SignUp.objects.get(user=user)
	#	signup_form = SignUpForm(request.POST or None, prefix = 'signup', instance = signup)
		#user_picture_form = UserPictureForm(request.POST or None, prefix = 'pic', instance = picture)
		

	#	if signup_form.is_valid():
	#		form1 = signup_form.save(commit=False)
	#		form1.save()
		
		#form2 = user_picture_form.save(commit =False)
		#form2.save()
	#return render_to_response("update_profile.html", locals(), context_instance=RequestContext(request))
	#except:
	#	user = request.user
	#	form = SignUp(request.POST or None)
		
	#	context = {
	#	"form": form,

	#	}
	#	if form.is_valid():
	#		form2 =form.save(commit = False)
	#		form2.save()

	#	return render(request, "new_profile.html", context)
		

def newProfile(request):


	return render(request, "new_profile.html", context)


	


	#if request.user.is_authenticated():
	#	user = request.user	
	#	title = "Welcome to Project Unite"
	#	form = SignUpForm()
	#	picture = UserPictureForm
	
	#	signup = SignUp.objects.get(user = user):
	#	form = SignUpForm(request.POST or None, instance = signup)
	#	picture = UserPicture.objects.get(user = user)
	#	UserPic = UserPictureForm(request.POST or None, request.FILES, instance = picture)

			#if form.is_valid() and UserPic.is_valid():
			#	form1 = form.save(commit = False)
			#	form1.save()
			#	form2 = UserPic.save(commit = False)
			#	form2.save()
		#else:
		#	if request.method=="POST":
	#
	#			context = {
	#			"title": title,
	#			"form": form
	#			}
	#			if form.is_valid():
	#				instance = form.save(commit=False)
	#				instance.save()
	#			return render(request, "update_profile.html", context)
		#"UserPicture": UserPicture
		#}
		#if request.user.is_authenticated():
		#	title = "Project Unite %s" %(request.user)
		
	
		#may require futher validation at a later date
		#if form.is_valid():
		#	instance = form.save(commit=False)
		#	full_name = form.cleaned_data.get("full_name")

			#if not full_name:
			#	full_name = "Unknown Name"
			#	instance.full_name = full_name
			#instance.save()
			#context = {"title": "Your profile has been updated"}
	#return render_to_response("update_profile.html", locals(), context_instance=RequestContext(request))
	#else:
		#title = "Error you must be logged in to update your profile"
		#context = {
		#"title": title
		#}
		#return render(request, "error.html", context)

# Create your views here.
#cant save so use model
def contact(request):
	form = ContactForm(request.POST or None)




	context = {
		"form": form,
	}
	return render(request, "forms.html", context)

def home(request):

	return render(request, "home.html", {})

def all(request):
	if request.user.is_authenticated():
		#for search function!!!!
		users = User.objects.filter(is_active=True)

		return render_to_response('all.html', locals(), context_instance = RequestContext(request))
	else:
		title = "Error you must be logged in to update your profile"
		context = {
		"title": title
		}
		return render(request, "error.html", context)

def single_user(request, userID):
	try:
		user = SignUp.objects.get(userID=userID)
		#name = single_user.get('full_name')
		
		single_user = user
		model = SignUp
		
	except:
		raise Http404
	#return render(request, "single_user.html", context)
	return render_to_response('single_user.html', locals(), context_instance = RequestContext(request))



def search_profiles(request):
	
	form = SearchForm(request.POST or None)
	if form.is_valid():
		location = form.cleaned_data['location']
		print location
		expertise = form.cleaned_data['expertise']
		print expertise

	#if 'location' in request.GET:
	#	print location
	#else: 
	#	print "error in getting location"
	#if request.method == 'POST':
	#	if not request.POST.get('location', ''):
	#		print "error"
	#location = request.POST['']
	#print location
	#user_location = request.GET['location']
	#print user_location
	#if form.is_valid():
		#location = get_object_or_404('location')
		#category = get_object_or_404('category')
	#	if location in request.GET and request.GET['Melbourne']:
	#		location = request.GET['Melbourne']
	#		print location
    #	elif 'Brunswick' in request.GET and request.GET['Brunswick']:
     #   	location = request.GET['Brunswick']	
      #  	print location
       # 	print "printed location"
        #elif 'WorldWide' in request.GET and request.GET['WorldWide']:
        #	location = request.GET['WorldWide']
        #	print location

		users = SignUp.objects.filter(location = location, expertise = expertise)
	
	return render_to_response('searchProfiles.html', locals(), context_instance = RequestContext(request))
	

