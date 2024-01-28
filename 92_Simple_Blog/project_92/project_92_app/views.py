from django.shortcuts import render

# Create your views here.

blogs = [{'blog_1':['Famous Quote 1','You must be the change you wish to see in the world.','Mahatma Gandhi']},
         {'blog_2':['Famous Quote 2','The only thing we have to fear is fear itself.','Franklin D. Roosevelt']},
         {'blog_3':['Famous Quote 3','Well done is better than well said.','Benjamin Franklin']}
         ]

def blog_post(request):
    return render(request, 'blog.html', {'blogs': blogs})