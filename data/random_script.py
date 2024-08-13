import pandas as pd
import json
import random

def predict_next_step(x, y):
    new_x = x + random.choice([-1, 0, 1])
    new_y = y + random.choice([-1, 0, 1])
    return new_x, new_y

def process_data(file_path):
    df = pd.read_csv(file_path)

    data_by_uid = df.groupby('uid')
    
    output = {"reference": [], "generated": []}
    
    for uid, group in data_by_uid:
        reference_trajectory = group[['d', 't', 'x', 'y']].values.tolist()
        generated_trajectory = []
        
        for d, t, x, y in reference_trajectory:
            new_x, new_y = predict_next_step(x, y)
            generated_trajectory.append([d, t, new_x, new_y])
        
        output["reference"].append(reference_trajectory)
        output["generated"].append(generated_trajectory)
    
    return output

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

file_path = './test/test2_checkins_Connecticut.csv'  
output_file = 'saida.json'  

data = process_data(file_path)
save_to_json(data, output_file)
