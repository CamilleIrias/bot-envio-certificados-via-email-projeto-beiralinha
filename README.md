# Projeto Beira Linha - Envio Automático de Certificados por Email

## Descrição
Este projeto automatiza o envio de certificados gerados no semestre pelo Projeto Beira Linha.

Ele lê uma planilha com os dados do aluno, gera mensagens e envia os certificados anexados.

A planilha deve conter as seguintes colunas:
- `Nome`
- `Curso`
- `Email1`
- `Email2`
- `Caminho` (do certificado no projeto)
---
## Pré-requisitos
- Python 3.7+
- Ambiente virtual
---
## Como usar
1. Criar e ativar ambiente virtual:
```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    
    .venv\Scripts\activate     # Windows

2. Instalar dependências:
    pip install -r requirements.txt

3. Criar um arquivo Dados.py com as credenciais de envio (criar com base o DadosExample.py)

4. Colocar planilha Certificados BL.xlsx na raiz do projeto

5. Rodar o script principal:
    python Main.py