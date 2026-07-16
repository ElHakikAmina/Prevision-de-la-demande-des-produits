from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="PFE | ESTs | MQSL",
    page_icon="📊",
    layout="wide"
)
# Set page configuration

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



<h5 style='text-align:center;color:#1565C0;font-weight:600;'>
Licence Professionnelle : MQSL
</h5>


<h6 style='text-align:center;color:#2E8B57;ont-size:15px;'>
Année Universitaire 2025–2026
</h6>
""", unsafe_allow_html=True)


st.markdown("""
    Bienvenue dans **l'Application de Prévision de la Demande des Produits** !🌟

    Cette application utilise des techniques avancées d'analyse de données afin d'aider les entreprises à comprendre et à prévoir la demande des produits à partir des données historiques de ventes. Grâce à des visualisations intuitives et à des modèles prédictifs, les utilisateurs peuvent prendre des décisions éclairées pour optimiser la gestion des stocks et améliorer leurs stratégies commerciales.

    ## Fonctionnalités principales:
    - **User-Friendly Interface**: Navigate easily through the application for a seamless experience.
    - **Interactive Data Visualizations**: Engage with dynamic graphs and charts for insightful data analysis.
    - **Accurate Demand Forecasting**: Leverage machine learning algorithms for precise demand predictions.

    ## Comment ça fonctionne:
    1. **Data Input**: Upload your sales data in the specified format to kickstart the analysis.
    2. **Forecasting**: Select the product and month for which you wish to forecast demand.
    3. **Visualization**: Explore detailed graphs and charts that illustrate your data and forecasts, aiding in strategic decision-making.

    ## À propos de ce projet:
    Our goal is to provide businesses with a robust tool for predictive analytics, enabling alignment of inventory management with actual consumer demand. By harnessing data-driven insights, we aim to empower businesses in navigating market fluctuations effectively.
    
    Thank you for using our application, and we hope it serves you well in your decision-making process!
""")

# Create two columns for images
col1, col2 = st.columns(2)

# Add images to the columns
with col1:
    st.image("https://media.licdn.com/dms/image/v2/C4D12AQFB-LCvXBaoNA/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1619619546670?e=2147483647&v=beta&t=8eHOWwIN7DPk9ucHRU5V1xnYHDdv-1Lk4v8c2Aax0N0", width=500)

with col2:
    st.image("https://tridentinfo.com/wp-content/uploads/2023/04/demand-forecasting-machine-learning-use-cases.webp", width=500)

st.image("https://miro.medium.com/v2/resize:fit:1400/1*yFjlQejWS5s_IwWGmRGjYQ.png", width=1026)  # Replace with the actual path to your logo or image
