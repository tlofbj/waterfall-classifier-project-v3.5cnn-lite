import torch.nn as nn

class CNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.sequential = nn.Sequential(
            # Convolutional Layer 1: (1*128*128->32*64*64)
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=4, stride=4),

            # Convolutional Layer 2: (32*64*64->64*32*32)
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Convolutional Layer 3: (32*32*32->64*16*16)
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Convolutional Layer 4: (64*16*16->64*8*8)
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2), 

            # Flatten feature maps to prepare for fully connected layers
            nn.Flatten(),

            # Fully Connected Layers for Prediction:
            nn.Linear(64*8*8, 256),
            nn.ReLU(),
            nn.Dropout(0.5), # (prevents overfitting)
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.sequential(x)
    
