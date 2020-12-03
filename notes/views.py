from django.shortcuts import render
from .models import Note, Topic
# Create your views here.
def home(request):
	alltopics = Topic.objects.all()
	return render(request, 'home.html', {'topics_for_home': alltopics})



def topic_new(request):
	if request.method == 'POST':
		subject = request.POST['subject']
		desc = request.Post['description']
		user = User.objects.first()
		topic = Topic.objects.create(
			subject = subject,
			description = desc,
			owner = user
		)
		return redirect('url_topics')
	return render(request, 'topic_new.html')
