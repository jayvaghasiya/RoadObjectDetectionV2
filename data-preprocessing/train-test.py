import os
import shutil
import random
import math
from tqdm import tqdm

def random_test_split(images_dir, labels_dir, test_images_dir, test_labels_dir, split_ratio):
    # Create the test and label directories if they don't exist
    os.makedirs(test_images_dir, exist_ok=True)
    os.makedirs(test_labels_dir, exist_ok=True)

    # Get a list of all image files
    image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

    # Get a list of all corresponding label files (assuming the label files have the same name with a specific extension)
    label_files = [f"{os.path.splitext(f)[0]}.txt" for f in image_files]

    # Calculate the number of images for the test set
    num_images = len(image_files)
    num_test = math.ceil(num_images * split_ratio)

    # Randomly shuffle the list of image and label files together
    combined_files = list(zip(image_files, label_files))
    random.shuffle(combined_files)
    test_files = combined_files[:num_test]

    # Move the test images and their corresponding label files to the test set directories
    for image_file, label_file in tqdm(test_files, desc="Processing", ncols=100, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"):
        shutil.move(os.path.join(images_dir, image_file), os.path.join(test_images_dir, image_file))
        shutil.move(os.path.join(labels_dir, label_file), os.path.join(test_labels_dir, label_file))

# Set the paths and split ratio (e.g., 0.3 for 30% test split)
images_directory = "val"
labels_directory = "valid-yolo-labels"
test_images_directory = "test"
test_labels_directory = "test-labels"
split_ratio = 0.3

random_test_split(images_directory, labels_directory, test_images_directory, test_labels_directory, split_ratio)
