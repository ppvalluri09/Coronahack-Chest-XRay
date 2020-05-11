import pandas as pd
import numpy as np
import shutil
import os

desc = pd.read_csv('./Chest_xray_Corona_Metadata.csv')
train_df = desc[desc['Dataset_type'] == "TRAIN"]
test_df = desc[desc['Dataset_type'] == "TEST"]

train_pos = train_df[train_df['Label'] == "Pnemonia"]
train_neg = train_df[train_df['Label'] == "Normal"]

test_pos = test_df[test_df['Label'] == "Pnemonia"]
test_neg = test_df[test_df['Label'] == "Normal"]

print(len(test_neg), len(test_pos), len(train_pos), len(train_neg))

train = {'0': './Coronahack-Chest-XRay-Dataset/train/0', 
		 '1': './Coronahack-Chest-XRay-Dataset/train/1'}

test = {'0': './Coronahack-Chest-XRay-Dataset/test/0',
		'1': './Coronahack-Chest-XRay-Dataset/test/1'}

source_train = './Coronahack-Chest-XRay-Dataset/train/'
source_test = './Coronahack-Chest-XRay-Dataset/test/'

def move(files, dest, source):
	for file in files:
		source_path = source+file
		_ = shutil.move(source_path, dest)

to_move = True
if to_move:
	move(train_pos['X_ray_image_name'].values.tolist(),
		 train['1'], source_train)
	move(train_neg['X_ray_image_name'].values.tolist(),
		 train['0'], source_train)
	move(test_pos['X_ray_image_name'].values.tolist(),
		 test['1'], source_test)
	move(test_neg['X_ray_image_name'].values.tolist(),
		 test['0'], source_test)
reorder = False

if reorder:
	PATH = './Coronahack-Chest-XRay-Dataset/pred/'
	for file in os.listdir(PATH):
		if file[:6] == "NORMAL":
			move([file], train['0'], PATH)
		elif file[:6] == "person":
			move([file], train['1'], PATH)