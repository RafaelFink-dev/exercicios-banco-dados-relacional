# Importação de bibliotecas
import pandas as pd                      # Biblioteca para leitura e manipulação de dados
import sqlalchemy as sa                  # Biblioteca para conexão com o banco de dados (SQLAlchemy Core)
import sqlalchemy.orm as orm             # ORM para uso com SQLAlchemy
import ocorrencias as oc                 # Módulo com os modelos ORM das tabelas (dp, municipio, responsavel_dp, ocorrencias)

# Caminho dos arquivos de entrada
endereco = "E:\\Pessoal\\Faculdade\\PUCRS\\Banco de dados Relacional\\projetos\\arquivos\\"

# Leitura dos arquivos de dados
dp = pd.read_csv(endereco + "DP.csv", sep = ",")                         # Dados das delegacias
municipio = pd.read_csv(endereco + "Municipio.csv", sep = ",")           # Dados dos municípios
responsavelDP = pd.read_excel(endereco + "ResponsavelDP.xlsx")           # Dados dos responsáveis pelas DPs
ocorrencias = pd.read_excel(endereco + "ocorrencias.xlsx")               # Dados das ocorrências

# Conversão dos dados lidos para DataFrames
tbDP = pd.DataFrame(dp)
tbMunicipio = pd.DataFrame(municipio)
tbResponsavelDp = pd.DataFrame(responsavelDP)
tbOcorrencias = pd.DataFrame(ocorrencias)

# Criação do engine de conexão com o banco SQLite
engine = sa.create_engine("sqlite:///BD/ocorrencias.db")

# Reflexão (leitura) da estrutura do banco de dados já existente
metadata = sa.MetaData()
metadata.reflect(bind=engine)

# Mapeamento das tabelas do banco usando os nomes definidos nos modelos do módulo 'ocorrencias'
tabela_dp = sa.Table(oc.dp.__tablename__, metadata, autoload_with=engine)
tabela_Municipio = sa.Table(oc.municipio.__tablename__, metadata, autoload_with=engine)
tabela_ResponsavelDp = sa.Table(oc.responsavel_dp.__tablename__, metadata, autoload_with=engine)
tabela_Ocorrencias = sa.Table(oc.ocorrencias.__tablename__, metadata, autoload_with=engine)

# Conversão dos DataFrames em listas de dicionários (cada dicionário representa uma linha da tabela)
dadosDp = tbDP.to_dict(orient="records")
dadoMunicipio = tbMunicipio.to_dict(orient="records")
dadosResp = tbResponsavelDp.to_dict(orient="records")
dadosOcorrencia = tbOcorrencias.to_dict(orient="records")

# Inserção dos dados no banco de dados usando uma transação
try:
    with engine.begin() as conn:  # Início da transação
        # Inserção em lote (bulk insert) para cada tabela
        conn.execute(tabela_dp.insert(), dadosDp)                  #type: ignore
        conn.execute(tabela_Municipio.insert(), dadoMunicipio)     #type: ignore
        conn.execute(tabela_ResponsavelDp.insert(), dadosResp)     #type: ignore
        conn.execute(tabela_Ocorrencias.insert(), dadosOcorrencia) #type: ignore

    # Se tudo der certo, exibe essa mensagem
    print("Dados inseridos na tabela com sucesso!")
except Exception as e:
    # Se algum erro ocorrer, será exibido aqui
    print("Erro ao inserir dados nas tabelas:", e)
