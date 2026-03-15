import numpy as np

OBSTACLES = [
    {"bounds": [0.45, 0.65, -0.25, -0.05]}, 
]

K_OBS   = 120.0   # repulsion stiffness
K_FRIC  = 15.0   # friction coefficient

def obstacle_force(x, dx=None):
    F = np.zeros(2)
    margin = 0.05  # start pushing before contact

    for obs in OBSTACLES:
        x_min, x_max, y_min, y_max = obs["bounds"]

        d_left  = x[0] - (x_min - margin)
        d_right = (x_max + margin) - x[0]
        d_down  = x[1] - (y_min - margin)
        d_up    = (y_max + margin) - x[1]

        if d_left < 0 or d_right < 0 or d_down < 0 or d_up < 0:
            continue  # outside the margin zone entirely

        min_d = min(d_left, d_right, d_down, d_up)

        if min_d == d_left:
            F += np.array([-K_OBS * d_left,  0.0])
        elif min_d == d_right:
            F += np.array([ K_OBS * d_right, 0.0])
        elif min_d == d_down:
            F += np.array([0.0, -K_OBS * d_down])
        else:
            F += np.array([0.0,  K_OBS * d_up])

        if dx is not None and np.linalg.norm(dx) > 1e-3:
            if min_d in (d_left, d_right):
                F += np.array([0.0, -K_FRIC * dx[1]])
            else:
                F += np.array([-K_FRIC * dx[0], 0.0])

    return F