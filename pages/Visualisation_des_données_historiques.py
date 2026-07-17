import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go


st.set_page_config(
    page_title="PFE | ESTs | MQSL",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>

/* Hide Streamlit header */
header[data-testid="stHeader"] {
    display: none;
}

/* Remove top spacing */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)




st.markdown("""
<style>

/* ===== Sidebar ===== */
[data-testid="stSidebar"]{
    background-color: #FCFCFC;
    border-right: 2px solid #F8E8DF;
}

/* ===== Navigation links ===== */
[data-testid="stSidebarNav"] a,
[data-testid="stSidebarNav"] a span{
    color:#B36742 !important;
    font-weight:600 !important;
    border-radius:12px;
    transition:all .3s ease;
}

/* ===== Hover ===== */
[data-testid="stSidebarNav"] a:hover,
[data-testid="stSidebarNav"] a:hover span{
    color:white !important;
}

/* Hover background */
[data-testid="stSidebarNav"] li:hover{
    background:linear-gradient(90deg,#D8AF99,#B36742);
    border-radius:12px;
}

/* ===== Selected page ===== */
[data-testid="stSidebarNav"] li[data-selected="true"]{
    background:linear-gradient(90deg,#1565C0,#4A90E2);
    border-radius:12px;
    box-shadow:0 4px 12px rgba(21,101,192,.25);
}

[data-testid="stSidebarNav"] li[data-selected="true"] a,
[data-testid="stSidebarNav"] li[data-selected="true"] span{
    color:white !important;
    font-weight:700 !important;
}

</style>
""", unsafe_allow_html=True)



# Load your data (ensure the file path is correct)
data = pd.read_excel('pages/Base_de_Donnees_Ventes.xlsx')

# Convert 'Month' to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Create a list of months sorted correctly
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']













st.markdown("""
<style>

/* Texte des labels */
label {
    color: #85482D !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

/* Zone du selectbox */
div[data-baseweb="select"] > div {
    background-color: #F8F9FA !important;
    border: 2px solid #236FAF !important;
    border-radius: 8px !important;
}

/* Texte sélectionné */
div[data-baseweb="select"] span {
    color: #236FAF !important;
    font-weight: 600;
}

/* Menu déroulant */
div[role="listbox"] {
    background-color: white !important;
}

/* Options */
div[role="option"] {
    color: #374151 !important;
}

/* Option survolée */
div[role="option"]:hover {
    background-color: #E8F1FB !important;
    color: #236FAF !important;
}

</style>
""", unsafe_allow_html=True)
# Streamlit user inputs for month and product selection
selected_month = st.selectbox("Choisissez un mois", months_list)
selected_product = st.selectbox("Choisissez un Produit", data['Product Name'].unique())

# Filter data for the selected product
monthly_data = data[data['Product Name'] == selected_product]

# Ensure the data is filtered for the selected month if needed
monthly_data['Month_str'] = monthly_data['Month'].dt.strftime('%B')
monthly_data = monthly_data[monthly_data['Month_str'] == selected_month]

# Calculate total stock and total sales for the selected product in the selected month
if not monthly_data.empty:  # Check if there is any data for the selected product in the selected month
    total_month_stock = monthly_data['Monthly_Stock'].sum()  # Total stock for the selected product
    total_sales = monthly_data['Monthly_Sales'].sum()  # Total sales for the selected product

    # Prepare data for prediction
    # Create a DataFrame for Prophet
    df = monthly_data[['Month', 'Monthly_Sales']].rename(columns={'Month': 'ds', 'Monthly_Sales': 'y'})
    
    # Fit the model
    model = Prophet()
    model.fit(df)

    # Create a future DataFrame for the next month
    future = model.make_future_dataframe(periods=1, freq='ME')
    forecast = model.predict(future)
    
    # Get the predicted value for the next month
    predicted_value = forecast['yhat'].iloc[-1]  # Last prediction value
    
    # Prepare data for different plots
    labels = ['Total Sales', 'Total Monthly Stock', 'Predicted Sales']
    values = [total_sales, total_month_stock, predicted_value]

    # Plotting sales vs stock
    st.subheader(f"Ventes vs. Stock pour {selected_product} en {selected_month}")

    # Bar Plot for Sales and Stock
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=['Ventes', 'Stock'], y=[total_sales, total_month_stock], 
                              marker_color=['blue', 'orange']))
    fig_bar.update_layout(title='Ventes vs Stock', xaxis_title='Category', yaxis_title='Amount')
    st.plotly_chart(fig_bar)

    # Line Plot to visualize trends
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=['Ventes', 'Stock'], y=[total_sales, total_month_stock], 
                                   mode='lines+markers', name='Sales & Stock', line=dict(shape='linear')))
    fig_line.update_layout(title='Ventes vs Stock Trend', xaxis_title='Category', yaxis_title='Amount')
    st.plotly_chart(fig_line)

    # Area Plot to visualize cumulative sales and stock
    fig_area = go.Figure()
    fig_area.add_trace(go.Scatter(x=['ventes', 'Stock'], y=[total_sales, total_month_stock], 
                                   mode='lines', fill='tozeroy', name='Values'))
    fig_area.update_layout(title='Cumul des ventes vs Stock', xaxis_title='Category', yaxis_title='Amount')
    st.plotly_chart(fig_area)

    # Pie Chart to represent sales and stock distribution
    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(labels=['Ventes totales', 'Stock total'], values=[total_sales, total_month_stock], 
                              name='Sales and Stock'))
    fig_pie.update_layout(title='Répartition des ventes et des stocks')
    st.plotly_chart(fig_pie)

else:
    st.error(f"No data available for {selected_product} in {selected_month}.")


