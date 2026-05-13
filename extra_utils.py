import yaml
import numpy as np

def get_files(path,file_names):

	data = {}
	for file_name in file_names:
		load_in = np.load(path /  f"{file_name}.npy")
		data[file_name] = load_in
	return data

def import_exp(exp_name):
	#Obtain Results Location and names
	config_loc = f"configs/{exp_name}.yml"

	with open(config_loc) as f:
		exp_params = yaml.safe_load(f)
	
	return exp_params
