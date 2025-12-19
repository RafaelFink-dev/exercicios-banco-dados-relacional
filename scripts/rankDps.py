import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

RankDP = pd.DataFrame(
    sessao.query(
        oc.dp.nome.label("DP - Delegacia de Polícia"),
        sa.func.sum(oc.ocorrencias.quantidade).label("Total de ocorrências"),
    )
    .join(oc.ocorrencias, oc.ocorrencias.cod_dp == oc.dp.cod_dp)
    .join(oc.municipio, oc.ocorrencias.cod_ibge == oc.municipio.cod_ibge)
    .where(oc.municipio.regiao == "Capital")
    .group_by(oc.dp.nome)
    .order_by(sa.func.sum(oc.ocorrencias.quantidade).desc())
    .all()
)

print(RankDP)

## NÃO RETORNOU NADA PORQUE O CODIGBE NAO TA CADASTRADO CERTO NOS ARQUIVOS QUE O PROFESSOR RETORNOU MAS A LOGICA É ESSA