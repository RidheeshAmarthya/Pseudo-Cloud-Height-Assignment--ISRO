# import numpy as np
# import h5py
# import pandas as pd
# import matplotlib.pyplot as plt
# from PIL import Image

# pd.options.display.width= None
# pd.options.display.max_columns= None
# pd.set_option('display.max_rows', 3000)
# pd.set_option('display.max_columns', 3000)


# fn = '/Users/kali/Desktop/temp-git/Pseudo-Cloud-Height/test.h5'
# f = h5py.File(fn, 'r')

# print(list(f.keys()))

# TIR1_TEMP = f['IMG_TIR1_TEMP'][:]
# TIR1 = f['IMG_TIR1'][:]
# lati = f['Latitude'][:]
# longi = f['Longitude'][:]

# print(np.shape(TIR1))

# # TIR1_ = np.squeeze(TIR1)
# # print(np.shape(TIR1_))
# # tempr = np.zeros((2816, 2805))
# # alt = np.zeros((2816, 2805))
# # for i in range(2816):
# #     for j in range(2805):
# #         tempr[i, j] = TIR1_TEMP[TIR1_[i, j]]-273
# #
# #         if tempr[i, j] > 15:
# #             alt[i, j] = 0
# #
# #         elif 13 < tempr[i, j] < 15:
# #             alt[i, j] = 1000
# #
# #         elif 11 < tempr[i, j] < 13:
# #             alt[i, j] = 2000
# #
# #         elif 9.1 < tempr[i, j] < 11:
# #             alt[i, j] = 3000
# #
# #         elif 7.1 < tempr[i, j] < 9.1:
# #             alt[i, j] = 4000
# #
# #         elif 5.1 < tempr[i, j] < 7.1:
# #             alt[i, j] = 5000
# #
# #         elif 3.1 < tempr[i, j] < 5.1:
# #             alt[i, j] = 6000
# #         elif 1.1 < tempr[i, j] < 3.1:
# #             alt[i, j] = 7000
# #         elif -0.8 < tempr[i, j] < 1.1:
# #             alt[i, j] = 8000
# #         elif -2.8 < tempr[i, j] < -0.8:
# #             alt[i, j] = 9000
# #         elif -4.8 < tempr[i, j] < -2.8:
# #             alt[i, j] = 10000
# #         elif -6.8 < tempr[i, j] < -4.8:
# #             alt[i, j] = 11000
# #         elif -8.8 < tempr[i, j] < -6.8:
# #             alt[i, j] = 12000
# #         elif -10.8 < tempr[i, j] < -8.8:
# #             alt[i, j] = 13000
# #         elif -12.7 < tempr[i, j] < -10.8:
# #             alt[i, j] = 14000
# #         elif -14.7 < tempr[i, j] < -12.7:
# #             alt[i, j] = 15000
# #         elif -16.7 < tempr[i, j] < -14.7:
# #             alt[i, j] = 16000
# #         elif -18.7 < tempr[i, j] < -16.7:
# #             alt[i, j] = 17000
# #         elif -20.7 < tempr[i, j] < -18.7:
# #             alt[i, j] = 18000
# #         elif -22.6 < tempr[i, j] < -20.7:
# #             alt[i, j] = 19000
# #         elif -24.6 < tempr[i, j] < -22.6:
# #             alt[i, j] = 20000
# #         elif -26.6 < tempr[i, j] < -24.6:
# #             alt[i, j] = 21000
# #         elif -28.6 < tempr[i, j] < -26.6:
# #             alt[i, j] = 22000
# #         elif -30.6 < tempr[i, j] < -28.6:
# #             alt[i, j] = 23000
# #         elif -32.5 < tempr[i, j] < -30.6:
# #             alt[i, j] = 24000
# #         elif -34.5 < tempr[i, j] < -32.5:
# #             alt[i, j] = 25000
# #         elif -36.5 < tempr[i, j] < -34.5:
# #             alt[i, j] = 26000
# #         elif -38.5 < tempr[i, j] < -36.5:
# #             alt[i, j] = 27000
# #         elif -40.5 < tempr[i, j] < -38.5:
# #             alt[i, j] = 28000
# #         elif -42.5 < tempr[i, j] < -40.5:
# #             alt[i, j] = 29000
# #         elif -44.4 < tempr[i, j] < -42.5:
# #             alt[i, j] = 30000
# #         elif -46.4 < tempr[i, j] < -44.4:
# #             alt[i, j] = 31000
# #         elif -48.4 < tempr[i, j] < -46.4:
# #             alt[i, j] = 32000
# #         elif -50.4 < tempr[i, j] < -48.4:
# #             alt[i, j] = 33000
# #         elif -52.4 < tempr[i, j] < -50.4:
# #             alt[i, j] = 34000
# #         elif -54.3 < tempr[i, j] < -52.4:
# #             alt[i, j] = 35000
# #         elif -56.3 < tempr[i, j] < -54.3:
# #             alt[i, j] = 36000
# #         elif -56.5 < tempr[i, j] < -56.3:
# #             alt[i, j] = 37000
# #         elif -92.91098022 < tempr[i,j] < -56.5:
# #             alt[i,j] = 36000
# #         else:
# #             alt[i, j] = 0
# #
# # #
# # # im = plt.imshow(alt, cmap='gray')
# # im = plt.imshow(alt )
# # plt.colorbar(im)
# # plt.savefig('cloud_texture.png', bbox_inches='tight', dpi=600)
# # plt.show()
# #
# # img = Image.open("cloud_texture.png")
# # area = (330, 94, 2541, 2311)
# # cropped_img = img.crop(area)
# # cropped_img.save("cropped_cloud_texture.png")
# #
# # ct = Image.open("cropped_cloud_texture.png")
# # rgba = ct.convert("RGBA")
# # datas = rgba.getdata()
# # newData = []
# # for item in datas:
# #    if item[0] == 0 and item[1] == 0 and item[2] == 0:
# #        newData.append((255, 255, 255, 0))
# #    else:
# #       newData.append(item)
# # rgba.putdata(newData)
# # rgba.save("transparent_cloud_texture.png", "PNG")

