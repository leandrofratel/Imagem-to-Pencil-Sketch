"""
Camada reponsável por salvar as imagens transformadas na camada de saída,
incluindo gestão de nomes de arquivo, criação de diretórios e
metadados de processamento.
"""

import cv2
import pandas as pd
from datetime import datetime

class Imageloader:
    def __init__(self, silver_path):
        """..."""
        self.silver_path = silver_path
        self._metadados = []

    def salvar_imagem(self, matriz, nome_arquivo):
        """..."""
        caminho_saida = self.silver_path / nome_arquivo
        return cv2.imwrite(str(caminho_saida), matriz)

    def registrar_metadados(
        self,
        *,
        metadados_origem: dict,           # Vem direto de Extract.coletar_metadados()
        nome_arquivo_saida: str,          # Nome definido no Load (ex: "foto1_sketch.png")
        matriz_processada: "cv2.Mat",     # Para extrair dims finais
        parametros_transformacao: dict[str, Any],
        tempo_execucao_segundos: float,
        status: str = "sucesso",
        mensagem_erro: str | None = None,
    ) -> None:
        """
        Registra metadados combinando o que veio do Extract com info da Load.

        Args:
            metadados_origem: Dicionário retornado por `ImageExtractor.coletar_metadados()`.
                Contém: nome_arquivo, nome_sem_extensao, extensao, pasta, tamanho_bytes,
                data_modificacao, altura, largura, canais, dtype, ndim, shape.
            nome_arquivo_saida: Nome do arquivo salvo em data/silver.
            matriz_processada: Matriz resultante da Transform (para dims finais).
            parametros_transformacao: Parâmetros usados no pipeline de transformação.
            tempo_execucao_segundos: Tempo total de processamento da imagem.
            status: "sucesso" ou "erro".
            mensagem_erro: Preenchido apenas se status == "erro".
        """
        # Extrai dims finais da matriz processada (Load não deve assumir formato)
        altura_final, largura_final = matriz_processada.shape[:2]

        registro = {
            # --- Identificação do arquivo original (do Extract) ---
            "nome_arquivo_original": metadados_origem["nome_arquivo"],
            "nome_sem_extensao": metadados_origem["nome_sem_extensao"],
            "extensao_original": metadados_origem["extensao"],
            "pasta_original": metadados_origem["pasta"],
            "tamanho_original_bytes": metadados_origem["tamanho_bytes"],
            "data_modificacao_original": metadados_origem["data_modificacao"].isoformat()
                if hasattr(metadados_origem["data_modificacao"], "isoformat")
                else str(metadados_origem["data_modificacao"]),

            # --- Dimensões originais (do Extract) ---
            "altura_original": metadados_origem["altura"],
            "largura_original": metadados_origem["largura"],
            "canais_original": metadados_origem["canais"],
            "dtype_original": metadados_origem["dtype"],

            # --- Saída (responsabilidade do Load) ---
            "arquivo_saida": nome_arquivo_saida,
            "caminho_saida": str(self.silver_path / nome_arquivo_saida),
            "altura_final": altura_final,
            "largura_final": largura_final,

            # --- Processamento ---
            "parametros_transformacao": str(parametros_transformacao),
            "tempo_execucao_segundos": tempo_execucao_segundos,
            "timestamp_processamento": datetime.utcnow().isoformat() + "Z",
            "status": status,
            "mensagem_erro": mensagem_erro,
        }

        self._metadados.append(registro)

    def finalizar(self):
        """..."""
        ...


if __name__=="__main__":
    ...