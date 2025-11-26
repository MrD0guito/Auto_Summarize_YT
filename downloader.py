import yt_dlp
import glob

# ==========================
#         CONSTANTES
# ==========================

PASTA_LEGENDAS = "subtitles_extracted"
PADRAO_SAIDA = f"{PASTA_LEGENDAS}/video_temp.%(ext)s"
LINGUAS_SUBS = ["pt"]
PADRAO_SRT = f"{PASTA_LEGENDAS}/*.srt"
PADRAO_VTT = f"{PASTA_LEGENDAS}/*.vtt"

# ==========================
#        FUNÇÃO
# ==========================

def baixar_legenda(url):
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": LINGUAS_SUBS,
        "skip_download": True,
        "outtmpl": PADRAO_SAIDA,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Procura a legenda baixada
    legendas = glob.glob(PADRAO_SRT) + glob.glob(PADRAO_VTT)
    return legendas[0] if legendas else None
