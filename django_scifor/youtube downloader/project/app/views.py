# app/views.py
from django.shortcuts import render
import yt_dlp
import os

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        print(f"Received link: {link}")  

        try:
            
            output_path = '/Users/pushpakreddy/youtube downloader/project'  
            
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            
   
            ydl_opts = {
                'format': 'best',  
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'), 
            }

            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_title = info_dict.get('title', None)
                print(f"Downloaded video: {video_title}")  
            return render(request, 'home.html', {'message': 'Download successful!'})

        except Exception as e:
            print(f"Error: {e}")  
            return render(request, 'home.html', {'error': f'An unexpected error occurred: {e}'})

    return render(request, 'home.html')
