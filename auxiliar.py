from plyer import notification
from datetime import datetime
import pandas as pd
import requests

def alerta(nivel, base, etapa):
    """
    Retorna um alerta no desktop

    :param nivel: Nível do alerta
    :param base: Base onde ocorreu a falha
    :param etapa: Etapa onde ocorreu a falha

    :type nivel: int
    :type base: str
    :type etapa: str
    """

    niveis = {1:"Baixo",
          2: "Médio",
          3: "Alto"}

    if nivel not in niveis:
        raise ValueError(f"Nível inválido. Deve ser 1, 2 ou 3")


    return notification.notify(title=f"ATENÇÃO: Alerta {niveis[nivel]}",
                               message=f"Falha no carregamento da base {base} na etapa {etapa}\n{datetime.now()}")

def get_req(url, base="base"):
    """
    Retorna o JSON de uma requisição a uma API. Em caso de resposta diferente de 200, retorna um alerta.

    :param url: URL da API
    :param base: Nome da base que será criada

    :type url: str
    :type base: str
    """
    # Trata respostas diferentes da esperada (200)
    req = requests.get(url)
    if req.status_code != 200:
        return alerta(1, base, "Extração")
    
    else:
        return req.json()

