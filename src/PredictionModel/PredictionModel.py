from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd
import joblib


#NOTICE: Feel free to modify the following to better suit your use cases
data = {
    'description': [
        '7-ELEVEN',
        'MTR ticket',
        'Octopus card recharge',
        'Restaurant',
        'HKU tuition fee',
        'Supermarket in Causeway Bay',
        'Insurance payment for health',
        'Clinic',
        'Hospital',
        'Octopus transit', 
        'Star Ferry fare', 
        'Hong Kong Disneyland tickets', 
        'iPhone purchase', 
        'Shenzhen border crossing fee', 
        'Night club entry fee', 
        'Yoga studio membership', 
        'Properties',
        'Real Estate',
        'Realtor',
        'Fitness',
        'Gym',
        'Tennis',
        'Basketball',
        'Food Panda',
        'Uber Eats',
        'Uber',
        'Doctor',
        'Movie',
        'Cinema',
        'Theatre',
        'Netflix',
        'HULU',
        'Amazon Prime',
        'HBO',
        'Electricity Bill',
        'Water Bill'
    ],
    'category': [
        'Food',
        'Transportation',
        'Transportation',
        'Food',
        'Education',
        'Food',
        'Health',
        'Health',
        'Health',
        'Transportation',
        'Transportation',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Sports',
        'Rent',
        'Rent',
        'Rent',
        'Sports',
        'Sports',
        'Sports',
        'Sports',
        'Food',
        'Food',
        'Transportation'
        'Health',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Entertainment',
        'Utility',
        'Utility'
    ]
}
df = pd.DataFrame(data)

model = make_pipeline(CountVectorizer(), MultinomialNB())

model.fit(df['description'], df['category'])

joblib.dump(model, '../src/PredictionModel/prediction_category_model.joblib')