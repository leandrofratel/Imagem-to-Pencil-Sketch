"""Camada responsável por realzar o processamento das imagens
"""
#%%
from extract import ImageExtractor, RAW_DATA
import cv2

#%%
class ImageTransform:
    """Aplica as transformações da imagem para 
    reproduzir o efeito Pencil Sketch."""

    def converter_para_cinza(self, matriz):
        """Recebe um `numpy.ndarray` e 
        converte para a escala de cinza"""
        cinza = cv2.cvtColor(matriz, cv2.COLOR_BGR2GRAY)
        return cinza

    def inverter_imagem(self, matriz):
        """Converte a imagem em negativo."""
        negativo = cv2.bitwise_not(matriz)
        return negativo

    def aplicar_desfoque(self, matriz):
        """Aplicação do filtro Gaussiano para suavização do brilho
        e desfoque da imagem."""
        desfoque = cv2.GaussianBlur(matriz, (5,5), 0)
        return desfoque

    def criar_pencil_sketch(self):
        ...

    def transformar(self):
        """Orquestrar a sequência de execuções"""
        ...


#! Exemplo de execução do Fluxo
#%%
extractor = ImageExtractor(RAW_DATA)
matriz = extractor.extrair()

transform = ImageTransform()
resultado = transform.converter_para_cinza(matriz)

# %%
