import sys
import numpy as np
import pandas as pd
import pickle
import json

# print("Python version:", sys.version)
# print("Python executable path:", sys.executable)
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
diseases_list = {
    0: '(vertigo) Paroymsal  Positional Vertigo',
    1: 'AIDS',
    2: 'Acne',
    3: 'Alcoholic hepatitis',
    4: 'Allergy',
    5: 'Arthritis',
    6: 'Bronchial Asthma',
    7: 'Cervical spondylosis',
    8: 'Chicken pox',
    9: 'Chronic cholestasis',
    10: 'Common Cold',
    11: 'Dengue',
    12: 'Diabetes ',
    13: 'Dimorphic hemmorhoids(piles)',
    14: 'Drug Reaction',
    15: 'Fungal infection',
    16: 'GERD',
    17: 'Gastroenteritis',
    18: 'Heart attack',
    19: 'Hepatitis B',
    20: 'Hepatitis C',
    21: 'Hepatitis D',
    22: 'Hepatitis E',
    23: 'Hypertension ',
    24: 'Hyperthyroidism',
    25: 'Hypoglycemia',
    26: 'Hypothyroidism',
    27: 'Impetigo',
    28: 'Jaundice',
    29: 'Malaria',
    30: 'Migraine',
    31: 'Osteoarthristis',
    32: 'Paralysis (brain hemorrhage)',
    33: 'Peptic ulcer diseae',
    34: 'Pneumonia',
    35: 'Psoriasis',
    36: 'Tuberculosis',
    37: 'Typhoid',
    38: 'Urinary tract infection',
    39: 'Varicose veins',
    40: 'hepatitis A'
}

# load databasedataset===================================
# Load datasets
sym_des = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\symtoms_df.csv")
precautions = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\precautions_df.csv")
workout = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\workout_df.csv")
description = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\description.csv")
medications = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\medications.csv")
diets = pd.read_csv(r"D:\AI-MedLab\backend\HealthPredict\diets.csv")

with open(r"D:\AI-MedLab\backend\aimodels\svc.pkl", 'rb') as model_fileL:
    model = pickle.load(model_fileL)

def get_predicted_value(symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    valid_symptoms = []

    for symptom in symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
            valid_symptoms.append(symptom)
        else:
            print(f"Warning: symptom '{symptom}' not found in symptoms_dict", file=sys.stderr)

    if not valid_symptoms:
        raise ValueError("No valid symptoms provided. Please check your input.")

    input_vector_df = pd.DataFrame([input_vector], columns=symptoms_dict.keys())
    return diseases_list[model.predict(input_vector_df)[0]]

def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join(desc.tolist())

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = pre.values.tolist()[0]  # Extract the first row as a list

    med = medications[medications['Disease'] == dis]['Medication']
    med = med.tolist()  # Ensure it's a list

    die = diets[diets['Disease'] == dis]['Diet']
    die = die.tolist()  # Ensure it's a list

    wrkout = workout[workout['disease'] == dis]['workout']
    wrkout = wrkout.tolist()  # Ensure it's a list

    return desc, pre, med, die, wrkout

# Parse input data
data = sys.argv[3]
data_dict = json.loads(data)
symptoms = data_dict['data']

# Ensure symptoms is a list
if isinstance(symptoms, str):
    symptoms = [symptoms]
elif not isinstance(symptoms, list):
    raise ValueError("Invalid input: 'data' must be a list of symptoms or a single symptom string.")

predicted_disease = get_predicted_value(symptoms)

# Get additional details
dis_des, precautions, medications, rec_diet, workout = helper(predicted_disease)

# Create the data dictionary
data = {
    "predicted_disease": str(predicted_disease),
    "dis_des": dis_des,
    "my_precautions": precautions,
    "medications": medications,
    "rec_diet": rec_diet,
    "workout": workout
}

# Convert the data dictionary to JSON and print it
json_string = json.dumps(data, indent=2)
print(json_string)


