import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def avg_similarity(visited, recommended):
    max_similarities = []
    
    for v in visited:
        similarities = [cosine_similarity(v.reshape(1, -1), r.reshape(1, -1))[0][0] for r in recommended]
        max_similarities.append(max(similarities))
    
    avg_sim = np.mean(max_similarities)
    return avg_sim

def diversity(recommended, visited=None):
    K = len(recommended)
    
    pairwise_similarities = []
    
    for i in range(K):
        for j in range(i + 1, K):
            similarity = cosine_similarity(recommended[i].reshape(1, -1), recommended[j].reshape(1, -1))[0][0]
            pairwise_similarities.append(similarity)
    
    if visited is not None:
        visited_pairwise_similarities = []
        
        for i in range(len(visited)):
            for j in range(i + 1, len(visited)):
                similarity = cosine_similarity(visited[i].reshape(1, -1), visited[j].reshape(1, -1))[0][0]
                visited_pairwise_similarities.append(similarity)
        
        visited_mean_similarity = np.mean(visited_pairwise_similarities) if visited_pairwise_similarities else 0
        
        diversity_score = 1 - np.mean(pairwise_similarities) / visited_mean_similarity if visited_mean_similarity > 0 else 1 - np.mean(pairwise_similarities)
    else:
        diversity_score = 1 - np.mean(pairwise_similarities)
    
    return diversity_score


def combined_score(visited, recommended, items, alpha=0.5, beta=0.5, visited_features=None):
    visited_items = items[items['detail_id'].isin(visited)]
    recommended_items = items[items['detail_id'].isin(recommended)]
    
    columns_to_drop = ['detail_id', 'name', 'latitude', 'longitude', 'photos', 'WEBSITE', 'PHONE', 'EMAIL', 'schedule']
    visited_items = visited_items.drop(columns=columns_to_drop, errors='ignore')
    recommended_items = recommended_items.drop(columns=columns_to_drop, errors='ignore')
    
    visited_features = visited_items.to_numpy()
    recommended_features = recommended_items.to_numpy() 
    
    avg_sim = avg_similarity(visited_features, recommended_features)
    div = diversity(recommended_features, visited_features)
    score = alpha * avg_sim + beta * div
    return score
