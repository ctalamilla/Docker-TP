import pandas as pd
import psycopg2
import sqlalchemy
import warnings
warnings.filterwarnings('ignore')

#conexion por sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5438/delitos')
#conecion por psycopg2
conn = psycopg2.connect(user= 'postgres', password='postgres' ,host='127.0.0.1', port='5438', database='delitos')

### Consultas a la DB
#Pregunta 1: 
#1. Cual es el Barrio con mayor incidencia de delitos. Indicador promedio mensual de delitos. 
consulta1= 'select barrio, round(avg(numeroDelitosMes),0 )as promedioMensual, min(numeroDelitosMes), max(numeroDelitosMes) from(select barrio, anio, mes, count(*) as numeroDelitosMes from delitos d group by barrio, mes, anio order by barrio, anio,mes)as resumen group by barrio order by promedioMensual desc;'
respuesta1= pd.read_sql(consulta1, engine)
print("=="*30)
print('### 1. Barrios con mayor ocurrencia de delitos (promedio mensual de delitos).')
print('A continuación se presenta el top 3 de Barrio con mayor promedio mensual de delitos')
print(' '*30)
print(respuesta1.head(3))
print("=="*30)
print(" "*30)
#Pregunta 2: 
#2. Durante la pandemia el numero de delitos semanales disminuyo? En que magnitud? Analisis en el Top 5 de barrios inseguros de la pregunta 1.

consulta2 =  "select barrio, anio, round(avg(numeroDelitoSemana), 0) as promedioSemanal from(select barrio, anio, date_part('week', fecha) as semana, count(*) as numeroDelitoSemana from delitos d where barrio in ('Palermo', 'Balvanera', 'Flores', 'Recoleta', 'Caballito') group by barrio, semana, anio) as resumensemana group by barrio, anio order by barrio, anio;"

respuesta2 = pd.read_sql(consulta2, engine)

print("=="*30)
print('### 2. Promedio Semanal de Delitos para los años 2016 a 2021 en los 5 Barrios con Mayor Ocurrencia de Delitos.')
print('Barrios: Palermo - Balvanera - Flores - Caballito y Recoleta')
print('EN TODOS LOS BARRIOS ANALIZADOS SE PUEDE OBSERVAR UNA DISMINUCION DE DELITOS EN EL AÑO 2020.')
print(' '*30)

for i in respuesta2['barrio'].unique():
    print('=='*10 , f'Barrio {i}' ,'=='*10 )
    df_filter = respuesta2.loc[respuesta2['barrio']== i ,]
    df_filter['%_variacion'] = round(df_filter['promediosemanal'].pct_change()*100,1)
    print(df_filter)
    print(' ')
print("=="*30)
print(" "*30)

#Pregunta 3:
#3. Todos los dias de la semana tienen el mayor riesgo en cuando a la incidencia de delitos?

consulta3 = "select dia_semana, round(avg(numeroDelitosDiaSemana),1) as promedioDiario, min(numeroDelitosDiaSemana), max(numeroDelitosDiaSemana)from(select  anio, date_part('week', fecha) as semana, dia_semana, count(*) as numeroDelitosDiaSemana from delitos d group by  semana, dia_semana, anio order by  anio, semana )as resumen group by dia_semana order by 2 desc;"

print("=="*30)
print('### 3. Promedio diario de Delitos según dia de la semana. Para toda CABA en el periodo 2016 a 2021.')

print(' '*30)

respuesta3 = pd.read_sql(consulta3, engine)
print(respuesta3)

#Pregunta 4:
#4. Cuales son las horas del dia con mayor numero de delitos?

consulta4= "select horario, round(avg(numerodelitosdia),1) as promediodiario from(select  anio, mes, date_part('day', fecha) as dia,horario, count(*) as numeroDelitosDia from delitos d group by mes, dia, anio, horario order by  anio, mes, dia)as resumen group by horario order by 2 desc;"

print("=="*30)
print('### 4. Promedio diario de Delitos según dia de la Hora del Dia. Para toda CABA en el periodo 2016 a 2021.')

print(' '*30)

respuesta4 = pd.read_sql(consulta4, engine)
respuesta4['%_variacion'] = round(respuesta4['promediodiario'].pct_change()*100,1)
print(respuesta4)

