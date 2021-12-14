from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido

import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'mateusalourenco@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'mateuslourenco55@outlook.com',
        'Cursos Python Pro',
        'Primeira turma Guido'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'mateusalourenco.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'mateuslourenco55@outlook.com',
            'Cursos Python Pro',
            'Primeira turma Guido'
        )
