import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tqdm import tqdm

# Função para analisar a distribuição do número de dias nas trajetórias
def analyze_days_distribution(df, min_uid=800):
    df_filtered = df[df['uid'] >= min_uid]
    days_per_traj = df_filtered.groupby('uid')['d'].nunique()
    
    plt.figure(figsize=(10, 6))
    plt.hist(days_per_traj, bins=30, edgecolor='k')
    plt.title('Distribuição do Número de Dias nas Trajetórias')
    plt.xlabel('Número de Dias')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()
    
    return days_per_traj

# Função para testar diferentes valores de min_days
def test_min_days(df, min_uid=800, min_days_list=[10, 14, 20, 30]):
    results = []
    for min_days in min_days_list:
        df_filtered = df[df['uid'] >= min_uid]
        valid_traj = [uid for uid, traj in df_filtered.groupby('uid') if traj['d'].nunique() >= min_days]
        results.append((min_days, len(valid_traj)))
        
    return results

# Função para testar diferentes máscaras
def test_masks(df, min_uid=8, mask_intervals=[(8, 20),(16, 30), (20, 34), (25, 39)]):
    results = []
    for mask_d_start, mask_d_end in mask_intervals:
        df_filtered = df[df['uid'] >= min_uid]
        masked_counts = []
        for uid, traj in tqdm(df_filtered.groupby('uid')):
            d = traj['d'].to_numpy()
            need_mask_idx = np.where((d >= mask_d_start) & (d <= mask_d_end))
            masked_counts.append(len(need_mask_idx[0]))
        results.append(((mask_d_start, mask_d_end), np.mean(masked_counts)))
        
    return results

# Carregar dados
path = 'testeAlabama.csv'
df = pd.read_csv(path)

# Analisar a distribuição dos dias
days_per_traj = analyze_days_distribution(df)

# Testar diferentes valores de min_days
min_days_results = test_min_days(df)
print("Resultados para diferentes valores de min_days:")
for min_days, count in min_days_results:
    print(f"min_days = {min_days}: {count} trajetórias válidas")

# Testar diferentes máscaras
mask_results = test_masks(df)
print("Resultados para diferentes máscaras:")
for (mask_d_start, mask_d_end), avg_masked in mask_results:
    print(f"Máscara {mask_d_start}-{mask_d_end}: média de {avg_masked:.2f} pontos mascarados por trajetória")
