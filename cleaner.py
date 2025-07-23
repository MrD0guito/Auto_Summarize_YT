import re

def limpar_vtt(caminho_vtt: str, caminho_saida_txt: str):
    with open(caminho_vtt, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Remove cabeçalhos e metadados
    conteudo = re.sub(r"WEBVTT.*?\n+", "", conteudo, flags=re.DOTALL)
    conteudo = re.sub(r"Kind:.*?\n+", "", conteudo)
    conteudo = re.sub(r"Language:.*?\n+", "", conteudo)

    # Remove linhas de tempo
    conteudo = re.sub(r"\d\d:\d\d:\d\d\.\d+ --> .*?\n", "", conteudo)

    # Remove tags como <c>, <00:00:xx.xxx>
    conteudo = re.sub(r"<.*?>", "", conteudo)

    # Remove linhas em branco duplicadas
    conteudo = re.sub(r"\n{2,}", "\n", conteudo)

    # Remove linhas que só repetem tempo residual
    conteudo = re.sub(r"^\s*\d+\s*$", "", conteudo, flags=re.MULTILINE)

    # Junta tudo em um parágrafo
    texto_limpo = conteudo.replace("\n", " ").strip()

    # Salva como arquivo limpo
    with open("clean_subtitles/legenda_limpa.txt", "w", encoding="utf-8") as f:
        f.write(texto_limpo)

    print("✅ Legenda limpa salva em: clean_subtitles")
    return texto_limpo
