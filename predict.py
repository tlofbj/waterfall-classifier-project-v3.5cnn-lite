import argparse
from modules.model import Model
from utils.helper import *
from utils.scraper import download

default_model_path = 'models/model_2025-05-08T17-34-36.pth'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predicts the presence of signal in a SatNOGS waterfall image")
    parser.add_argument("img_path", nargs="?", type=str, default=None, help="Path to a standard downloaded SatNOGS waterfall PNG image")
    parser.add_argument("--observation_id", "-o", type=int, default=False, help="SatNOGS observation ID (Do not use with --img_path)")
    parser.add_argument("--model_path", "-m", type=str, default=default_model_path, help="Path to the trained model file")
    parser.add_argument("--no_print", "-n", action="store_true", help="Suppresses the printing of prediction results")
    args = parser.parse_args()

    img_path = args.img_path
    if img_path is None:
        if args.observation_id:
            if download(args.observation_id):
                img_path = f"images/waterfall_{args.observation_id}.png"
            else:
                rprint(f"Observation ID ({args.observation_id}) not found.")
                exit
        else:
            rprint("Please provide either an image path or an observation ID.")
            exit

    model = Model(args.model_path)
    prediction = model.predict(img_path, print_results=(not args.no_print))

