import numpy as np
import matplotlib.pyplot as plt

def poincare_map(time_series, delay):
    poincare_points = []
    for i in range(len(time_series) - delay):
        poincare_points.append([time_series[i], time_series[i + delay]])
    return np.array(poincare_points)

# Örnek bir zaman serisi oluşturalım (örneğin, bir sine dalgası)
t = np.arange(0, 100, 0.1)
time_series = np.sin(t)

# Poincaré haritası için gerekli parametreler
delay = 10  # Gecikme sayısı

# Poincaré haritasını oluştur
poincare_points = poincare_map(time_series, delay)

# Poincaré haritasını çiz
plt.figure(figsize=(8, 6))
plt.plot(poincare_points[:, 0], poincare_points[:, 1], 'bo', markersize=2)
plt.xlabel('x(n)')
plt.ylabel('x(n + {})'.format(delay))
plt.title('Poincaré Haritası')
plt.grid(True)
plt.show()
