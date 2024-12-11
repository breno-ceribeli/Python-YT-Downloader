# YouTube Downloader

Este projeto é um script em Python para baixar vídeos do YouTube, com a opção de baixar apenas o áudio. Ele utiliza a biblioteca `pytubefix` como alternativa à biblioteca `pytube`, pois a original não estava funcionando no momento da implementação.

---

## Requisitos

- Python 3.7 ou superior
- Biblioteca `pytubefix`

---

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/breno-ceribeli/Python-YT-Downloader.git
   cd Python-YT-Downloader
   ```

2. Instale a biblioteca `pytubefix`:
   ```bash
   pip install pytubefix
   ```

---

## Como usar

1. Execute o script:
   ```bash
   python yt_downloader.py
   ```

2. Insira a URL do vídeo que você deseja baixar.

   - Para baixar o vídeo com a melhor resolução:
     ```
     https://www.youtube.com/watch?v=VIDEO_ID
     ```

   - Para baixar apenas o áudio:
     ```
     https://www.youtube.com/watch?v=VIDEO_ID audio
     ```

---

## Estrutura do Código

- O script utiliza `pytubefix` para lidar com mudanças frequentes no YouTube que quebraram a biblioteca `pytube` original.
- O progresso do download é exibido usando o callback `on_progress` fornecido pela biblioteca.
- Dependendo do input do usuário, o script:
  - Baixa o vídeo com a melhor resolução disponível.
  - Ou baixa apenas o áudio do vídeo.

---

## Tratamento de Erros

- Caso o download falhe, uma mensagem de erro será exibida no console.

Exemplo:
```bash
Ocorreu um erro: ["descrição do erro"]
```

---

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

---

## Créditos

Este projeto utiliza a biblioteca [`pytubefix`](https://github.com/JuanBindez/pytubefix), uma alternativa à biblioteca [`pytube`](https://github.com/pytube/pytube/tree/master) para lidar com mudanças recentes no YouTube.
