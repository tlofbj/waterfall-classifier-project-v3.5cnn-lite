from PIL import Image
from torchvision import transforms

class Waterfall():

    def __init__(self, img_path):
        self.path = img_path
        self.image = self.modify()
        self.tensor = self.tensorize()

    def modify(self):
        image = Image.open(self.path)
        image = image.convert('L')
        image = image.crop((67, 11, 686, 1550))
        transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5], std=[0.5])
        ])
        return transform(image)

    def tensorize(self):
        return self.image.unsqueeze(0)