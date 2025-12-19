
import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///BD/vendas.db")

base = orm.declarative_base()

#Tabela cliente

class clientes(base):
    __tablename__ = "clientes"

    cpf = sa.Column(sa.CHAR(14), primary_key = True, index = True)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)
    genero = sa.Column(sa.CHAR(1))
    salario = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#Tabela fornecedor

class fornecedores(base):
    __tablename__ = "fornecedores"

    registro_fornecedor = sa.Column(sa.INTEGER, primary_key = True, index = True)
    nome_fantasia = sa.Column(sa.VARCHAR(100), nullable = False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable = False)
    cidade = sa.Column(sa.VARCHAR(50), nullable = False)
    uf = sa.Column(sa.CHAR(2), nullable = False)


#Tabela produto

class produtos(base):
    __tablename__ = "produtos"

    codigo_de_barras = sa.Column(sa.INTEGER, primary_key = True, index = True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey("fornecedores.registro_fornecedor", ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    dscProduto = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))

#Tabela vendedores

class vendedores(base):
    __tablename__ = "vendedores"

    registro_vendedor = sa.Column(sa.INTEGER, primary_key = True, index = True)
    cpf = sa.Column(sa.CHAR(14), nullable = False)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)
    genero = sa.Column(sa.CHAR(1))

#Tabela vendas

class vendas(base):
    __tablename__ = "vendas"

    id_transacao = sa.Column(sa.INTEGER, primary_key = True, index = True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("clientes.cpf",ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("vendedores.registro_vendedor",ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)
    codigo_de_barras = sa.Column(sa.INTEGER, sa.ForeignKey("produtos.codigo_de_barras",ondelete = "NO ACTION", onupdate = "CASCADE"), index = True)

try:
    base.metadata.create_all(engine) #Criar tabelas
    print("Tabelas criadas!")
except ValueError:
    ValueError()