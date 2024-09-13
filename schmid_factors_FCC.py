"""
Created on Fri Sep 13 22:40:05 2024

@author:
 Devendra Nagpure
 Ph.D Research Scholar
 MSB-337, Mechanical Sciences Block, Dept. Mechanical Engg., 
 Indian Institute of Technology Madras, Chennai 600 036
"""
import numpy as np

def calculate_schmid_factors(re_stress, loading_direction):
    # Define slip systems for FCC: (Slip Plane, Slip Direction)
    slip_systems = [
        (np.array([1, 1, 1]), np.array([1, -1, 0])),
        (np.array([1, 1, 1]), np.array([1, 0, -1])),
        (np.array([1, 1, 1]), np.array([0, 1, -1])),
        (np.array([1, -1, 1]), np.array([1, 1, 0])),
        (np.array([1, -1, 1]), np.array([1, 0, 1])),
        (np.array([1, -1, 1]), np.array([0, 1, 1])),
        (np.array([1, 1, -1]), np.array([1, 1, 0])),
        (np.array([1, 1, -1]), np.array([0, 1, 1])),
        (np.array([1, 1, -1]), np.array([1, 0, 1])),
        (np.array([-1, 1, 1]), np.array([1, 1, 0])),
        (np.array([-1, 1, 1]), np.array([1, 0, 1])),
        (np.array([-1, 1, 1]), np.array([0, 1, 1])),
    ]

    # Normalize the loading direction
    loading_direction = np.array(loading_direction)
    loading_direction = loading_direction / np.linalg.norm(loading_direction)

    # Calculate Schmid factors
    schmid_factors = []
    for plane_normal, slip_direction in slip_systems:
        # Normalize the slip plane normal and slip direction
        plane_normal = plane_normal / np.linalg.norm(plane_normal)
        slip_direction = slip_direction / np.linalg.norm(slip_direction)
        
        # Calculate cos(phi) and cos(lambda)
        cos_phi = np.dot(loading_direction, plane_normal)
        cos_lambda = np.dot(loading_direction, slip_direction)
        
        # Calculate Schmid factor
        schmid_factor = (cos_phi * cos_lambda)
        schmid_factors.append(schmid_factor)
        # Calculate resolved shear stress
        load= re_stress/schmid_factor

    # Calculate average Schmid factor
    #average_schmid_factor = np.mean(schmid_factors)
    
    # Output results in a table format
    print(f"{'Slip Plane':<15} {'Slip Direction':<15} {'cos(phi)':<10} {'cos(lambda)':<10} {'Schmid Factor':<15} {'Stress':<15}")
    for i, (plane_normal, slip_direction) in enumerate(slip_systems):
        cos_phi = np.dot(loading_direction, plane_normal / np.linalg.norm(plane_normal))
        cos_lambda = np.dot(loading_direction, slip_direction / np.linalg.norm(slip_direction))
        schmid_factor = schmid_factors[i]
        load= re_stress/schmid_factor
        print(f"{' '.join(map(str, plane_normal.tolist())):<15} {' '.join(map(str, slip_direction.tolist())):<15} {cos_phi:<10.3f} {cos_lambda:<10.3f} {schmid_factor:<15.3f} {load:<15.3f}")
    
    #print(f"\nAverage Schmid Factor: {average_schmid_factor:.3f}")

# Example usage
re_stress= 50 # Critical resolved shear stress
loading_direction = [1, 1, 2]  # For loading direction eg. [100]
calculate_schmid_factors(re_stress, loading_direction)
