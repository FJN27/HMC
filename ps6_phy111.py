import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --------------- part(a)-----------------------

def pendulum_system(t, y):
    theta, omega = y
    g = 9.81  # Gravitational acceleration
    L = 1.0  # length of the string
    omega0 = np.sqrt(g / L)
    tau = omega0 * t
    dtheta_dt = omega
    domega_dt = np.sin(tau) - (g / (L * omega0**2)) * np.sin(theta)
    return [dtheta_dt, domega_dt]


# Time span
t_span = (0, 20)
# Initial conditions
initial_conditions_list = [
    [0.1, 0],  # Initial condition 1
    [0.5, 0],  # Initial condition 2
    [1.0, 0],  # Initial condition 3
]

# Figure size
plt.figure(figsize=(10, 6))

for initial_conditions in initial_conditions_list:
    # Solving the DE
    sol = solve_ivp(
        pendulum_system, t_span, initial_conditions, t_eval=np.linspace(0, 20, 1000)
    )

    # Plot the trajectory
    plt.plot(
        sol.y[0],
        sol.y[1],
        label=f"Initial conditions: θ={initial_conditions[0]}, ω={initial_conditions[1]}",
    )

plt.title("Phase Space: Pendulum")
plt.xlabel(r"$\theta$ (radians)")
plt.ylabel(r"$\omega$ (radians/s)")
plt.grid()
plt.legend()
plt.show()


# --------------- part(b)-----------------------
# Define the system of ODEs
def torus_system(t, y):
    g = 9.81  # Gravitational acceleration
    L = 1.0   # Length of the pendulum rod
    omega0 = np.sqrt(g / L)  # Natural frequency

    # State variables: theta, omega, theta2 (proxy for time)
    theta, omega, theta2 = y

    dtheta_dt = omega
    domega_dt = np.sin(theta2) - (g / L* omega0**2) * np.sin(theta)  # Corrected equation
    dtheta2_dt = 1  # Theta2 evolves linearly with time

    return [dtheta_dt, domega_dt, dtheta2_dt]

# Time range and higher resolution
t_span = (0, 100)  # Increase time range to capture more points
t_eval = np.linspace(0, 100, 50000)  # Increase resolution for accuracy

# List of different initial conditions to explore (theta, omega, theta2)
initial_conditions_list = [
    [0.1, 0, 0],  # Regular motion (small initial angle)
    [1.0, 0.5, 0],  # Larger initial angle
    [2.0, 1.0, 0],  # More energy in the system
    [3.0, -0.5, 0],  # Negative initial angular velocity
    [0.5, 2.0, 0]   # High initial angular velocity
]

# Prepare the plot
plt.figure(figsize=(10, 6))

# Loop over different initial conditions
for initial_conditions in initial_conditions_list:
    # Solve the ODEs
    sol_torus = solve_ivp(
        torus_system, t_span, initial_conditions, t_eval=t_eval
    )

    # Extract points for the surface of section at multiples of 2π
    theta_values = []
    omega_values = []
    
    # The for loop iterates over each time step t where the solver (solve_ivp) has computed the solution.
    # Then, it divides values of theta2 by 2pi and calcultates the reminder
    # if the reminder if zero, meaning that it is an integral of 2pi, we compuate values of theta and omega
    for i in range(len(sol_torus.t)):
        theta2_mod = sol_torus.y[2][i] % (2 * np.pi)

        if np.isclose(theta2_mod, 0, atol=1e-1):  # Increased tolerance
            theta_values.append(sol_torus.y[0][i])
            omega_values.append(sol_torus.y[1][i])

    # Plot the surface of section for this initial condition
    plt.scatter(theta_values, omega_values, s=5, label=f"IC: {initial_conditions}")

# Customize the plot
plt.title("Surface of Section at $\Theta_2 = 0, 2\pi, 4\pi, \dots$")
plt.xlabel(r"$\theta$ (radians)")
plt.ylabel(r"$\omega$ (radians/s)")
plt.grid()
plt.axis("equal")  # Keep aspect ratio equal
plt.legend(loc='best')
plt.xlim(-20, 20)  # Set appropriate axis limits
plt.ylim(-10, 10)

# Show the plot
plt.show()


#------------------part (c)----------------

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE system for the double pendulum with θ2 as the independent variable
def double_pendulum(z, theta2):
    omega1, omega2, theta1 = z  # Unpack the state vector
    delta_theta = theta1 - theta2  # Δθ = θ1 - θ2

    # ODEs for the system
    d_omega1_dtheta2 = (
        -np.sin(delta_theta) * (omega1**2 * np.cos(delta_theta) + omega2**2)
        - 2 * np.sin(theta1) + np.sin(theta2) * np.cos(delta_theta)
    ) / (omega2 * (1 + np.sin(delta_theta)**2))

    d_omega2_dtheta2 = (
        np.sin(delta_theta) * (omega1**2 + omega2**2 * np.cos(delta_theta))
        + np.sin(theta1) * np.cos(delta_theta) - 2 * np.sin(theta2)
    ) / (omega2 * (1 + np.sin(delta_theta)**2))

    d_theta1_dtheta2 = omega1 / omega2  # dθ1 / dθ2

    return [d_omega1_dtheta2, d_omega2_dtheta2, d_theta1_dtheta2]

# Parameters
N = 11  # Number of initial conditions in the grid
H = 1   # Hamiltonian value

# Generate initial conditions
omega1_0 = np.linspace(-2, 2, N)  # Range of ω1 values
omega2_0 = np.linspace(-2, 2, N)  # Range of ω2 values
theta1_0 = np.zeros((N, N))  # Initialize θ1 grid

# Compute the initial values of θ1 using the Hamiltonian constraint
for a in range(N):
    for b in range(N):
        if omega1_0[a] * omega2_0[b] != 1:  # Avoid singularity
            cos_theta1 = (1 + H - omega1_0[a]**2 - 0.5 * omega2_0[b]**2) / (omega1_0[a] * omega2_0[b] - 1)
            cos_theta1 = np.clip(cos_theta1, -1, 1)  # Clamp to valid range for arccos
            theta1_0[a, b] = np.arccos(cos_theta1)
        else:
            theta1_0[a, b] = 0  # Assign default value to avoid division by zero

# Values of theta2 (similar to time span)
theta2 = np.linspace(0, 200 * np.pi, 10000)  # Generate 10,000 points from 0 to 50π

# Create the phase space plot
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through each combination of initial conditions
for i in range(N):
    for j in range(N):
        z0 = [omega1_0[i], omega2_0[j], theta1_0[i, j]]  # Initial state vector
        z = odeint(double_pendulum, z0, theta2)  # Solve the ODE system

        # Extract ω1 and θ1 from the solution matrix z
        y = z[:, 0]  # ω1
        x = z[:, 2]  # θ1

        # Plot the points on the phase space plot
        ax.scatter((x + np.pi) % (2 * np.pi) - np.pi, y, c=[i / N, 0, (1 - i / N)], s=1)

# Customize the plot
ax.set_xlabel(r'$\theta_1$ (radians)')
ax.set_ylabel(r'$\omega_1$ (radians/s)')
ax.set_ylim(-3, 3)
ax.set_title("Phase Space of Double Pendulum")

# Display the plot
plt.grid(True)
plt.show()
