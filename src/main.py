from modules.model import Model

model_path = 'models/model_2025-05-08T17-34-36.pth'
img_path = 'images/waterfall_10370.png'

model = Model(model_path)
prediction = model.predict(img_path, print_results=True)

