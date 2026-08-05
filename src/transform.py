"""
Este módulo implementa a etapa de Transformação (Transform) do pipeline ETL,
aplicando uma sequência de operações OpenCV para gerar o efeito Pencil Sketch.
"""
#%%
from extract import ImageExtractor, RAW_DATA #! Import de teste, apagar após finalizar a Class.
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
        #! Kernel de (5,5) testar (9,9) ou (21,21)
        desfoque = cv2.GaussianBlur(matriz, (5,5), 0)
        return desfoque

    def criar_pencil_sketch(self,imagem_cinza, imagem_desfocada_invertida, scale: float = 256.0,):
        """Combina a imagem cinza com a invertida+desfocada para criar o efeito lápis.

        A operação matemática é o "Color Dodge" (esquiva de cor):
            resultado = (imagem_cinza * scale) / (255 - imagem_desfocada_invertida)

        Em OpenCV, usa-se `cv2.divide` com parâmetro `scale` para evitar
        divisão por zero e saturação.

        Args:
            imagem_cinza: Imagem original em escala de cinza (H, W), uint8.
            imagem_desfocada_invertida: Imagem negativa com Gaussian Blur (H, W), uint8.
            scale: Fator de escala para a divisão (padrão 256.0).
                Valores maiores = imagem final mais clara/exposta.

        Returns:
            Array NumPy com o efeito Pencil Sketch aplicado (H, W), uint8.

        Example:
            >>> cinza = transform.converter_para_cinza(img)
            >>> negativo = transform.inverter_imagem(cinza)
            >>> desfoque = transform.aplicar_desfoque(negativo)
            >>> sketch = transform.criar_pencil_sketch(cinza, desfoque)
        """
        # TODO: Implementar usando cv2.divide
        # cv2.divide(
        #     src1=imagem_cinza,
        #     src2=255 - imagem_desfocada_invertida,
        #     scale=scale,
        #     dtype=cv2.CV_8U
        # )
        #
        # Alternativa manual (sem OpenCV):
        # denominador = 255 - imagem_desfocada_invertida
        # denominador[denominador == 0] = 1  # evita divisão por zero
        # resultado = (imagem_cinza.astype(np.float32) * scale / denominador).clip(0, 255).astype(np.uint8)
        #
        # Dica: teste scale=256.0 (padrão), 128.0 (mais escuro), 512.0 (mais claro)
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
