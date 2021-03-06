import pandas as pd
import sqlalchemy

datos = pd.read_csv('/datain/datosDelitos.csv', index_col=0 )
# Create the engine to connect to the PostgreSQL database
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db_delitos:5432/delitos')
# Write data into the table in PostgreSQL database
datos.to_sql('delitos',engine, if_exists= 'append')