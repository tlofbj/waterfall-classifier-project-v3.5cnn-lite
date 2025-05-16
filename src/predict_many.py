import os
import argparse
from modules.model import Model
from utils.helper import *
from utils.logger import Logger

default_model_path = 'models/model_2025-05-08T17-34-36.pth'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predicts the presence of signal in a SatNOGS waterfall image")
    parser.add_argument("--model_path", "-m", type=str, default=default_model_path, help="Path to the trained model file")
    parser.add_argument("--log_dir", "-l", type=str, default='images', help="Directory of the prediction_log.json file")
    parser.add_argument("--img_dir", "-i", type=str, default='images', help="Directory of the images to predict")
    args = parser.parse_args()

    logger = Logger(args.log_dir, 'prediction_log.json')

    model = Model(args.model_path)

    for filename in os.listdir(args.img_dir):
        if filename.endswith('.png'):
            img_path = os.path.join(args.img_dir, filename)
            prediction = model.predict(img_path, print_results=False)
            logger.append({
                'img_path': img_path,
                'timestamp': get_timestamp(),
                'prediction': prediction
            })
    gprint(f"Predictions saved to {args.log_path}")