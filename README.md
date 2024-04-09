# Butterfly Image Classification Project

## Overview

This project focuses on classifying images of butterflies into 75 different species using image classification techniques. The dataset includes training, testing, and validation sets, along with CSV files containing information about the images and butterfly species.

## Dataset Description

- **Train Set**: Consists of 9285 images partitioned into 75 subdirectories, one for each species.
- **Test Set**: Contains 375 images partitioned into 75 subdirectories, with 5 test images per species.
- **Validation Set**: Comprises 375 images partitioned into 75 subdirectories, with 5 validation images per species.
- **File Format**: All images are in JPG format with dimensions 224 x 224 x 3.

## Data Files

1. **butterflies.csv**:
   - Contains 3 columns: filepaths, labels, and dataset.
   - Each row represents an image in the dataset.
   - `filepaths`: Relative path to the image.
   - `labels`: Species label associated with the image file.
   - `dataset`: Specifies which dataset (train, test, or validation) the image belongs to.

2. **classdict.csv**:
   - Consists of 6 columns: classindex, class, SCIENTIFIC NAME, height, width, and scale by.
   - Contains 75 rows, one for each species.
   - `classindex`: Integer index of the class.
   - `class`: Common name of the butterfly species.
   - `SCIENTIFIC NAME`: Official scientific name of the species.
   - `Height` and `width`: Values used by the model when trained.
   - `scale by`: Value to scale the image pixels by.

3. **CLASS NAMES.csv**:
   - Contains 2 columns: COMMON NAME and SCIENTIFIC NAME.
   - Includes 75 rows, each representing a butterfly species.
   - `COMMON NAME`: Common name of the butterfly.
   - `SCIENTIFIC NAME`: Associated scientific name of the species.

4. **6 images file**:
   - Includes 6 butterfly images used for demonstration purposes.

## Model Usage

The provided files enable the use of a trained model for butterfly image classification. The classdict.csv file facilitates mapping between class indices and species names, while the CLASS NAMES.csv file provides common and scientific names of the butterfly species.

## Demonstration

The 6 images file can be used to demonstrate the prediction function within the kernel.

## Conclusion

This project serves as a valuable resource for researchers and enthusiasts interested in butterfly species classification using image recognition techniques. With a comprehensive dataset and associated metadata, it offers opportunities for further research and exploration in the field of computer vision and biodiversity conservation.
