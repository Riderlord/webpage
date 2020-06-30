from django.shortcuts import render

posts = [
    {
        'title': 'Python',
        'author': 'Sid',
        'content': 'First post',
        'date': 'June 4th,2019'

    },
    {
        'title': 'c++',
        'author': 'varun',
        'content': 'second post',
        'date': 'June 9th,2019'   
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    
    
    

