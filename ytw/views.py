from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from yt_dlp import YoutubeDL
import os
import tempfile
import shutil
from ytw.cron import iniciar_agendamento


def download_video(request):

    iniciar_agendamento()
    

    if request.method == 'POST':
        url = request.POST.get('video_url')
        output_folder = 'video_folder'  # Especifique o caminho completo da pasta de destino

        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
                'ignoreerrors': True,
            }

            with YoutubeDL(ydl_opts) as ydl:

                info_dict = ydl.extract_info(url, download=True)
                # print(info_dict)
                video_tittle = ydl.prepare_filename(info_dict)
                

                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    ydl.download([url])
                    video_filename = os.path.join(video_tittle)
                    
                    shutil.copyfile(video_filename, temp_file.name)

                response = FileResponse(open(temp_file.name, 'rb'), as_attachment=True)
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video_filename)}"'
                return response

        except Exception as e:
            return HttpResponse(f"O vídeo não pôde ser baixado: {str(e)}")

    return render(request, 'download_video.html')
