import streamlit as st
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

st.title('Penguin Classifier')
st.write('Esta aplicación usa 6 inputs para predecir la especie de pingüino usando'
            'un modelo pre-entrenado en el Palmer Penguyins datasete. Usa'
            'el formulario siguiente para empezar.')

st.subheader('Train your model')
penguin_file = st.file_uploader('Upload file with penguin data')

@st.cache_resource()
def get_model_and_mapping() -> tuple[RandomForestClassifier, pd.Index]:
    """Devuelve el modelo pre entrenado y el mapping

    Returns
    -------
    tuple[RandomForestClassifier, pd.Index]
        _description_
    """
    with open('rf_penguin.pickle', 'rb') as f:
        rfc:RandomForestClassifier = pickle.load(f)

    with open('output_penguin.pickle', 'rb') as f:
        unique_penguin_mapping:pd.Index = pickle.load(f)
    
    return rfc, unique_penguin_mapping

if penguin_file is None:
    rfc, unique_penguin_mapping = get_model_and_mapping()

else:
    penguin_df = pd.read_csv(penguin_file)
    penguin_df.dropna(inplace=True)
    output = penguin_df['species'] #target
    features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm',
                            'flipper_length_mm', 'body_mass_g', 'sex']]
    features = pd.get_dummies(features)
    output, unique_penguin_mapping = pd.factorize(output)

    X_train, X_test, y_train, y_test = train_test_split(
        features, output, test_size=.8)

    rfc = RandomForestClassifier(random_state=42)
    rfc.fit(X_train.values, y_train)
    y_pred = rfc.predict(X_test.values)

    score = accuracy_score(y_pred, y_test)
    st.write(f'Hemos entrenado el modelo en tu data. Tiene una puntuación de {score:.2%} !')

island_biscoe, island_dream, island_torgerson = 0, 0, 0
sex_female, sex_male = 0, 0

st.subheader('Predict your penguin')
with st.form('Penguin Island'):
    island = st.selectbox("Penguin Island", options=['Biscoe', 'Dream', 'Torgerson'])
    sex = st.selectbox("Sex", options=['Female', 'Male'])
    bill_length = st.number_input('Bill Lenght (mm)', min_value=0)
    bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
    flipper_length = st.number_input('Flipper Lenght (mm)', min_value=0)
    body_mass = st.number_input('Body mass (g)', min_value=0)
    user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]

    if island == 'Biscoe':
        island_biscoe = 1
    elif island == 'Dream':
        island_dream = 1
    else:
        island_torgerson = 1

    if sex == 'Female':
        sex_female = 1
    else:
        sex_male = 1

    pred_df = pd.DataFrame(data=[[bill_length, bill_depth, flipper_length,
                            body_mass, island_biscoe, island_dream,
                            island_torgerson, sex_female, sex_male]], columns=['bill_length', 'bill_depth', 'flipper_length',
                                                                                'body_mass', 'island_biscoe', 'island_dream',
                                                                                'island_torgerson', 'sex_female', 'sex_male'])

    new_pred = rfc.predict(pred_df.values)
    predecir = st.form_submit_button("Submit")

st.subheader("Predicting your penguin's species")
if predecir:
    prediction_species = unique_penguin_mapping[new_pred][0]
    st.write(f'Predecimos que tu pingüino de mierda pertenece a la especie :red[{prediction_species}]')
st.divider()
st.write("""
        Hemos usado un modelo Random Forest para predecir las especies
            Las varaibles usadas están ranqueadas por importancia.
        """)
st.image('feature_importance.png')
st.write("""Debajo se detallan los histogramas para cada variable continua separada
            por especie de pingüino de mierda. La linea vertical
            representa el valor inputado.""")
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_length_mm'],
                    hue=penguin_df['species'])
plt.axvline(bill_length)
plt.title("Bill Length por especie")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_depth_mm'],
                    hue=penguin_df['species'])
plt.axvline(bill_depth)
plt.title("Bill Depth por especie")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['flipper_length_mm'],
                    hue=penguin_df['species'])
plt.axvline(flipper_length)
plt.title("Flipper Lenght por especie")
st.pyplot(ax)



#st.write(f"""the user inputs are: {user_inputs}""")


#st.write(rfc)
#st.write(unique_penguin_mapping)