
import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BD/ocorrencias.db")

base = orm.declarative_base()

#Tabela DP

class dp(base):
    __tablename__ = "DP"
    cod_dp = sa.Column(sa.INTEGER, primary_key = True, index = True)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    endereco = sa.Column(sa.VARCHAR(255), nullable = False)

#Tabela responsavelDP

class responsavel_dp(base):
    __tablename__ = "responsavel_dp"

    cod_dp = sa.Column(sa.INTEGER, primary_key = True, index = True)
    delegado = sa.Column(sa.VARCHAR(100), nullable = False)

#Tabela municipio

class municipio(base):
    __tablename__ = "municipio"

    cod_ibge = sa.Column(sa.INTEGER, primary_key = True, index = True)
    municipio = sa.Column(sa.VARCHAR(100), nullable = False)
    regiao = sa.Column(sa.VARCHAR(100), nullable = False)

#Tabela ocorrencias

class ocorrencias(base):
    __tablename__ = "ocorrencias"

    id_registro = sa.Column(sa.INTEGER, primary_key = True, index = True)
    cod_dp = sa.Column(sa.INTEGER, sa.ForeignKey("DP.cod_dp", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    cod_ibge = sa.Column(sa.INTEGER, sa.ForeignKey("municipio.cod_ibge", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    ano = sa.Column(sa.CHAR(4), nullable = False)
    mes = sa.Column(sa.CHAR(2), nullable = False)
    ocorrencia = sa.Column(sa.VARCHAR(100), nullable = False)
    quantidade = sa.Column(sa.INTEGER, nullable = False)

try:
    base.metadata.create_all(engine) #Criar tabelas
    print("Tabelas criadas!")
except ValueError:
    ValueError()