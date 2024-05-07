from torch import nn, device, cuda, flatten, load
from torch import sigmoid, softmax, argmax
from torchvision import models

# CNN model Architecture, to be able to load the model
class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        
        input_img_group = 10
        self.input = nn.Conv2d(input_img_group, 3, kernel_size = 3)
        model = models.efficientnet_b0(weights = 'IMAGENET1K_V1')
        
        self.features = model.features
        self.avgpool = model.avgpool
        
        #heads
        self.bowel = nn.Linear(1280, 1) #1,0

        self.extravasation = nn.Linear(1280, 1) #1.0

        self.kidney = nn.Linear(1280, 3)

        self.liver = nn.Linear(1280,3) 

        self.spleen = nn.Linear(1280, 3)
    
    def forward(self, x):
        
        # extract features
        x = self.input(x)
        x = self.features(x)
        x = self.avgpool(x)
        x = flatten(x, 1)

        # output logits
        bowel = self.bowel(x)
        extravsation = self.extravasation(x)
        kidney = self.kidney(x)
        liver = self.liver(x)
        spleen = self.spleen(x)
        
        return bowel, extravsation, kidney, liver, spleen
    
model = CNNModel()
model.eval()
# decide wether to use GPU or CPU based on availability
machine_device = device('cuda' if cuda.is_available() else 'cpu')

model.load_state_dict(load('./efficientnet_b0_1.658.pth', map_location = machine_device))

def binary_metric(output):
    prob = sigmoid(output)
    return prob > 0.5

def class_metric(output):
    prob = softmax(output, dim = 1)
    return argmax(prob, dim=1)

def get_predictions(processed_images):
    bowel, extravsation, kidney, liver, spleen = model(processed_images)

    bowel = binary_metric(bowel).item()
    extravsation = binary_metric(extravsation).item()
    kidney = class_metric(kidney).item()
    liver = class_metric(liver).item()
    spleen = class_metric(spleen).item()

    return bowel, extravsation, kidney, liver, spleen
