"""
Este módulo implementa a etapa de Transformação (Transform) do pipeline ETL,
aplicando uma sequência de operações OpenCV para gerar o efeito Pencil Sketch.
"""

import cv2

class ImageTransform:
    """Aplica as transformações da imagem para
    reproduzir o efeito Pencil Sketch."""

    def converter_para_cinza(self, matriz):
        """Recebe um `numpy.ndarray` e
        converte para a escala de cinza."""
        return cv2.cvtColor(matriz, cv2.COLOR_BGR2GRAY)

    def inverter_imagem(self, matriz):
        """Converte a imagem em negativo."""
        return cv2.bitwise_not(matriz)

    def aplicar_desfoque(self, matriz, kernel=(5,5)):
        """Aplicação do filtro Gaussiano para suavização do brilho
        e desfoque da imagem."""
        return cv2.GaussianBlur(matriz, kernel, 0)

    def criar_pencil_sketch(
            self, imagem_cinza, 
            imagem_desfocada_invertida, 
            scale: float = 256.0
    ):
        """Combina a imagem cinza com a invertida+desfocada 
        para criar o efeito sketch."""
        return cv2.divide(
            imagem_cinza,
            255 - imagem_desfocada_invertida,
            scale=scale,
            dtype=cv2.CV_8U
        )

    def transformar(self, matriz_bgr):
        """Executa o pipeline completo de transformação Pencil Sketch."""
        imagem_cinza = self.converter_para_cinza(matriz_bgr)
        imagem_invertida = self.inverter_imagem(imagem_cinza)
        imagem_desfocada_invertida = self.aplicar_desfoque(imagem_invertida)

        # Criar desenho.
        imagem_sketch = self.criar_pencil_sketch(imagem_cinza, imagem_desfocada_invertida)
        return imagem_sketch
