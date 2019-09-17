from django.shortcuts import render

posts = [
    {
        'title': 'First post',
        'date': '2nd Jan, 2019',
        'author': 'Bob',
        'content': 'First post woohoo'
    },
    {
        'title': 'Second post',
        'date': '3rd Jan, 2019',
        'author': 'Jane',
        'content': 'Second post sad'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)