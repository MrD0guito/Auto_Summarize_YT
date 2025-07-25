# 🧠 AutoResumo - Resumos por IA a partir de Vídeos

O **AutoResumo** é um projeto que transforma vídeos em resumos automáticos utilizando técnicas de pré-processamento e inteligência artificial. Basta fornecer o link de um vídeo com legendas embutidas para obter um resumo limpo, direto e coeso.

## 📌 Funcionalidades

- 🧹 Limpeza automática de arquivos `.vtt` (remoção de timestamps, repetições e linhas quebradas).
- 📝 Extração e reconstrução do texto contínuo da legenda.
- 🤖 Resumo do conteúdo utilizando modelos de linguagem (IA).
- 💬 Geração de texto pronto para leitura, estudo ou compartilhamento.
  
## 🏗️ Tecnologias Utilizadas

- Python 3.12.4
- `Gemini` (API)
- Manipulação de arquivos `re`
- API do Gemini para geração de resumos

## 🚀 Como usar

### 1. Configure sua API Key da GEMINI

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
GEMINI_API_KEY=sua-chave-aqui
```

### 2. Execute o projeto

```bash
python main.py
```

## 📌 Exemplo de Uso

1. Copia o link do vídeo e cola no programa.
2. O programa remove os timestamps, setas e duplicações.
3. O texto é reconstruído como parágrafo contínuo.
4. A IA lê esse texto e entrega um resumo automático.

---

## 🧠 Idealizado por

Gabriel Gatto (MrDoguito) — apaixonado por automação, IA, tecnologia e criatividade.
