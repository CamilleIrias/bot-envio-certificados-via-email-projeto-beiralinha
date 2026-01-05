import pandas as pd
from Models import Aluno, Curso

def extrair_emails(row):
    return [
        row[col].strip()
        for col in ['Email1', 'Email2']
            if col in row and pd.notna(row[col])
    ]

def carregar_e_criar_alunos(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []

    df['Nome'] = df['Nome'].str.strip().str.title()
    
    alunos_dic = {}

    for i, row in df.iterrows():
        nome = row['Nome']
        curso_nome = row['Curso']
        emails = extrair_emails(row)
        caminho_arquivo = row['Caminho']
        
        chave_aluno = (nome, tuple(emails))
        
        if chave_aluno not in alunos_dic:
            aluno = Aluno(nome, emails)
            alunos_dic[chave_aluno] = aluno
        else:
            aluno = alunos_dic[chave_aluno]

        curso = Curso(curso_nome, caminho_arquivo)
        aluno.adicionar_curso(curso)
    
    return list(alunos_dic.values())