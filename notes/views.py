from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Topic
from django.contrib.auth.models import User
from .forms import NewTopicForm

# Create your views here.
def home(request):
	alltopics = Topic.objects.all()
	return render(request, 'home.html', {'topics_for_home': alltopics})

def topic_new(request):
	user = request.user
	if user.is_authenticated:
		if request.method == 'POST':
			form = NewTopicForm(request.POST)
			if form.is_valid():
				topic = form.save(commit=False)
				topic.owner = user
				topic.save()
				return redirect('url_topics')
		else:
			form = NewTopicForm()
		return render(request, 'topic_new.html', {'topic_form': form})
	else:
		return redirect('login')

def topic_edit(request, topic_id):
	user = request.user
	if user.is_authenticated:
		topic = get_object_or_404(Topic, pk=topic_id)
		if topic.owner != user:
			return HttpResponseForbidden
		else:
			if request.method == 'POST':
				form = EditTopicForm(request.POST, instance = topic)
				if form.is_valid():
					topic.save()
					return redirect('url_topics')
			else:

				form = EditTopicForm(instance=topic)
			return render(request, 'topic_edit.html', {'topic_form': form})
	else:
		return redirect('login')
