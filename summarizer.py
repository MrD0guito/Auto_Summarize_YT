from google import genai
import time

nome_arquivo = f"resumo_{int(time.time())}.txt"

# Inicializa o cliente
client = genai.Client()

def resumir_texto():
    # Lê o conteúdo do arquivo de entrada
    with open("clean_subtitles/legenda_limpa.txt", "r", encoding="utf-8") as f:
        texto_original = f.read()

    # Gera o resumo com Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Faça um resumo da seguinte transcrição de um vídeo em português, separe por tópicos: Resumo, Destaques e uma curta Análise (ignore a repetição de palavras desnecessárias):\n\n{texto_original}"
    )

    # Extrai o resumo do objeto de resposta
    resumo = response.text
    
    # Salva o resumo em uma nova pasta chamada summaries
    with open(f"summaries/{nome_arquivo}", "w", encoding="utf-8") as f: 
        f.write(resumo)
