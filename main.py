from downloader import baixar_legenda
from cleaner import limpar_vtt
from summarizer import resumir_texto, nome_arquivo
import os
caminho_saida_txt = "clean_subtitles/legenda_limpa.txt"
caminho_vtt = "subtitles_extracted/video_temp.pt.vtt"

URL = input("Cole a URL do video do YouTube: ")

print("\n🎥 Baixando legenda...")
legenda_path = baixar_legenda(URL)

print("🧹 Limpando legenda...")
print("🛠️ Abrindo arquivo:", caminho_vtt)
with open(legenda_path, 'r', encoding='utf-8') as f:
    legenda_raw = f.read()
legenda_limpa = limpar_vtt(caminho_vtt, caminho_saida_txt)

print("🤖 Resumindo com IA...")
resumo = resumir_texto()

print("📄 RESUMO:")
with open(f"summaries/{nome_arquivo}", "r", encoding="utf-8") as f:
    resumo = f.read()
print(resumo)

print("\n✅ Resumo salvo na pasta Summaries")

os.remove("clean_subtitles/legenda_limpa.txt")
os.remove("subtitles_extracted/video_temp.pt.vtt")