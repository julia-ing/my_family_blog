from django.shortcuts import render, redirect, get_object_or_404
from .models import myText, Comment
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LectureForm

# Create your views here.

def lecture_list(request):
    texts = myText.objects.filter()
    around_news = myText.objects.filter(category="주변 뉴스")
    family_news = myText.objects.filter(category="가족 소식")
    memory = myText.objects.filter(category="추억 기록")
    return render(request, 'share/lecture_list.html', {'texts': texts, 'around_news': around_news,
                                                       'family_news': family_news, 'memory': memory})

def lecture_list_info(request, pk):
    board_contents = get_object_or_404(myText, pk=pk)
    comment = Comment.objects.filter(lecture=board_contents)

    if request.method == 'POST':
        rate = request.POST['rate']
        writer = request.POST['writer']
        comment = request.POST['comment']

        Comment.objects.create(lecture=board_contents, writer=writer, rate=rate, comment=comment)
        return redirect('/lecture_list/' + str(pk))

    return render(request, 'share/lecture_list_info.html', {'board_contents': board_contents,
                                                              'comment': comment})

def comment_remove(request, pk):
    if request.method == 'POST':
        Comment.objects.get(pk=pk).delete()

    return redirect('/lecture_list')

def show_lecture(request, pk):
    board_contents = get_object_or_404(myText, pk=pk)
    return render(request, 'share/show_lecture.html', {'board_contents': board_contents})

def create_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            myText = form.save(commit=False)
            myText.author = request.user
            myText.save()
            return redirect('/share/lecture_list')
    lecture_form = LectureForm()
    return render(request, 'share/create_lecture.html', {'lecture_form': lecture_form})

def my_lecture(request):
    lectures = myText.objects.filter(author=request.user)
    return render(request, 'share/my_lecture.html', {'lectures': lectures})

def edit_lecture(request, pk):
    lecture = get_object_or_404(myText, pk=pk)

    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.author = request.user
            lecture.save()
            return redirect('/my_lecture')
    else:
        form = LectureForm(instance=lecture)

    return render(request, 'share/edit_lecture.html', {'lecture_form': form, 'primary_key': pk})
