from django.shortcuts import render, redirect, get_object_or_404
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    ctx = {'videos': videos}
    return render(request, 'videos/video-list.html', ctx)

def video_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        upload_date = request.POST.get('upload_date')
        video_file = request.FILES.get('video_file')
        if title and description and upload_date and video_file:
            Video.objects.create(
                title=title,
                description=description,
                upload_date=upload_date,
                video_file=video_file,
            )
            return redirect('videos:list')
    return render(request, 'videos/video-create.html')

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        upload_date = request.POST.get('upload_date')
        video_file = request.FILES.get('video_file')
        if title and description and upload_date and video_file:
            video.title = title
            video.description = description
            video.upload_date = upload_date
            video.video_file = video_file
            video.save()
            return redirect(video.get_detail_url())
    ctx = {'video': video}
    return render(request, 'videos/video-create.html', ctx)


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    ctx = {'video': video}
    return render(request, 'videos/video-detail.html', ctx)

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect('videos:list')
    ctx = {'video': video}
    return render(request, 'videos/video-delete-confirm.html', ctx)

