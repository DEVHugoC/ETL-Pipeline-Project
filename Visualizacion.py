
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import GestionSQLite as gs  

def visualize_data():
        
    # ---------------- 1. Conexión a la base de datos y extracción de datos ----------------
    base_datos = 'bd_Ordenes_de_Compra.db'
    tabla = 'Ordenes'
    conexion = gs.create_connection(base_datos)
    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conexion)
    gs.close_connection(conexion)

    # ---------------- Gráfico 1: Total gastado por ACUERDO_MARCO ----------------
    df_acuerdo = df.groupby('ACUERDO_MARCO')['TOTAL'].sum().reset_index()
    plt.figure(figsize=(12,8))
    ax1 = sns.barplot(data=df_acuerdo, x='ACUERDO_MARCO', y='TOTAL', palette='viridis')
    plt.title('Total Gastado por Acuerdo Marco', fontsize=16)
    plt.xlabel('Acuerdo Marco', fontsize=14)
    plt.ylabel('Total Gastado (en millones)', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)

    max_val = df_acuerdo['TOTAL'].max()
    ax1.set_ylim(0, max(30, max_val * 1.1))

    ticks1 = ax1.get_yticks()
    ax1.set_yticklabels([str(int(t)) for t in ticks1])

    for p in ax1.patches:
        height = p.get_height()
        ax1.annotate(f'{height:,.0f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', fontsize=10, color='black',
                    xytext=(0, 5), textcoords='offset points')
    plt.tight_layout()
    plt.show()

    # ---------------- Gráfico 2: Total gastado por MES ----------------
    df_mes = df.groupby('MES')['TOTAL'].sum().reset_index()

    meses = {1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
            7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    df_mes['Nombre_Mes'] = df_mes['MES'].map(meses)

    plt.figure(figsize=(10,6))
    ax2 = sns.barplot(data=df_mes, x='Nombre_Mes', y='TOTAL', palette='coolwarm')
    plt.title('Total Gastado por Mes', fontsize=16)
    plt.xlabel('Mes', fontsize=14)
    plt.ylabel('Total Gastado (en millones)', fontsize=14)
    plt.xticks(rotation=0, fontsize=12)
    plt.yticks(fontsize=12)

    for p in ax2.patches:
        height = p.get_height()
        ax2.annotate(f'{height:,.0f}',
                    (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', fontsize=10, color='black',
                    xytext=(0, 5), textcoords='offset points')
    plt.tight_layout()
    plt.show()

    # ---------------- Gráfico 3: Distribución de Órdenes por TIPO_PROCEDIMIENTO ----------------
    df_tipo = df['TIPO_PROCEDIMIENTO'].value_counts()
    plt.figure(figsize=(8,8))
    df_tipo.plot.pie(autopct='%1.1f%%', startangle=90, cmap='Pastel1', legend=True)
    plt.title('Distribución de Órdenes por Tipo de Procedimiento', fontsize=16)
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

    if __name__ == "__main__":
        visualize_data()