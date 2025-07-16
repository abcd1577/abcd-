from sklearn.metrics import f1_score

def find_optimal_threshold(y_true,y_pred):
    """寻找最大化F1分数的阈值"""
    best_threshold=0.5
    best_score=0
    for threshold in [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45]:
        y_pred=(y_pred>threshold).astype(int)
        f1=f1_score(y_true,y_pred)
        if f1>best_score:
            best_score=f1
            best_threshold=threshold
    return best_threshold,best_score
# Compare this snippet from 01_data_exploration.ipynb#W4sZmlsZQ%3D%3D: