import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")
sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

RankMunicipio = pd.DataFrame(
    sessao.query(
        oc.municipio.municipio.label("Munícipio"),
        sa.func.sum(oc.ocorrencias.quantidade).label("Quantidade de ocorrências"),
    )
    .join(oc.ocorrencias, oc.ocorrencias.cod_ibge == oc.municipio.cod_ibge)
    .where(oc.ocorrencias.ocorrencia == "roubo_veiculo")
    .group_by(oc.municipio.municipio)
    .order_by(sa.func.sum(oc.ocorrencias.quantidade).desc())
    .all()
)

print(RankMunicipio)
