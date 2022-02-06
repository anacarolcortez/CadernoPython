from models.professor import Professor


if __name__ == "__main__":
    ana = Professor("Ana")
    print(ana)
    ana.mostrar_tarefas()
    ana.busca_perguntas_sem_resposta()
    ana.busca_cursos_do_mes()
