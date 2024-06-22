import json
import geobleu
import pandas as pd


with open('/home/alvaro/Documentos/GitHub/LP-BERT/result/task1/2024_06_18_13_46_49.json', 'r') as f:
    data = json.load(f)

all_trajectories = {"generated": [], "reference": []}
for traj_group in data:
    all_trajectories[traj_group] = [tuple(step) for traj_list in data[traj_group] for step in traj_list]

generated = all_trajectories['generated']
reference = all_trajectories['reference']


# num_coords_generated = ([len(traj) for traj in generated])
# num_coords_reference = ([len(traj) for traj in reference])

# for traj in generated:
#     print(traj)

# print("Número de coordenadas nas trajetórias geradas:", num_coords_generated)
# print("Número de coordenadas nas trajetórias de referência:", num_coords_reference)

# similarity = geobleu.calc_geobleu_orig(generated, reference)
# print(similarity)

geobleu_val = geobleu.calc_geobleu(generated, reference)
dtw_val = geobleu.calc_dtw(generated, reference)

print('Resultado GeoBleu: ', geobleu_val)
print('Resultado DTW: ', dtw_val)
