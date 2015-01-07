from django.shortcuts import render, get_object_or_404, redirect
from discussions.forms import PostForm, CommentForm
from discussions.models import Topic, Category, Comment
from institutions.models import Institution


def categories(request, abbr=None, template='discussions/index.html'):
    institution = get_object_or_404(Institution, abbr=abbr)
    latest_discussions = Topic.objects.filter(institution=institution).order_by('-date_created')
    categories = Category.objects.all().order_by('date_created')
    return render(request, template, {'institution':institution, 'latest_discussions':latest_discussions, 'categories':categories})

def category(request, abbr=None, discussion_category=None, template='discussions/category.html'):
    institution = get_object_or_404(Institution, abbr=abbr)
    category = get_object_or_404(Category, slug=discussion_category)
    discussions = Topic.objects.filter(institution=institution, category=category).order_by('-date_created')
    return render(request, template, {'institution':institution, 'discussions':discussions, 'category':category})

def topic(request, abbr=None, topic_id=None, topic_slug=None, template='discussions/topic.html'):
    institution = get_object_or_404(Institution, abbr=abbr)
    topic = get_object_or_404(Topic, id=topic_id, slug=topic_slug, institution=institution)
    comments = Comment.objects.filter(topic=topic).order_by('date_created')
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            c = comment_form.save(commit=False)
            c.topic = topic
            c.user = request.user
            c.save()
            return redirect('/%s/topic/%s/%s' %(institution.abbr, topic.id, topic.slug))
        else:
            return redirect('/%s/topic/%s/%s' %(institution.abbr, topic.id, topic.slug))
    #import time
    #from datetime import date
    #today = date.today()
    #str(today)
    return render(request, template, {'institution':institution, 'topic':topic, 'comments':comments, 'comment_form':comment_form})

def post_topic(request, abbr=None, template='discussions/post_topic.html'):
    cat = request.GET.get('cat')
    post_form = PostForm(request.POST)
    institution = Institution.objects.get(abbr=abbr)
    get_category = Category.objects.get(slug=cat)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            p = post_form.save(commit=False)
            p.category = get_category
            p.institution = institution
            p.user = request.user
            p.active = True
            p.save()
            return redirect('/%s/topic/%s/%s' %(institution.abbr, p.id, p.slug))
        else:
            return
        #return redirect('/')
    return render(request, template, {'institution':institution, 'post_form':post_form, 'category':get_category})

def addcomment(request, abbr=None, template='discussions/add_comment.html'):
    topic_id = request.GET.get('topic')
    institution = get_object_or_404(Institution, abbr=abbr)
    topic = get_object_or_404(Topic, id=topic_id, institution=institution)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            c = comment_form.save(commit=False)
            c.topic = topic
            c.user = request.user
            c.save()
            return redirect('/%s/topic/%s/%s' %(institution.abbr, topic.id, topic.slug))
        else:
            return redirect('/%s/topic/%s/%s' %(institution.abbr, topic.id, topic.slug))
    return render(request, template, {'institution':institution, 'topic':topic, 'comment_form':comment_form})
