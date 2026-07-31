"""
Extract:
Camada responsável por receber os as imagens e coletar os metadados...
"""
#%% Import da bibliotexas
from pathlib import Path
import cv2

#%%
class ImageExtractor:
    """Extrai os caminhos de arquivos de imagem de uma pasta RAW."""
    # Definição das extensões

    def __init__(self, raw_path: Path):
        """Guarda onde está a camada RAW"""
        self.raw_path = raw_path
        self.EXTENSOES_VALIDAS = {
            ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"
        }

    def listar_imagens(self) -> list:
        """Retorna uma lista contendo apenas os :class:`pathlib.Path`
        de arquivos de imagem presentes em ``self.raw_path``."""
        lista_de_imagens = []
        # Percorre todos os itens da pasta
        for img in sorted(self.raw_path.iterdir()):
            # Verificar se a extensão é válida
            if img.is_file() and img.suffix.lower() in self.EXTENSOES_VALIDAS:
                # adicionar o Path a lista vazia
                lista_de_imagens.append(img)
        # return lista_de_imagens
        return lista_de_imagens

    def carregar_imagem(self, caminho_imagem: Path):
        """Recebe um `Path` e retorna a imagem carregada em memória."""
        # Receber o arquivo e converter em matriz
        imagem = cv2.imread(str(caminho_imagem))
        # Verificr se a leitura foi bem-sucedida (!= None)
        if imagem is None:
            raise ValueError(f"Erro ao carregar imagem {caminho_imagem}")
        # Retornar a matriz de imagem
        return imagem

    def coletar_metadados(self):
        """..."""
        pass

    def funcao_generica(self):
        """..."""
        pass

#%% Execução da Classe
RAW_DATA = Path("../data/raw")
extractor = ImageExtractor(RAW_DATA)

#%% teste Init
extractor.raw_path
#%% teste lista de imagens
imagens = extractor.listar_imagens()
# %%
imagem = extractor.carregar_imagem(imagens[0])
type(imagem)
# %%
