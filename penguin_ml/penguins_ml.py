import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

penguin_df = pd.read_csv('penguins.csv')
print(penguin_df.head())
penguin_df.dropna(inplace=True)
output = penguin_df['species'] #target

features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm',
                        'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
print(f'{output.head() = }')
print(f'{features.head()}')
print(features.columns)

output, uniques = pd.factorize(output)
print(uniques)

X_train, X_test, y_train, y_test = train_test_split(
                                            features, output, test_size=.8)

rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train.values, y_train)
y_pred = rfc.predict(X_test.values)

score = accuracy_score(y_pred, y_test)
print(f'Accuracy score del modelo: {score:.2%}')

# Guardamos el modelo
with open('rf_penguin.pickle', 'wb') as f:
    pickle.dump(rfc, f)

with open('output_penguin.pickle', 'wb') as f:
    pickle.dump(uniques, f)

fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
plt.title('Which features are the most important for species predictions ?')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
fig.savefig('feature_importance.png')
    