# tex = Image.open("/Users/kali/Desktop/temp-git/Pseudo-Cloud-Height/8081_earthmap2k.png").convert('RGB')
# print(tex.size)
# cld = Image.open("/Users/kali/Desktop/temp-git/Pseudo-Cloud-Height/transparent_cloud_texture.png").convert('RGB')
# print(cld.size)
# cld = cld.resize(tex.size)
# print(cld.size)
# Image.blend(cld, tex, .5).save("final_cloud.png")



# import pyvista

# sphere = pyvista.Sphere(
#     radius=1, theta_resolution=120, phi_resolution=120, start_theta=270.001, end_theta=270
# )

# # Initialize the texture coordinates array
# sphere.active_t_coords = np.zeros((sphere.points.shape[0], 2))

# # Populate by manually calculating
# for i in range(sphere.points.shape[0]):
#     sphere.active_t_coords[i] = [
#         0.5 + np.arctan2(-sphere.points[i, 0], sphere.points[i, 1]) / (2 * np.pi),
#         0.5 + np.arcsin(sphere.points[i, 2]) / np.pi,
#     ]

# p = pyvista.Plotter()

# while True:
#     #ftex = pyvista.read_texture("/Users/kali/Desktop/temp-git/Pseudo-Cloud-Height/final_cloud.png")
#     gtex = pyvista.read_texture("/Users/kali/Desktop/temp-git/Pseudo-Cloud-Height/transparent_cloud_texture.png")
#     mesh1 = pyvista.Sphere()
#     mesh1.texture_map_to_sphere(inplace=True)
#     mesh1.plot(texture=gtex)






import os
import numpy as np
import h5py
import pyvista as pv

# Load the .h5 file
fn = '3DIMG_01JUN2022_0000_L1B_STD.h5'
with h5py.File(fn, 'r') as f:
    TIR1_TEMP = f['IMG_TIR1_TEMP'][:]
    TIR1 = f['IMG_TIR1'][:]
    lati = f['Latitude'][:]
    longi = f['Longitude'][:]

# Constants
lapse_rate = -6.5  # Standard lapse rate in K/km
T_surface = 288.15  # Assumed surface temperature in Kelvin (15°C)

# Subsample data
subsample_factor = 5
lati_sub = lati[::subsample_factor, ::subsample_factor]
longi_sub = longi[::subsample_factor, ::subsample_factor]
TIR1_sub = TIR1[0, ::subsample_factor, ::subsample_factor]

# Calculate temperature values
temp_sub = TIR1_TEMP[TIR1_sub]

# Calculate cloud height using a simple lapse rate model
cloud_height_km = (T_surface - temp_sub) / lapse_rate  # in km

# Find and filter out occurrences of the lowest value
min_height = np.min(cloud_height_km)
mask = cloud_height_km != min_height

# Apply mask to filter out the lowest values
x_vals = np.linspace(0, 1, longi_sub.shape[1])
y_vals = np.linspace(0, 1, lati_sub.shape[0])
x, y = np.meshgrid(x_vals, y_vals)

x_flat = x.ravel()[mask.ravel()]
y_flat = y.ravel()[mask.ravel()]
z_flat = (cloud_height_km * 0.0005).ravel()[mask.ravel()]  # Apply scaling factor

# Create a point cloud with PyVista excluding lowest values
point_cloud = pv.PolyData(np.c_[x_flat, y_flat, z_flat])
point_cloud["cloud_height"] = cloud_height_km.ravel()[mask.ravel()]

# Create a plotter and add points with grey colors and transparency
plotter_clouds = pv.Plotter()
plotter_clouds.add_points(point_cloud, color="white", opacity=0.1)  # Set color to grey and adjust opacity

# Path to your image file for texture
image_path = 'earth.png'  # Update this path to your actual image location

if os.path.isfile(image_path):
    # Create a plane and apply texture if image exists
    plane = pv.Plane(center=(0.5, 0.5, -0.001), i_size=1, j_size=1)
    texture = pv.read_texture(image_path)
    plotter_clouds.add_mesh(plane, texture=texture)

plotter_clouds.camera_position = [(0.5, 0.5, 10), (0.5, 0.5, 0), (0, 1, 0)]

# Show the plot
plotter_clouds.show()
