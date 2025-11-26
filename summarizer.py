from google import genai
import time

# ==========================
#         CONSTANTES
# ==========================

ARQUIVO_LEGENDA = "clean_subtitles/legenda_limpa.txt"
PASTA_SUMMARIES = "summaries"
MODELO_IA = "gemini-2.5-flash"
PROMPT_RESUMO = (
    "Faça um resumo da seguinte transcrição de um vídeo em português, "
    "separe por tópicos: Resumo, Destaques e uma curta Análise "
    "(ignore a repetição de palavras desnecessárias):\n\n"
)

nome_arquivo = f"resumo_{int(time.time())}.txt"

# ==========================
#      INICIALIZA CLIENTE
# ==========================

client = genai.Client()

# ==========================
#       FUNÇÃO RESUMO
# ==========================

def resumir_texto():
    # Lê o conteúdo da legenda limpa
    with open(ARQUIVO_LEGENDA, "r", encoding="utf-8") as f:
        texto_original = f.read()

    # Gera o resumo com Gemini
    response = client.models.generate_content(
        model=MODELO_IA,
        contents=f"{PROMPT_RESUMO}{texto_original}"
    )

    # Extrai o resumo do objeto de resposta
    resumo = response.text

    # Salva o resumo
    caminho_saida = f"{PASTA_SUMMARIES}/{nome_arquivo}"
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write(resumo)
