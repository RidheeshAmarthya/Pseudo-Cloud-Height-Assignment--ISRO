# Pseudo-Cloud-Height
Data Processing from INSAT 3D 3DR to get cloud height based on lapse rate

Requires 3DIMG_01AUG2022_0000_L1B_STD_V01R00.h5 from MOSDAC to run, get it from here!
 ```bash
https://drive.google.com/file/d/1rx52MuekrAtYAAIOTwgApud0S9IsDXAA/view?usp=sharing
```

```markdown
# Pseudo-Cloud-Height Visualization

This project visualizes cloud heights using temperature data from an HDF5 file. It utilizes PyVista for 3D plotting and visualization, allowing users to interactively explore cloud height data with a textured base image representing Earth.

## Features

- Visualizes cloud heights as a 3D point cloud.
- Applies a grey color scheme with transparency for better visibility.
- Integrates a textured plane as the base image (e.g., Earth).
- Filters out the lowest cloud height values for cleaner visualization.

## Requirements

- Python 3.8+
- NumPy
- h5py
- PyVista

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Pseudo-Cloud-Height.git
   cd Pseudo-Cloud-Height
   ```

2. **Install dependencies:**
   Use pip to install the required Python packages:
   ```bash
   pip install numpy h5py pyvista
   ```

## Usage

1. **Prepare your data:**
   Ensure you have an HDF5 file (`test.h5`) containing the necessary datasets (`IMG_TIR1_TEMP`, `IMG_TIR1`, `Latitude`, `Longitude`). These files can be found on MOSDAC.

2. **Run the script:**
   Execute the main script to generate the visualization:
   ```bash
   python main.py
   ```

3. **View the visualization:**
   The script will display an interactive 3D plot with cloud height data and a textured base image.

## Configuration

- **Subsample Factor:** Adjust `subsample_factor` in the script to control data resolution.
- **Image Path:** Ensure `earth.png` is located at the specified path or update `image_path` in the script.

## Example Data

The example HDF5 file should contain datasets structured as follows:
- `IMG_TIR1_TEMP`: Temperature data used to calculate cloud heights.
- `IMG_TIR1`: Index mapping for temperature data.
- `Latitude` and `Longitude`: Geographical coordinates.

## Troubleshooting

- **FileNotFoundError:** Verify that paths to data files and images are correct.
- **Dependencies:** Ensure all required packages are installed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
