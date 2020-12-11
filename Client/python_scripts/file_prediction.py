import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import utils
import network
import sys

input_file = './python_scripts/audio/1.wav'

min_score = 0.7
min_diff = 0.2


def print_prediction(file_name):
    model = load_model('./python_scripts/model/model.hdf5')
    labels_file = './python_scripts/features/labels.npy'
    labels = np.load(labels_file)
    le = LabelEncoder()
    le.fit_transform(labels)
    prediction_feature = np.array([utils.extract_features(file_name)])
    print(f'features:\n{prediction_feature}\n')
    

    predicted_vector = model.predict_classes(prediction_feature)
    predicted_class = le.inverse_transform(predicted_vector)
    print(f'The predicted class for file {file_name} is: {predicted_class[0]}')
    sys.stdout.flush()
       
    

    predicted_proba_vector = model.predict_proba(prediction_feature)
    predicted_proba = predicted_proba_vector[0]

    score_str = format(max(predicted_proba), '.3f')
    score = float(score_str)

    for i in range(len(predicted_proba)):
        category = le.inverse_transform(np.array([i]))
        print(category[0], "\t\t : ", format(predicted_proba[i], '.32f'))
        

    valid = np.diff(sorted(predicted_proba.tolist()))[-1] > min_diff and score > min_score
    if not valid:
        print('*** unsure prediction')
        return

    network.export(prediction_feature, predicted_class[0], score_str)


if __name__ == '__main__':
    print_prediction(input_file)
