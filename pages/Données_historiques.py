import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your data
data = pd.read_excel("pages/Base_de_Donnees_Ventes.xlsx")

# Convert 'Month' to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Dictionary des mois en français
months = {
    "Janvier": 1,
    "Février": 2,
    "Mars": 3,
    "Avril": 4,
    "Mai": 5,
    "Juin": 6,
    "Juillet": 7,
    "Août": 8,
    "Septembre": 9,
    "Octobre": 10,
    "Novembre": 11,
    "Décembre": 12
}

# Sélection du mois et du produit
selected_month = st.selectbox(
    "Choisissez un mois",
    list(months.keys())
)

selected_product = st.selectbox(
    "Choisissez un produit",
    data['Product Name'].unique()
)

# Filtrer les données selon le numéro du mois
month_data = data[data['Month'].dt.month == months[selected_month]]

if not month_data.empty:

    fig = go.Figure()

    for product in month_data['Product Name']:
        color = 'blue' if product == selected_product else 'lightgray'
        opacity = 1 if product == selected_product else 0.5

        fig.add_trace(
            go.Bar(
                x=[product],
                y=month_data[month_data['Product Name'] == product]['Monthly_Sales'],
                name=product,
                marker_color=color,
                opacity=opacity,
                width=0.4
            )
        )

    fig.update_layout(
        title=f"Comparaison des ventes mensuelles - {selected_month}",
        xaxis_title="Produit",
        yaxis_title="Ventes",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.write(f"Aucune donnée disponible pour le mois de {selected_month}.")

# -----------------------------
# Graphique des ventes annuelles
# -----------------------------
st.subheader(f"Tendance des ventes de {selected_product} sur la dernière année")

last_year = data['Month'].dt.year.max()

product_last_year_data = data[
    (data['Month'].dt.year == last_year) &
    (data['Product Name'] == selected_product)
]

fig_trend = px.line(
    product_last_year_data,
    x='Month',
    y='Monthly_Sales',
    title=f"Tendance des ventes de {selected_product}",
    labels={
        'Monthly_Sales': 'Ventes',
        'Month': 'Mois'
    },
    markers=True
)

st.plotly_chart(fig_trend, use_container_width=True)