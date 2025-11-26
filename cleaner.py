import re

# ==========================
#         CONSTANTES
# ==========================

ENCODING_PADRAO = "utf-8"

REGEX_WEBVTT_HEADER = r"WEBVTT.*?\n+"
REGEX_KIND = r"Kind:.*?\n+"
REGEX_LANGUAGE = r"Language:.*?\n+"
REGEX_LINHAS_TEMPO = r"\d\d:\d\d:\d\d\.\d+ --> .*?\n"
REGEX_TAGS = r"<.*?>"
REGEX_LINHAS_BRANCAS_DUPLAS = r"\n{2,}"
REGEX_NUMERO_SOZINHO = r"^\s*\d+\s*$"

CAMINHO_SAIDA_PADRAO = "clean_subtitles/legenda_limpa.txt"
MENSAGEM_SUCESSO = "✅ Legenda limpa salva em: clean_subtitles"

# ==========================
#       FUNÇÃO PRINCIPAL
# ==========================

def limpar_vtt(caminho_vtt: str, caminho_saida_txt: str = CAMINHO_SAIDA_PADRAO):
    with open(caminho_vtt, "r", encoding=ENCODING_PADRAO) as f:
        conteudo = f.read()

    # Remove cabeçalhos e metadados
    conteudo = re.sub(REGEX_WEBVTT_HEADER, "", conteudo, flags=re.DOTALL)
    conteudo = re.sub(REGEX_KIND, "", conteudo)
    conteudo = re.sub(REGEX_LANGUAGE, "", conteudo)

    # Remove linhas de tempo
    conteudo = re.sub(REGEX_LINHAS_TEMPO, "", conteudo)

    # Remove tags tipo <...>
    conteudo = re.sub(REGEX_TAGS, "", conteudo)

    # Remove linhas em branco duplicadas
    conteudo = re.sub(REGEX_LINHAS_BRANCAS_DUPLAS, "\n", conteudo)

    # Remove números isolados que sobram das legendas
    conteudo = re.sub(REGEX_NUMERO_SOZINHO, "", conteudo, flags=re.MULTILINE)

    # Junta tudo em um único parágrafo
    texto_limpo = conteudo.replace("\n", " ").strip()

    # Salva arquivo de saída
    with open(caminho_saida_txt, "w", encoding=ENCODING_PADRAO) as f:
        f.write(texto_limpo)

    print(MENSAGEM_SUCESSO)
    return texto_limpo
