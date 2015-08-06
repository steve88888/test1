from django.shortcuts import render, RequestContext, render_to_response, Http404
from .forms import FormProjectTitle, SearchForm, DeleteForm
from .models import ProjectTitle
from django.contrib.auth.models import User
# Create your views here.
#def projectlist(request):
	#title = "Current Projects listed below"
	#form = ProjectForm(request.POST or None)
	#form = SignUpForm(request.POST or None)
	#if request.user.is_authenticated():
	#	title = "Project Unite %s" %(request.user)

	#if request.method=="POST":
	#	print request.POST
	#context = {
	#"title": title,
	#"form" : form,

	#}
	#return render(request, "allproject.html", context)
#def newProject(request):
#	user = request.user
#	projecttitle = ProjectTitle.objects.get(user=user)
#	form = FormProjectTitle(request.POST or None, instance = projecttitle)

#	if form.is_valid():

#		form.save()

#	return render_to_response('newProject.html', locals(), context_instance = RequestContext(request))


def new_project(request):
	title = "Create a new Project"
	form = FormProjectTitle(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		title = "Project has been sucessfully created"
	context = {
		"form": form,
		"title": title,

	}
	return render(request, "newProject.html", context)
def edit_project(request, projectID):
	title = "Edit Project"
	projecttitle, created = ProjectTitle.objects.get_or_create(user = request.user)
	form = FormProjectTitle(request.POST or None, request.FILES or None, instance = projecttitle)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		title = "Project has been sucessfully updatted"
		#return redirect("single_user")
	context ={
		"form": form,
		"title": title,
		}
	return render(request, "editProject.html", context)


def projectlist(request):
	if request.user.is_authenticated():
		#for search function!!!!
		#title = "Assinate 007"
		projects = ProjectTitle.objects.filter(active=True)
		#projects = ProjectTitle.objects.filter(projectID = "2")
		#users = User.objects.filter(is_active=True)
		return render_to_response('allproject.html', locals(), context_instance = RequestContext(request))
	else:
		title = "Error you must be logged in to search projects"
		context = {
			"title": title
			}
		return render(request, "error.html", context)
#needs to save data properly
#def EditProject(request):
#	if request.user.is_authenticated():
#		title = "Welcome to Project Unite"
#		projects = ProjectTitle.objects.get(projectID=projectID)
#		form = FormProjectTitle(request.POST or None, instance = projecttitle)
		#picture = UserPicture.objects.get(user = user)
		#UserPic = UserPictureForm(request.POST or None, request.FILES, instance = picture)

#		if form.is_valid():
#			form = form.save(commit = False)
#			form.save()
			#form2 = UserPic.save(commit = False)
			#form2.save()
		#if request.user.is_authenticated():

	return render_to_response("newProject.html", locals(), context_instance=RequestContext(request))

def search_projects(request):

	form = SearchForm(request.POST or None)
	if form.is_valid():
		location = form.cleaned_data['location']
		print location
		expertise = form.cleaned_data['expertise']
		print expertise
		if location == 'All' and expertise == 'All':
			print "success"
			projects = ProjectTitle.objects.filter(active = True)
		elif location == 'All':
			projects = ProjectTitle.objects.filter(expertise = expertise, active = True)
		elif expertise == 'All':
			projects = ProjectTitle.objects.filter(location = location, active = True)
		else:
			projects = ProjectTitle.objects.filter(location = location, expertise = expertise, active = True)
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

		#projects = ProjectTitle.objects.filter(location = location, expertise = expertise)

	return render_to_response('searchProjects.html', locals(), context_instance = RequestContext(request))



def single_project(request, projectID):
	try:
		project = ProjectTitle.objects.get(projectID = projectID)
		#project = "Assinate 007"
		#name = single_user.get('full_name')
		#if project.is_active:
		single_project = project
		model = ProjectTitle
	except:
		raise Http404
	#return render(request, "single_user.html", context)
	return render_to_response('single_project.html', locals(), context_instance = RequestContext(request))

def my_projects(request):
	current_user = request.user
	if request.user.is_authenticated():
		projects = ProjectTitle.objects.filter(user = request.user)
		form = DeleteForm(request.POST or None)
		if form.is_valid():
			deleteID = form.cleaned_data['projectID']
			if ProjectTitle.objects.filter(user = current_user):
				if ProjectTitle.objects.filter(projectID = deleteID):
					b= ProjectTitle.objects.get(projectID = deleteID)
					b.delete()
					title = "Project has been sucessfully deleted"
				else:
					title = "Project could not be deleted"
			else:
				title = "you do not have permission to delete this project"
	return render_to_response('myProjects.html', locals(), context_instance = RequestContext(request))
