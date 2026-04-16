import onnxruntime as ort
import numpy as np

# Load model once
session = ort.InferenceSession("model/health_model.onnx")
input_name = session.get_inputs()[0].name


def get_category(score):
    if score >= 90:
        return "Healthy"
    elif score >= 65:
        return "Good"
    elif score >= 40:
        return "Degrading"
    else:
        return "Critical"


def predict_health(features):
    inputs = np.array([features], dtype=np.float32)
    output = session.run(None, {input_name: inputs})

    score = int(round(float(output[0][0])))
    score = max(0, min(100, score))

    category = get_category(score)

    return score, category
