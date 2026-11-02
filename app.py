import plotly.express as px
import pandas as pd

data = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

#6 
print("Resultat question n°6")
data['ca'] = data['prix'] * data['qte']

print("CA par produit (CApp)")
print("Moyenne ")
CApp_moy = data.groupby('produit')['ca'].mean()
print("Resultat question n°6 a-i")
print("CApp_moy : " , CApp_moy)

print("Mediane")
CApp_med = data.groupby('produit')['ca'].median()
print("Resultat question n°6 a-ii")
print("CApp_med : " , CApp_med)


print("Volume de vente par produit (VVpp)")
print("Moyenne")
VVpp_moy = data.groupby('produit')['qte'].mean()
print("Resultat question n°6 a-i")
print("VVpp_moy : " , VVpp_moy)

print("Mediane")
VVpp_med = data.groupby('produit')['qte'].median()
print("Resultat question n°6 a-ii")
print("VVpp_med : " , VVpp_med)

print("pour le volume des ventes par produit")
# ecart-type > std
# variance > var
print("Resultat question n°6 b-ii")
VVpp_ET_VAR = data.groupby('produit')['qte'].agg(['std', 'var'])
print("VVpp_ET_VAR : " , VVpp_ET_VAR)


# 7
print("Resultat question n°7")
data_python = data.to_dict(orient='records')

vpp = {}
for ligne in data_python:
    produit = ligne['produit']
    qte = ligne['qte']

    vpp[produit] = vpp.get(produit, 0) + qte

vente_max = max(vpp, key=vpp.get)
vente_min = min(vpp, key=vpp.get)

print(f"Plus vendu : {vente_max} ({vpp[vente_max]})")
print(f"Moins vendu : {vente_min} ({vpp[vente_min]})")


# 8.a
print("Resultat question n°8.a")
vpp_df=data.groupby('produit')['qte'].sum().reset_index()
figure_vpp_pie = px.pie(
    vpp_df,
    names='produit',
    values='qte',
    title="Ventes par produit (Quantités)"
)
figure_vpp_pie.write_html('vpp_pie.html')
print('Voir vpp_pie.html')

figure_vpp_bar = px.bar(
    vpp_df,
    x='produit',
    y='qte',
    title="Ventes par produit (Quantités)"
)
figure_vpp_bar.write_html('vpp_bar.html')
print('Voir vpp_bar.html')

# 8.b
print("Resultat question n°8.b")
CAPP_df=data.groupby('produit')['ca'].sum().reset_index()
figure_vpp_pie = px.pie(
    CAPP_df,
    names='produit',
    values='ca',
    title="CA par produit (€)"
)
figure_vpp_pie.write_html('CAPP_pie.html')
print('Voir CAPP_pie.html')



# figure = px.pie(data, values='qte', names='region', title='quantité vendue par région')
# figure.write_html('ventes-par-region.html')
# 
# print('ventes-par-région.html généré avec succès !')
