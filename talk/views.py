from django.shortcuts import render, get_object_or_404, redirect
from talk.models import Talk, Comment
from django.core.paginator import Paginator
from talk.forms import TalkForm, CommentForm, UpdateTalkForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User


def list(request):
    talks = Talk.objects.all()
    paginator = Paginator(talks, 5)

    page = request.GET.get('page')  # third/list?page=1
    items = paginator.get_page(page)
    context = {
        'talks': items
    }
    return render(request, 'talk/list.html', context)

def create(request):
    if request.method == 'POST':
        form = TalkForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            new_item.writer = request.user
        return HttpResponseRedirect('/talk/list/')
    form = TalkForm()
    return render(request, 'talk/create.html', {'form': form})

def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Talk, pk=request.POST.get('id'))
        password = request.POST.get('password', '')
        form = UpdateTalkForm(request.POST, instance=item)
        if form.is_valid() and password == item.password:
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(Talk, pk=request.GET.get('id'))
        form = TalkForm(request.GET, instance=item)
        return render(request, 'talk/update.html', {'form': form})
    return HttpResponseRedirect('/talk/list/')

def detail(request, id):
    if id is not None:
        item = get_object_or_404(Talk, pk=id)
        contents = Comment.objects.filter(talk=item).all()
        return render(request, 'talk/detail.html', {'item': item, 'contents': contents})
    if request.method == 'POST':
        contents = request.POST['content']
        writer = request.POST['writer']
        Comment.objects.create(writer=writer, content=contents)
        return redirect('/list/' + str(id))
    return HttpResponseRedirect('/talk/list/')

def delete(request, id):
    item = get_object_or_404(Talk, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('talk-detail', id=id)
    return render(request, 'talk/delete.html', {'item': item})

def comment_create(request, talk_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('talk-detail', id=talk_id)
    item = get_object_or_404(Talk, pk=talk_id)
    form = CommentForm(initial={'talk': item})  # 미리 채워지길 원하는 필드명 - restaurant
    return render(request, 'talk/comment_create.html', {'form': form, 'item': item})

def comment_delete(request, talk_id, comment_id):
    item = get_object_or_404(Comment, id=comment_id)
    item.delete()

    return redirect('talk-detail', id=talk_id)

def my_talk(request):
    talks = Talk.objects.filter(writer=request.user)
    return render(request, 'talk/my_talk.html', {'talks': talks})
