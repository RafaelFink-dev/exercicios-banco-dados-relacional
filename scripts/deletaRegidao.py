import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")

metadado = sa.MetaData()
metadado.reflect(bind=engine)

tbMunicipio = metadado.tables[oc.municipio.__tablename__]

atualiza_regiao = sa.delete(tbMunicipio).where(
    tbMunicipio.c.regiao == "Rio Grande do Sul"
)

try:
    with engine.connect() as conn:
        conn.execute(atualiza_regiao)
        conn.commit()
    print("Dados deletados com sucesso!")
except Exception as e:
    print(f"Erro ao deletar os dados: {e}")