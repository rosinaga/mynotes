from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Topic
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.
def home(request):
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
