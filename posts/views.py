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
            return redirect('/posts/templates/')
        else:
            #return render(request, 'posts/create.html',
                          #{'error': 'ERROR: You must include a title and a URL to create a post.'})
            return render(request, 'posts/editor.html')
    else:
        return render(request, 'posts/editor.html')

# @login_required
# def home(request):
#   posts = Template.objects.order_by('-votes_total')
#   return render(request, 'posts/home.html', {'posts':posts})

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
#         post.v+otes_total -= 1
#         post.save()
#         return redirect('home')

@login_required
def templates(request):
    docs = Template.objects.filter(user_id=request.user.id).order_by('-date_creation')
    public = Template.objects.filter(access=1).order_by('-date_creation')
    author = User.objects.get(username=request.user)
    return render(request, 'posts/usertemplates.html', {'userDocs':docs, 'publicDocs':public, 'author':author})

def documents(request):
    docs = Template.objects.filter(user_id=request.user.id).order_by('-date_creation')
    public = Template.objects.filter(access=1).order_by('-date_creation')
    author = User.objects.get(username=request.user)
    return render(request, 'posts/userdocs.html', {'userDocs':docs, 'publicDocs':public, 'author':author})

def insertTemplate(request, template):
    template.name = request.POST['name']
    template.text = request.POST['text']
    template.description = request.POST['description']
    template.access = request.POST.get('access', False)
    template.date_creation = timezone.datetime.now()
    template.user = request.user

    parents = Template.objects.filter(name=request.POST['name']).order_by('-version')
    if parents:
        template.version = parents[0].version + 1

    # template.version = request.POST['title']
    template.save()
    templates(request)

def insertTags(request, template):
    words = request.POST['tags'].split(",")
    for element in words:
        tag = Tag()
        tag.name = element.strip()
        tag.doc_id = template.id
        tag.save()