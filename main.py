from apiclient import configurar_api, gerar_conteudo
from database import conectar_banco, inserir_documento
import os


def get_files(path):
    pdf_files = []
    for pasta_atual, subpastas, arquivos in os.walk(path):
        for arquivo in arquivos:
            if arquivo.endswith(".pdf"):
                pdf_path = os.path.join(pasta_atual, arquivo)
                pdf_files.append(pdf_path)
    return pdf_files


def main():
    pdf_directory = None  # Insira aqui o path do diretório onde estão os arquivos PDF

    model = configurar_api()
    pdf_files = get_files(pdf_directory)

    for pdf_file in pdf_files:
        try:
            document = gerar_conteudo(model, pdf_file)
        except Exception as e:
            print(f"Erro ao processar o conteúdo do documento: {e}")
            continue

        conn, cursor = conectar_banco()

        try:
            inserir_documento(cursor, conn, document)
        except Exception as e:
            print(f"Erro ao inserir documento no banco de dados: {e}")
        finally:
            conn.close()


if __name__ == "__main__":
    main()
