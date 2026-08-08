
from extract import ImageExtractor
from transform import ImageTransform
from load import Imageloader
from pathlib import Path

# Exemplo de execução
RAW_DATA = Path("../data/raw")
extractor = ImageExtractor(RAW_DATA)
registros = extractor.extrair()


# Exemplo de execução
loader = ImageLoader(Path("data/silver"))

for registro in registros:  # Vem do Extract
    sketch = transformer.transformar(registro["matriz"])

    caminho_saida = loader.salvar_imagem(sketch, registro["metadados"]["nome_sem_extensao"])
    loader.registrar_metadados(registro["metadados"], caminho_saida)

loader.finalizar()  # Salva o parquet consolidado