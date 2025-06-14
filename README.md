# Image Inpainting with PDE-Based Techniques

This project implements image inpainting using Partial Differential Equation (PDE) techniques, with a focus on edge detection using Laplacian PDE methods. The goal is to reconstruct missing or damaged regions of an image by leveraging the smoothness properties of PDEs and edge-preserving techniques.

## Project Overview
Image inpainting is the process of filling in missing or corrupted parts of an image in a visually coherent manner. This project uses PDE-based methods, specifically the Laplacian PDE, to propagate information from surrounding areas into the inpainting region. Edge detection is incorporated to preserve structural details, ensuring the inpainted regions align with the image's natural boundaries.

The Laplacian PDE is used to model the smoothness of the image intensity, while edge detection helps guide the inpainting process to maintain sharp transitions where necessary.

## Features
- Implementation of Laplacian PDE for image inpainting.
- Edge detection to preserve structural details during inpainting.
- Support for grayscale and color image processing.
- Customizable inpainting masks for user-defined damaged regions.
- Visualization of intermediate and final inpainting results.

## Requirements
To run this project, you need the following dependencies:
- Python 3.8+
- NumPy
- OpenCV
- Matplotlib (for visualization)

Optional:
- Jupyter Notebook (for interactive exploration)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Akshurai2004/Image-Inpainting-PDE.git
   cd Image-Inpainting-PDE
