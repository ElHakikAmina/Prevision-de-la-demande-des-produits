from PIL import Image
import streamlit as st


# Set page configuration
st.set_page_config(page_title="Product Demand Forecasting", layout="wide")

# Logo ESTS
col1, col2, col3 = st.columns([1,4,1])

with col1:
    img = Image.open("images/est.png")
    img = img.resize((130, 60))

    st.image(img)

with col2:
    st.markdown(""" <h1 style='text-align: center; font-size: 42px;
           color: #0E4C92;
           margin-bottom: 10px;'>
    🎓 Projet de Fin d'Études
    </h1>

    <h3 style='text-align: center;
           color: gray;'>
    École Supérieure de Technologie de Safi (EST Safi)
    </h3>

    <h5 style='text-align: center;
           color: #2E8B57;'>
    Année Universitaire 2025–2026
    </h5>
    """, unsafe_allow_html=True)

with col3:
    img = Image.open("images/EST-Safi.jpg")
    img = img.resize((130, 60))

    st.image(img)
    





# Title and Introductory Message

st.title("Application de Prévision de la Demande des Produits")
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
