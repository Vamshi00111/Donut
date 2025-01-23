# Donut Renderer in Python

This project is a Python implementation of a rotating ASCII art donut. It uses mathematical concepts from 3D graphics and trigonometry to render a torus (a donut shape) on the terminal screen in real-time.

---

## Features
- Renders a 3D torus using ASCII characters in the terminal.
- Rotates the torus dynamically, creating a hypnotic visual effect.
- Uses z-buffering to ensure proper depth representation.
- Adjusts brightness based on surface angles and light reflection.

---

## How It Works
1. **3D Rotation and Projection:**
   - The torus is mathematically defined using parametric equations for a circle rotated in 3D space.
   - The program calculates the 3D coordinates and projects them onto a 2D plane (the terminal).

2. **Luminance Calculation:**
   - The brightness of each point on the donut is calculated based on its angle relative to a simulated light source.
   - Brightness values are mapped to a set of ASCII characters to create shading effects.

3. **Z-Buffering:**
   - To simulate depth, the program uses a z-buffer to store the depth of each pixel.
   - Only the closest points to the viewer are rendered.

---

## Code Highlights
### Constants
- `theta_spacing` and `phi_spacing`: Define the resolution of the donut.
- `R1` and `R2`: Radii of the torus.
- `K1` and `K2`: Constants for scaling and perspective projection.

### Main Functions
- **`render_frame(A, B)`**: 
  - Handles the rotation, projection, and rendering of the torus.
  - Updates the ASCII display and z-buffer for each frame.

- **`frange(start, stop, step)`**: 
  - Helper function for generating values with floating-point increments.

---

## Usage
### Prerequisites
- Python 3.x

### Running the Program
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd donut-renderer
   ```
3. Run the script:
   ```bash
   python donut.py
   ```

### Controls
- No manual controls are required. The animation runs continuously until interrupted (Ctrl+C).

---

## Customization
- **Resolution:**
  - Modify `theta_spacing` and `phi_spacing` to change the smoothness of the donut.
- **Size and Scale:**
  - Adjust `R1`, `R2`, `K1`, and `K2` for different torus sizes or projection styles.
- **Screen Dimensions:**
  - Update `screen_width` and `screen_height` to match your terminal size.

---
