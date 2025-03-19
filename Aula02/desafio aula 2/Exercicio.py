# Passo 1: Definir as listas de valores de x e y

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Passo 2: Calcular a média de x e y

def calcular_media(lista):
    return sum(lista) / len(lista)

# Calculando a média de x e y

media_x = calcular_media(x)
media_y = calcular_media(y)

# Passo 3: Calcular os somatórios necessários para calcular os coeficientes
# Somatório de (x_i - média_x) * (y_i - média_y)

somatorio_xy = 0

# Somatório de (x_i - média_x)²

somatorio_xx = 0

for i in range(len(x)):
    somatorio_xy += (x[i] - media_x) * (y[i] - media_y)
    somatorio_xx += (x[i] - media_x) ** 2

# Passo 4: Calcular os coeficientes beta_1 e beta_0

beta_1 = somatorio_xy / somatorio_xx
beta_0 = media_y - beta_1 * media_x

# Passo 5: Exibir os resultados

print(f'Coeficiente beta_0 (interceptação): {beta_0}')
print(f'Coeficiente beta_1 (declive): {beta_1}')
