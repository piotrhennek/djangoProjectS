from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Template, Tag
from django.contrib.auth.models import User

@login_required
def editor(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['description'] and request.POST['tags'] and request.POST['text']:
            template = Template()
            insertTemplate(request, template)
            insertTags(request, template)
            return redirect('home')
        else:
            #return render(request, 'posts/create.html',
                          #{'error': 'ERROR: You must include a title and a URL to create a post.'})
            return render(request, 'posts/editor.html')
    else:
        return render(request, 'posts/editor.html')

@login_required
def home(request):
    posts = Template.objects.order_by('-votes_total')
    return render(request, 'posts/home.html', {'posts':posts})

# @login_required
# def upvote(request, pk):
#     if request.method == 'POST':
#         post = Template.objects.get(pk=pk)
#         post.votes_total += 1
#         post.save()
#         return redirect('home')
#
# @login_required
# def downvote(request, pk):
#     if request.method == 'POST':
#         post = Template.objects.get(pk=pk)
#         post.votes_total -= 1
#         post.save()
#         return redirect('home')

@login_required
def templates(request, fk):
    posts = Template.objects.filter(author__id=fk).order_by('-votes_total')
    author = User.objects.get(pk=fk)
    return render(request, 'posts/userposts.html', {'posts':posts, 'author':author})

def insertTemplate(request, template):
    template.name = request.POST['name']
    template.text = request.POST['text']
    template.description = request.POST['description']
    template.access = request.POST.get('access', False)
    template.date_creation = timezone.datetime.now()
    template.user = request.user
    # template.version = request.POST['title']
    template.save()

def insertTags(request, template):
    words = request.POST['tags'].split(",")
    for element in words:
        tag = Tag()
        tag.name = element.strip()
        tag.doc_id = template.id
        tag.save()