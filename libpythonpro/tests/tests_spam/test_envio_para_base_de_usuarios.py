from unittest.mock import Mock

from libpythonpro.spam.main import EnviadorDeSpam
import pytest

from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Mateus', email='mateuslourenco55@outlook.com'),
            Usuario(nome='Rafael', email='mateuslourenco55@outlook.com')
        ],
        [
            Usuario(nome='Mateus', email='mateuslourenco55@outlook.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Mateus', email='mateuslourenco55@outlook.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'karpen@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'karpen@outlook.com',
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
