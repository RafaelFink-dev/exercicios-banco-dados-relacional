import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

endereco = "E:\\Pessoal\\Faculdade\\PUCRS\\Banco de dados Relacional\\projetos\\arquivos\\"

vendedor = pd.read_csv(endereco + "vendedor.csv", sep = ";")

tbVendedor = pd.DataFrame(vendedor)

engine = sa.create_engine("sqlite:///BD/vendas.db")

sessao = orm.sessionmaker(bind = engine)
sessao = sessao()

tbVendedor['registro_vendedor'] = tbVendedor['registro_vendedor'].astype(int)
#Garantindo que seja INT

#Abordagem inserção - 1
for i in range(len(tbVendedor)):
    dados_vendedor = vd.vendedores(
        registro_vendedor = int(tbVendedor['registro_vendedor'][i]),
        cpf = tbVendedor['cpf'][i],
        nome = tbVendedor['nome'][i],
        genero = tbVendedor['genero'][i],
        email = tbVendedor['email'][i]
    )

    try:
        sessao.add(dados_vendedor)
        sessao.commit()
    except ValueError:
        ValueError()

print("Dados inseridos na tabela com sucesso na tabela vendedor!")

#Abordagem inserção - 2 - Mais rapido

produtos = pd.read_excel(endereco + "produto.xlsx")
tbProdutos = pd.DataFrame(produtos)

metadata = sa.MetaData()
metadata.reflect(bind=engine)

tabela_produto = sa.Table(vd.produtos.__tablename__, metadata, autoload_with=engine)

dadosProduto = tbProdutos.to_dict(orient="records")

try:
    with engine.begin() as conn:
        conn.execute(tabela_produto.insert(), dadosProduto) #type: ignore
    print("Dados inseridos na tabela com sucesso na tabela produtos!")
except Exception as e:
    print("Erro ao inserir dados na tabela produtos:", e)



