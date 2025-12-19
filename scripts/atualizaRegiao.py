import sqlalchemy as sa
import ocorrencias as oc

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")

metadado = sa.MetaData()
metadado.reflect(bind=engine)

tbMunicipio = metadado.tables[oc.municipio.__tablename__]

atualiza_regiao = sa.update(tbMunicipio).values(
    {"cod_ibge":"3304557"}
).where(
    tbMunicipio.c.cod_ibge == "2"
)

try:
    with engine.connect() as conn:
        conn.execute(atualiza_regiao)
        conn.commit()
    print("Dados atualizados com sucesso!")
except Exception as e:
    print(f"Erro ao atualizar os dados: {e}")

'''
## SUGESTÃO DO GPT FORMA ATUALIZADO DO SQL ALCHEMY

from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///BD/ocorrencias.db", future=True)

atualiza_regiao = text("""
    UPDATE municipio
    SET regiao = 'Capital'
    WHERE nome_municipio = 'Porto Alegre'
""")

try:
    with engine.connect() as conn:
        conn.execute(atualiza_regiao)
        conn.commit()
    print("Dados atualizados com sucesso!")
except Exception as e:
    print(f"Erro ao atualizar os dados: {e}")

'''