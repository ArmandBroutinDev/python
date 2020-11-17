import streamlit as st
import pandas as pd
import numpy as np



st.title("TP Streamlit")

ud = pd.read_csv("~/python/user_device.csv",index_col=0,sep=',')
lf = pd.read_csv("~/python/listings_final.csv",index_col=0,sep=';')
ds = ud

occupation = st.selectbox("Dataset a utiliser",['user_device','listings_final'])
if occupation == 'user_device':
    ds = ud
elif occupation == 'listings_final':
    ds = lf

st.header("Afficher un nombre de lignes")
user_input = st.text_input("Combien de ligne voulez-vous lire",0)
user_input = int(user_input)
st.table(ds.head(user_input))

st.header("Afficher le nom des colonnes du dataset")
for col in ds.columns: 
    st.text(col)

st.header("Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées")
st.table(ds.dtypes)

selec = []
for col in ds.columns:
    selec.append(col)
location = st.multiselect("Selectionner les colonnes",(selec))
st.table(ds[location].head())