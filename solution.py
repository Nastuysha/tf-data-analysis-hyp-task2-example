import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 1141722952 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.01
    stat, p_value = MMD(compute_kernel="laplacian", gamma=1).test(x, y)
    return pval < alpha # Ваш ответ, True или False
