"""Camada responsável por receber os as imagens e coletar os metadados
"""

from datetime import datetime
from pathlib import Path
import numpy
import cv2

class ImageExtractor:
    """Extrai os caminhos de arquivos de imagem de uma pasta RAW."""
    # Definição das extensões

    def __init__(self, raw_path: Path):
        """Guarda onde está a camada RAW"""
        self.raw_path = raw_path
        self.EXTENSOES_VALIDAS = {
            ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"
        }

    def listar_imagens(self) -> list[Path]:
        """Retorna uma lista contendo apenas os :class:`pathlib.Path`
        de arquivos de imagem presentes em ``self.raw_path``."""
        lista_de_imagens = []
        # Percorre todos os itens da pasta
        for img in sorted(self.raw_path.iterdir()):
            # Verificar se a extensão é válida e adiciona à lista vazia
            if img.is_file() and img.suffix.lower() in self.EXTENSOES_VALIDAS:
                lista_de_imagens.append(img)
        return lista_de_imagens

    def carregar_imagem(self, caminho_imagem: Path) -> numpy.ndarray:
        """Recebe um `Path` e retorna a imagem carregada em memória."""
        # Receber o arquivo e converter em matriz
        imagem = cv2.imread(str(caminho_imagem))
        # Verificr se a leitura foi bem-sucedida (!= None)
        if imagem is None:
            raise ValueError(f"Erro ao carregar imagem {caminho_imagem}")
        # Retornar a matriz de imagem
        return imagem

    def coletar_metadados(self, caminho: Path, imagem) -> dict:
        """Recebe o `Path` e coleta os metadados da matriz 
        e do arquivo de imagem."""
        altura, largura = imagem.shape[:2]
        # Verifica se a imagem possui canal RGB/BGR
        canais = 1 if imagem.ndim == 2 else imagem.shape[2]

        # Armazena as estatisticas das imagens, evita novas chamadas
        estatisticas = caminho.stat()

        metadados_imagem = {
            "altura": altura,
            "largura": largura,
            "canais": canais,
            "dtype": str(imagem.dtype),
            "ndim": imagem.ndim,
            "shape": imagem.shape
        }

        metadados_arquivo = {
            "nome_arquivo": caminho.name,
            "nome_sem_extensao": caminho.stem,
            "extensao": caminho.suffix,
            "pasta": str(caminho.parent),
            "tamanho_bytes": estatisticas.st_size,
            "data_modificacao": datetime.fromtimestamp(
                estatisticas.st_mtime # 2026-08-01 14:52:17
            ) 
        }

        return { # Desenpacotamento e agregação dos dicionários
            **metadados_arquivo, 
            **metadados_imagem
        }

    def extrair(self) -> list:
        """Orquestra a sequência de execução dos métodos da classe."""
        # Lista que armazenará todos os registros
        registros = []
        # Percorre todas as imagens da RAW
        for caminho in self.listar_imagens():
            imagem = self.carregar_imagem(caminho)
            metadados = self.coletar_metadados(caminho, imagem)

            registro = {
                "caminho": caminho,
                "matriz": imagem,
                "metadados": metadados
            }
            # Adiciona o regitro a lista
            registros.append(registro)

        return registros

if __name__=="__main__":
    extrator = ImageExtractor(Path("data/raw"))
    registros = extrator.extrair()
    print(f"Extraidos {len(registros)} registros")
    for r in registros[:3]:
        print(f" -{r['metadados']['nome_arquivo']}: {r['matriz'].shape}")