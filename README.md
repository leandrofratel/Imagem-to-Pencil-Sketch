# Image-to-Pencil-Sketch

Pipeline de Engenharia de Dados para processamento de imagens utilizando **OpenCV**, transformando fotografias coloridas em imagens que simulam desenhos feitos a lápis (*Pencil Sketch*).

*Desafio proposto pela StrataScratch:* https://platform.stratascratch.com/data-projects/image-pencil-sketch

---

# 📖 Sobre o projeto

Este projeto tem como objetivo desenvolver um pipeline de processamento de imagens seguindo conceitos de **Engenharia de Dados**.

A aplicação recebe imagens armazenadas na camada **Raw**, realiza a extração de metadados, aplica uma sequência de transformações utilizando a biblioteca **OpenCV** e salva as imagens processadas na camada **Silver**.

Embora o resultado final seja uma imagem com efeito *Pencil Sketch*, o principal objetivo do projeto é demonstrar a construção de um pipeline organizado, modular e reutilizável, separando as etapas de **Extração (Extract)**, **Transformação (Transform)** e **Carga (Load)**.

---

# 🎯 Problema

Processar imagens manualmente pode ser uma tarefa repetitiva e pouco escalável quando existe um grande volume de arquivos.

Este projeto resolve esse problema automatizando todo o fluxo de processamento, permitindo que diversas imagens sejam transformadas de maneira padronizada por meio de um pipeline.

Além da transformação da imagem, o projeto também realiza a coleta de metadados, possibilitando maior rastreabilidade e organização dos arquivos processados.

---

# ⚙️ Objetivos

* Construir um pipeline de processamento de imagens.
* Aplicar conceitos de Engenharia de Dados.
* Organizar o projeto em camadas.
* Automatizar o processamento de múltiplas imagens.
* Extrair metadados dos arquivos.
* Aplicar o efeito **Pencil Sketch** utilizando OpenCV.

---

# 🖼️ Transformações aplicadas

O processamento segue a sequência proposta pelo desafio:

1. Conversão da imagem RGB para escala de cinza (*Grayscale*).
2. Inversão da imagem em escala de cinza (*Negative*).
3. Aplicação de um filtro de desfoque (*Gaussian Blur*).
4. Combinação da imagem em escala de cinza com a imagem invertida e desfocada.
5. Geração da imagem com aparência de desenho feito a lápis.

---

# 📂 Estrutura do projeto

```text
IMAGE_TO_PENCIL_SKETCH/
│
├── data/
│   ├── raw/
│   │   └── Imagens originais
│   │
│   └── silver/
│       ├── Imagens processadas
│       └── metadata.parquet
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── validation.py
│
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🔄 Pipeline

```text
Raw Images
      │
      ▼
Extract
      │
      ├── Localização das imagens
      ├── Leitura dos arquivos
      └── Coleta de metadados
      │
      ▼
Transform
      │
      ├── Grayscale
      ├── Negative
      ├── Gaussian Blur
      └── Pencil Sketch
      │
      ▼
Load
      │
      ├── Salvamento da imagem
      └── Registro dos metadados
      │
      ▼
Silver
```

---

# 🛠️ Tecnologias

* Python
* OpenCV
* NumPy
* Pathlib
* Pandas
* UV

---

# 📁 Camadas de dados

## Raw

Armazena as imagens originais sem qualquer modificação.

## Silver

Armazena as imagens processadas e os metadados gerados durante a execução do pipeline.

---

# 📌 Aprendizados

Durante este projeto são explorados conceitos como:

* Organização de pipelines de dados.
* Processamento de imagens com OpenCV.
* Estruturação em camadas (Raw e Silver).
* Modularização do código.
* Separação das etapas de ETL.
* Coleta de metadados.
* Manipulação de arquivos utilizando `pathlib`.
