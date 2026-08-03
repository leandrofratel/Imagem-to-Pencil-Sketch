"""Camada responsável por realzar o processamento das imagens
"""

class ImageTransform:
    """Aplica as transformações da imagem para reproduzir o efeito Pencil Sketch."""

    def converter_para_cinza(self) -> dict:
        """Recebe um `numpy.ndarray` e converte para a escala de cinza"""
        ...

    def inverter_imagem(self):
        ...

    def aplicar_desfoque(self):
        ...

    def criar_pencil_sketch(self):
        ...

    def transformar(self):
        """Orquestrar a sequência de execuções"""
        ...

#%%
#! Exemplo de execução do Fluxo
"""
extractor = ImageExtractor(RAW_DATA)
dados = extractor.extrair()

transform = ImageTransform()
resultado = transform.transformar(dados)
"""