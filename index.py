import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# INGRESAR LA FUNCIÓN COMO UNA CADENA DE CARACTERES
func_expression = input('INGRESE LA FUNCIÓN f(x): ')

# Convertir la expresión en una función simbólica
x = sp.symbols('x')
f = sp.sympify(func_expression)

# INGRESAR EL PUNTO DE EVALUACIÓN
x0 = float(input('INGRESE EL PUNTO DE EVALUACIÓN a: '))

# INGRESAR EL VALOR DE h o LA DISTANCIA ENTRE PUNTOS
h = float(input('INGRESE EL VALOR DE h: '))

# CREAMOS UN RANGO DE VALORES PARA x
x_range = np.linspace(x0 - 2 * h, x0 + 2 * h, 100)

# CALCULAMOS LAS DIFERENCIAS FINITAS
forward_diff = (f.subs(x, x0 + h) - f.subs(x, x0)) / h
backward_diff = (f.subs(x, x0) - f.subs(x, x0 - h)) / h
centered_diff = (f.subs(x, x0 + h) - f.subs(x, x0 - h)) / (2 * h)

# CALCULAR LAS DERIVADAS ANALÍTICAS (PARA COMPARAR CON LAS DIFERENCIAS FINITAS)
f_prime = sp.diff(f, x)
analytical_forward_diff = f_prime.subs(x, x0 + h)
analytical_backward_diff = f_prime.subs(x, x0 - h)
analytical_centered_diff = f_prime.subs(x, x0)

# CALCULAR LOS ERRORES
error_forward = abs(forward_diff - analytical_forward_diff)
error_backward = abs(backward_diff - analytical_backward_diff)
error_centered = abs(centered_diff - analytical_centered_diff)

# MOSTRAR RESULTADOS
print('DIFERENCIAS FINITAS__(Hacia Adelante):')
print(f'Aproximación: {forward_diff}')
print(f'Error: {error_forward}')

print('DIFERENCIAS FINITAS__(Hacia Atrás):')
print(f'Aproximación: {backward_diff}')
print(f'Error: {error_backward}')

print('DIFERENCIAS FINITAS__(Centrada):')
print(f'Aproximación: {centered_diff}')
print(f'Error: {error_centered}')

# CREAR UN RANGO PARA LA GRÁFICA
x_plot = np.linspace(x0 - 20 * h, x0 + 20 * h, 100)

# GRAFICAR LA FUNCION Y LA RECTA TANGENTE
plt.figure()

# Convertir la función simbólica en una función numérica para graficar
f_numeric = sp.lambdify(x, f, 'numpy')
tangent_line = lambda x_val: f_numeric(x0) + analytical_forward_diff * (x_val - x0)

# GRAFICAR LA FUNCIÓN
plt.plot(x_plot, f_numeric(x_plot), label='Función', linewidth=2)

# GRAFICAR LA RECTA TANGENTE
plt.gca().set_prop_cycle(None)  # Reiniciar el ciclo de colores
plt.plot(x_plot, tangent_line(x_plot), label='Recta Tangente', linewidth=2)

# PUNTO DE EVALUACIÓN
plt.scatter(x0, f_numeric(x0), c='r', label='Punto de Evaluación')

# MOSTRAR LA POSICIÓN DEL PUNTO DE EVALUACIÓN
plt.text(x0, f_numeric(x0), f'  PUNTO DE EVALUACIÓN ({x0}, {f_numeric(x0)})')

# AJUSTAR LA APARIENCIA DE LA GRÁFICA
plt.title('GRÁFICA DE LA FUNCIÓN')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.show()
