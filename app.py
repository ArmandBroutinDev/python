import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title("TP Streamlit")
ds = None

#occupation = st.selectbox("Dataset a utiliser",[None,'user_device.csv','listings_final.csv'])
#if occupation:
#    ds = pd.read_csv("~/python/"+occupation,index_col=0)

uploaded_file = st.file_uploader("selectionner votre csv",type=["csv"])
inpt = st.text_input("séparateur utilisé (à changer si une erreur apparait)",',')
if uploaded_file is not None:
    @st.cache
    def get_data(sep):
        return pd.read_csv(uploaded_file,sep=inpt)
    ds = get_data(inpt)
    

if ds is not None:
    st.header("Afficher un nombre de lignes")
    user_input = st.text_input("Combien de ligne voulez-vous lire depuis le début",0)
    user_input = int(user_input)
    if user_input > 0 :
        st.table(ds.head(user_input))

    st.header("Afficher le nom des colonnes du dataset")
    selec = []
    for col in ds.columns:
        st.text(col)
        selec.append(col)

    st.header("Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées")
    st.table(ds.dtypes)

    location = st.multiselect("Selectionner les colonnes",(selec))
    if len(location) > 0 :
        st.table(ds[location].head())

    st.header("La shape du dataset, par lignes et par colonnes")
    st.text("nombre de colonnes {}".format(ds.shape[0]))
    st.text("nombre de lignes {}".format(ds.shape[1]))

    st.header("Afficher les statistiques descriptives du dataset")
    st.text(ds.describe())

    st.header("Afficher plusieurs type de graphique dans une partie visualisation avec notamment :")
    st.subheader("Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write(sns.heatmap(ds.corr(),annot = True))
    st.pyplot()

    st.subheader("Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)")
    col = ds[selec]
    sns.displot(col)
    st.write(plt.show())
    