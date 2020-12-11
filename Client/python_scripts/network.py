import time
import json
import numpy as np


def export(feats, predicted_class, score):
    data = {"predicted_class": predicted_class, "score": score, "features": feats, "timestamp": time.time()}
    save_json(data)


def save_json(data):
    with open("./recognition.json", "w+") as file:
        file.write(json.dumps(data, cls=NumpyEncoder, indent=4))


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
