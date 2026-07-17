from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="PFE | ESTs  | MQSL",
    page_icon="📊",
    layout="wide"
)
# Set page configuration




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

Cette application a été développée dans le cadre de mon **Projet de Fin d'Études (PFE)** pour l'obtention de la **Licence Professionnelle en Management de la Qualité, Sécurité et Logistique (MQSL)** à l'**École Supérieure de Technologie de Safi (EST Safi)**.

""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    #img = Image.open("images/dmnd-forcast.JPG")
    #img = img.resize((200, 200))

    #st.image(img)
    st.image(
    "images/dmnd-forcast.JPG",
    use_container_width=True
    )

with col2:
    st.markdown("""  
            Le projet consiste à concevoir une application intelligente capable d'analyser les données historiques de ventes et de générer des prévisions fiables de la demande des produits grâce à l'utilisation de techniques d'**Intelligence Artificielle** et d'**analyse prédictive**.

            L'application permet aux utilisateurs de consulter les données historiques, visualiser les tendances, générer des prévisions futures et faciliter la prise de décision afin d'optimiser la gestion des stocks et d'améliorer la planification des approvisionnements.
""", unsafe_allow_html=True)







st.markdown("""


<h3 style="color:#85482D;">Fonctionnalités principales</h3>

- **Interface conviviale** : Naviguez facilement dans l'application grâce à une interface simple et intuitive.
- **Visualisations interactives des données** : Explorez les données à travers des graphiques et des visualisations dynamiques.
- **Prévision précise de la demande** : Exploitez des algorithmes de machine learning pour générer des prévisions fiables de la demande des produits.

<h3 style="color:#85482D;">Comment ça fonctionne</h3>

1. **Importation des données** : Chargez vos données de ventes afin de lancer l'analyse et les prévisions.
2. **Prévision de la demande** : Sélectionnez le produit et le mois pour lesquels vous souhaitez générer une prévision.
3. **Visualisation des résultats** : Consultez des graphiques et des tableaux interactifs pour analyser les données historiques et les prévisions.

<h3 style="color:#85482D;">À propos de ce projet</h3>

Mon objectif est de développer un outil performant d'analyse prédictive.
             </span>
""", unsafe_allow_html=True)

