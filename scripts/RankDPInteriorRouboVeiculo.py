import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc
from tabulate import tabulate

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

RankDP = sessao.query(
    oc.dp.nome,
    sa.func.sum(oc.ocorrencias.quantidade),
    oc.municipio.regiao
).join(
    oc.ocorrencias,
    oc.ocorrencias.cod_dp == oc.dp.cod_dp
).join(
    oc.municipio,
    oc.ocorrencias.cod_ibge == oc.municipio.cod_ibge
).where(
    oc.municipio.regiao == "Interior",
    sa.or_(oc.ocorrencias.ocorrencia == "furto_veiculos", oc.ocorrencias.ocorrencia == "roubo_veiculos")
).order_by(
    sa.func.sum(oc.ocorrencias.quantidade).desc()
).group_by(
    oc.dp.nome
).all()

print(tabulate(RankDP, headers=["Delegacia de Polícia", "Quantidade Total", "Região DP"], tablefmt="grid"))