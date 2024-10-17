# Document Processor

Este projeto é um processador de documentos que utiliza a API do Google Generative AI para extrair informações de
arquivos PDF, como título, tags, nome do signatário, resumo e tradução. As informações extraídas são armazenadas em um
banco de dados SQLite.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
    - `pydantic`
    - `google.generativeai`
    - `python-dotenv`
    - `sqlite3`

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/document-processor.git
   cd document-processor

2. Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Google:
    ```env
   API_KEY=your_api_key_here
    ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do projeto

- models/Document.py: Contém o modelo de dados DocumentResponse que define a estrutura dos documentos processados.
- api.py: Configura a API do Google e contém funções para gerar conteúdo a partir de arquivos PDF.
- database.py: Gerencia a conexão com o banco de dados SQLite e fornece funções para inserir documentos.
- main.py: O ponto de entrada do programa, que orquestra o processamento dos arquivos PDF.

## Como usar

1. Coloque seus arquivos pdf na pasta desejada:
2. Execute o script main.py:

   ```bash
   python main.py
   ```
   
3. O programa irá:
   - Carregar os arquivos PDF do diretório especificado.
   - Enviar cada arquivo para a API do Google Generative AI para gerar conteúdo.
   - Extrair as informações relevantes e armazená-las no banco de dados SQLite.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.