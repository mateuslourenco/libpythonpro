from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'mateusalourenco@gmail.com',
        'mateuslourenco55@outlook.com',
        'Cursos Python Pro',
        'Primeira turma Guido'
    )
    assert 'mateuslourenco@gmail.com' in resultado
