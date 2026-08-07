from extract import ImageExtractor
from transform import ImageTransform
from pathlib import Path

# Execução
RAW_DATA = Path("../data/raw")
extractor = ImageExtractor(RAW_DATA)
registros = extractor.extrair()
