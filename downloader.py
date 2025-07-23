import yt_dlp
import glob

def baixar_legenda(url):
    outtmpl = 'subtitles_extracted/video_temp.%(ext)s'
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['pt'],
        'skip_download': True,
        'outtmpl': outtmpl,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Retorna o caminho da legenda baixada
    legendas = glob.glob("subtitles_extracted/*.srt") + glob.glob("subtitles_extracted/*.vtt")
    return legendas[0] if legendas else None