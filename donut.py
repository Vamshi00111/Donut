import math
import os
import time

# Constants
theta_spacing = 0.07
phi_spacing = 0.02

R1 = 1  # Inner radius of the torus
R2 = 2  # Outer radius of the torus
K2 = 5  # Distance between viewer and donut
screen_width = 120  # Width of the terminal screen
screen_height = 40  # Height of the terminal screen

# Calculate K1 based on the screen size
K1 = screen_width * K2 * 2 / (8 * (R1 + R2))


def render_frame(A, B):
    # Precompute sines and cosines of A and B
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    # Initialize the output and zbuffer
    output = [[" " for _ in range(screen_width)] for _ in range(screen_height)]
    zbuffer = [[0 for _ in range(screen_width)] for _ in range(screen_height)]

    # Theta goes around the cross-sectional circle of a torus
    for theta in frange(0, 2 * math.pi, theta_spacing):
        # Precompute sines and cosines of theta
        costheta = math.cos(theta)
        sintheta = math.sin(theta)

        # Phi goes around the center of revolution of a torus
        for phi in frange(0, 2 * math.pi, phi_spacing):
            # Precompute sines and cosines of phi
            cosphi = math.cos(phi)
            sinphi = math.sin(phi)

            # The x, y coordinate of the circle before revolving
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            # Final 3D (x, y, z) coordinates after rotations
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z  # "one over z"

            # x and y projection
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            # Ensure xp and yp are within bounds
            if 0 <= xp < screen_width and 0 <= yp < screen_height:
                # Calculate luminance
                L = (
                    cosphi * costheta * sinB
                    - cosA * costheta * sinphi
                    - sinA * sintheta
                    + cosB * (cosA * sintheta - costheta * sinA * sinphi)
                )

                # If L > 0, plot it
                if L > 0:
                    # Test against the z-buffer
                    if ooz > zbuffer[yp][xp]:
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L * 8)
                        luminance_index = max(0, min(11, luminance_index))  # Clamp to 0-11
                        output[yp][xp] = ".,-~:;=!*#$@"[luminance_index]

    # Render the frame
    os.system("cls" if os.name == "nt" else "clear")
    print("\x1b[H", end="")
    for row in output:
        print("".join(row))


def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


# Main loop
A = 0
B = 0
while True:
    render_frame(A, B)
    A += 0.04
    B += 0.02
    time.sleep(0.03)
