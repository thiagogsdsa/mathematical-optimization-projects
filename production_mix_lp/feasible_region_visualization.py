import numpy as np
import matplotlib.pyplot as plt

# Example data matching the optimization problem
resource_limits = {'Labor_Hours': 100, 'Raw_Material': 150}

# Fix Product_C quantity to zero
product_c_qty = 0

# Define ranges for Product_A (x) and Product_B (y)
x = np.linspace(0, 50, 500)
y = np.linspace(0, 50, 500)
X, Y = np.meshgrid(x, y)

# Calculate resource usage based on fixed Product_C quantity
labor_usage = 2 * X + 4 * Y + 3 * product_c_qty
raw_usage = 3 * X + 2 * Y + 5 * product_c_qty

# Define feasible region mask
feasible = (labor_usage <= resource_limits['Labor_Hours']) & \
           (raw_usage <= resource_limits['Raw_Material']) & \
           (X >= 0) & (Y >= 0)

plt.figure(figsize=(8, 6))
plt.title('Feasible Region for Product_A and Product_B (Product_C fixed at 0)')
plt.xlabel('Product_A quantity')
plt.ylabel('Product_B quantity')

# Plot feasible region as a translucent green area
plt.imshow(feasible.astype(int), extent=(x.min(), x.max(), y.min(), y.max()),
           origin='lower', cmap='Greens', alpha=0.3)

# Plot resource constraint boundaries
y_labor = (resource_limits['Labor_Hours'] - 2 * x) / 4
y_labor = np.clip(y_labor, 0, y.max())

y_raw = (resource_limits['Raw_Material'] - 3 * x) / 2
y_raw = np.clip(y_raw, 0, y.max())

plt.plot(x, y_labor, label='Labor Hours Constraint')
plt.plot(x, y_raw, label='Raw Material Constraint')

plt.xlim(0, x.max())
plt.ylim(0, y.max())
plt.legend()
plt.grid(True)
plt.show()
