import os
from tqdm import tqdm

images_lst = os.listdir("train")

for i in tqdm(images_lst):
    if os.path.exists(f"train-yolo-labels/{i.replace('jpg','txt')}"):
        pass
    else:
        os.remove(f'train/{i}')

print("Opration completed >>>>>>>")