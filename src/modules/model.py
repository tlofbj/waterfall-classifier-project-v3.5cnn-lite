import torch
from utils.helper import *
from modules.waterfall import Waterfall
from modules.cnn import CNN

class Model:
    
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.cnn = CNN().to(self.device)
        self.cnn.load_state_dict(torch.load(model_path, map_location=self.device))
        self.cnn.eval()

    def predict(self, img_path, print_results=True):
        # Convert image to tensor
        input_tensor = Waterfall(img_path).tensor.to(self.device)

        # Make prediction
        with torch.no_grad():
            output = self.cnn(input_tensor)
            probability = output.item()
            label = float(probability > 0.5)
            prediction = "signal" if label == 1 else "no_signal"

            results = {
                "label": label,
                "probability": probability,
                "prediction": prediction
            }

            if print_results:
                gprint(f"Label: {label}")
                gprint(f"Probability: {(100*probability):.2f}%")
                gprint(f"Prediction: '{prediction}'")

            return results

