import torch
from pathlib import Path
import numpy as np
import glob

# Set paths to access training data and test data
data_dir = Path.cwd() / "archive"
train_dir = data_dir / "train"
test_dir = data_dir / "test"

# 
image_sets = ["hot_dog","not_hot_dog"]

for sets in image_sets:
    image_paths = glob.glob(str(train_dir / "hot_dog\*"))
    #images = np.load(image_paths[0])
    
    print(image_paths[0])
