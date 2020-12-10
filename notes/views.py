from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Topic
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.
def home(request):
	alltopics = Topic.objects.all()
	return render(request, 'home.html', {'topics_for_home': alltopics})



def topic_new(request):
	user = User.objects.first()
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.owner = user
			topic.save()
			return redirect('url_topic_new')
	else:
		form = NewTopicForm()
	return render(request, 'topic_new.html', {'topic_form': form})
