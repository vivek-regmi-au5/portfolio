from django.shortcuts import render

# Create your views here.
from .models import Blog 

def blog(request):

	blog = Blog.objects
	return render(request, 'blog/blog.html', {'blog':blog})
