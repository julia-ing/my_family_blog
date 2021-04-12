from django.shortcuts import render, redirect, get_object_or_404
from .models import myText, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import PostingForm

# Create your views here.

def posting_list(request):
    texts = myText.objects.filter()
    around_news = myText.objects.filter(category="주변 뉴스")
    family_news = myText.objects.filter(category="가족 소식")
    memory = myText.objects.filter(category="추억 기록")
    return render(request, 'share/posting_list.html', {'texts': texts, 'around_news': around_news,
                                                       'family_news': family_news, 'memory': memory})

def posting_list_info(request, pk):
    board_contents = get_object_or_404(myText, pk=pk)
    comment = Comment.objects.filter(lecture=board_contents)

    if request.method == 'POST':
        rate = request.POST['rate']
        writer = request.POST['writer']
        comment = request.POST['comment']

        Comment.objects.create(posting=board_contents, writer=writer, rate=rate, comment=comment)
        return redirect('/posting_list/' + str(pk))

    return render(request, 'share/posting_list_info.html', {'board_contents': board_contents,
                                                              'comment': comment})

def comment_remove(request, pk):
    if request.method == 'POST':
        Comment.objects.get(pk=pk).delete()

    return redirect('/posting_list')

def show_posting(request, pk):
    board_contents = get_object_or_404(myText, pk=pk)
    return render(request, 'share/show_posting.html', {'board_contents': board_contents})

def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST, request.FILES)
        if form.is_valid():
            myText = form.save(commit=False)
            myText.author = request.user
            myText.save()
            return redirect('/share/lecture_list')
    posting_form = PostingForm()
    return render(request, 'share/create_posting.html', {'posting_form': posting_form})

def my_posting(request):
    posting = myText.objects.filter(author=request.user)
    return render(request, 'share/my_posting.html', {'posting': posting})

def edit_posting(request, pk):
    posting = get_object_or_404(myText, pk=pk)

    if request.method == 'POST':
        form = PostingForm(request.POST, request.FILES, instance=posting)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.author = request.user
            posting.save()
            return redirect('/my_lecture')
    else:
        form = PostingForm(instance=posting)

    return render(request, 'share/edit_posting.html', {'posting_form': form, 'primary_key': pk})
