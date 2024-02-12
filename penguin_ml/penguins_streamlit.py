import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

st.title('Penguin Classifier')
st.write('Esta aplicación usa 6 inputs para predecir la especie de pingüino usando'
            'un modelo pre-entrenado en el Palmer Penguyins datasete. Usa'
            'el formulario siguiente para empezar.')

with open('rf_penguin.pickle', 'rb') as f:
    rfc:RandomForestClassifier = pickle.load(f)

with open('output_penguin.pickle', 'rb') as f:
    unique_penguin_mapping = pickle.load(f)

island_biscoe, island_dream, island_torgerson = 0, 0, 0
sex_female, sex_male = 0, 0

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
    st.write(f'Predecimos que tu pingüino de mierda pertenece a la especie {prediction_species}')

#st.write(f"""the user inputs are: {user_inputs}""")


#st.write(rfc)
#st.write(unique_penguin_mapping)