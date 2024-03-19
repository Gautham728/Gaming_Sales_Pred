import streamlit as st

st.title('Visualisation ')

st.markdown('Analyse the DataFrame ')

# Personnalisation CSS pour agrandir l'iframe
css = """
    <style>
    iframe {
        width: 200%;
        height: 700px;
    }
    </style>
    """

# Affichage du CSS personnalisé
st.markdown(css, unsafe_allow_html=True)

# Affichage de l'iframe contenant le rapport Power BI
st.components.v1.iframe("https://public.tableau.com/app/profile/gautham.acharya/viz/Gamingsalesdashboard/Dashboard1")

