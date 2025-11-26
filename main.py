from downloader import baixar_legenda
from cleaner import limpar_vtt
from summarizer import resumir_texto, nome_arquivo
import os

# ==========================
#         CONSTANTES
# ==========================

CAMINHO_SAIDA_TXT = "clean_subtitles/legenda_limpa.txt"
CAMINHO_VTT = "subtitles_extracted/video_temp.pt.vtt"
PASTA_SUMMARIES = "summaries"
ARQUIVO_LIMPO = f"{PASTA_SUMMARIES}/{nome_arquivo}"
ARQUIVO_TEMP_TXT = "clean_subtitles/legenda_limpa.txt"
ARQUIVO_TEMP_VTT = "subtitles_extracted/video_temp.pt.vtt"

# ==========================
#          CÓDIGO
# ==========================

URL = input("Cole a URL do video do YouTube: ")

print("\n🎥 Baixando legenda...")
legenda_path = baixar_legenda(URL)

print("🧹 Limpando legenda...")
print("🛠️ Abrindo arquivo:", CAMINHO_VTT)
with open(legenda_path, 'r', encoding='utf-8') as f:
    legenda_raw = f.read()

legenda_limpa = limpar_vtt(CAMINHO_VTT, CAMINHO_SAIDA_TXT)

print("🤖 Resumindo com IA...")
resumo = resumir_texto()

print("📄 RESUMO:")
with open(ARQUIVO_LIMPO, "r", encoding="utf-8") as f:
    resumo = f.read()
print(resumo)

print("\n✅ Resumo salvo na pasta summaries")

os.remove(ARQUIVO_TEMP_TXT)
os.remove(ARQUIVO_TEMP_VTT)
