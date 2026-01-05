from Controller import carregar_e_criar_alunos    
from SendEmail import SendEmail    

def gerar_mensagem(aluno):
    mensagem = f"Olá {aluno.nome}, \n\n"
    
    if len(aluno.cursos) > 1:
        mensagem += "Segue em anexo os certificados dos cursos concluídos:\n"
    else:
        mensagem += "Segue em anexo o certificado do curso concluído:\n"
    for curso in aluno.cursos:
        mensagem += f"- {curso.nome}\n"
        
    mensagem += (
        "\nO Projeto Beira Linha espera que tenha gostado do curso "
        "e te convida para participar novamente no próximo semestre!\n\n"
        "Caso ainda não tenha preenchido a pesquisa de satisfação, pedimos que o faça por meio do link abaixo: \n"
        "https://forms.office.com/r/07V2pzxSqV\n\n"
        "Esse feedback nos ajuda a melhorar cada vez mais os cursos!\n\n"
        
        "Atenciosamente, \n\n"
        "Equipe Beira Linha"
    )
    return mensagem

if __name__ == "__main__":
    alunos = carregar_e_criar_alunos("Certificados BL.xlsx")
    
    if not alunos:
        print("Nenhum aluno encontrado.")
        exit()

    bot = SendEmail()

    envios_erros = []
    
    for aluno in alunos:
        try:
            mensagem = gerar_mensagem(aluno)
            bot.enviar_email(aluno, mensagem)
        except Exception as e:
            envios_erros.append((aluno, str(e)))

print("\nPROCESSO FINALIZADO")

if not envios_erros:
    print("Todos os e-mails foram enviados com sucesso!")
else:
    print(f"{len(envios_erros)} envio(s) falharam.")

    with open("envios_com_erro.log", "w", encoding="utf-8") as f:
        for aluno, erro in envios_erros:
            f.write(
                f"{aluno.nome} | "
                f"{', '.join(aluno.emails)} | "
                f"{erro}\n"
            )
