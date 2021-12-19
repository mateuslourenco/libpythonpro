from libpythonpro.spam.enviador_de_email import Enviador
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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Mateus', email='mateuslourenco55@outlook.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'karpen@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'karpen@outlook.com',
        'mateuslourenco55@outlook.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
