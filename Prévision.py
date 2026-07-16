from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="PFE | ESTs | MQSL",
    page_icon="📊",
    layout="wide"
)
# Set page configuration







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





# Logo ESTS
col1, col2, col3 = st.columns([1,4,1])

with col1:
    img = Image.open("images/est.png")
    img = img.resize((130, 60))

    st.image(img)

with col2:
    st.markdown("""
<h3 style='text-align:center;color:#0D47A1;font-size:20px;'>
🎓 Projet de Fin d'Études 🎓
</h3>

<h6 style='text-align:center;color:#6E6E6E;'>
École Supérieure de Technologie de Safi (EST Safi)
</h6>


""", unsafe_allow_html=True)

with col3:
    img = Image.open("images/EST-Safi.jpg")
    img = img.resize((130, 60))

    st.image(img)
    





# Title and Introductory Message

st.markdown("""
<h1 style='color:#B36742; text-align:center;'>
Application de Prévision de la Demande des Produits
</h1>
""", unsafe_allow_html=True)




st.markdown("""

<h6 style='text-align:center;color:#5CA1D6;ont-size:15px;'>

<span style='text-align:center;color:#5CA1D6;ont-size:15px;'>
    Licence Professionnelle : MQSL
</span>
|
<span style='text-align:center;color:#A5D6A7;font-size:15px;'>
Année Universitaire 2025–2026
</span>
|
<span style='text-align:center;color:#6B7280;font-size:15px;'>
EL HAKIK Amina
</span>
</h6>


<h6 style='text-align:center;color:#A5D6A7;font-size:15px;'>

</h6>
""", unsafe_allow_html=True)

st.markdown("""
<span style="color:#6B7280;">
Bienvenue dans **l'Application de Prévision de la Demande des Produits** ! 🌟

Cette application utilise des techniques avancées d'analyse de données afin d'aider les entreprises à comprendre et à prévoir la demande des produits à partir des données historiques de ventes.

<h3 style="color:#85482D;">Fonctionnalités principales</h3>

- **User-Friendly Interface** : Navigate easily through the application.
- **Interactive Data Visualizations** : Engage with dynamic graphs.
- **Accurate Demand Forecasting** : Leverage machine learning algorithms.

<h3 style="color:#85482D;">Comment ça fonctionne</h3>

1. **Data Input** : Upload your sales data.
2. **Forecasting** : Select the product and month.
3. **Visualization** : Explore graphs and charts.

<h3 style="color:#85482D;">À propos de ce projet</h3>

Our goal is to provide businesses with a robust tool for predictive analytics.

Thank you for using our application! </span>
""", unsafe_allow_html=True)

# Create two columns for images
col1, col2 = st.columns(2)

# Add images to the columns
with col1:
    st.image("https://media.licdn.com/dms/image/v2/C4D12AQFB-LCvXBaoNA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1619619546670?e=2147483647&v=beta&t=8eHOWwIN7DPk9ucHRU5V1xnYHDdv-1Lk4v8c2Aax0N0", width=500)

with col2:
    st.image("https://tridentinfo.com/wp-content/uploads/2023/04/demand-forecasting-machine-learning-use-cases.webp", width=500)

st.image("https://miro.medium.com/v2/resize:fit:1400/1*yFjlQejWS5s_IwWGmRGjYQ.png", width=1026)  # Replace with the actual path to your logo or image
