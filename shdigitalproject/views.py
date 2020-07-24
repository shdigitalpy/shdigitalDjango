from django.shortcuts import render

def home(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message_content = request.POST['message-content']
		return render (request, 'home.html', {'message_content': message_content})

	else:
		return render (request, 'home.html',{})