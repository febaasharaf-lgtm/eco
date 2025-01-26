 # eco
 Project Name:EchoBin
 
 Team Name:Code Red
 
 # Team Members:
 
  • Member 1:Feba Asharaf - College of Engineering Chenganuur
  
  • Member 2:Gayatri Sabin - College of Engineering Chenganuur
  
  Hosted Project Link: https://github.com/febaasharaf-lgtm/eco

 ### Project Description:
 
 This project develops an AI-powered waste classification system using the pre-trained MobileNetV2 model. It automates the process of classifying waste as Recyclable or Non-recyclable, enabling efficient waste segregation. The solution includes a REST API for real-time image classification, supporting better recycling practices and reducing environmental impact.

### The Problem Statement:
 
 Improper waste segregation leads to inefficient recycling, increased pollution, and resource wastage. Manual sorting is labor-intensive and error-prone. This project provides an automated system to accurately classify waste, improving waste management and promoting sustainability.

 ### The Solution:
 
The solution is an AI-powered system that uses a pre-trained MobileNetV2 model to classify waste as Recyclable or Non-recyclable based on images. It includes a Flask-based REST API for real-time classification, enabling easy integration into smart waste management systems to improve recycling efficiency and reduce environmental impact.
 
 
# 🌿 EcoBin

Waste Classification Using MobileNetV2
### Overview
This project focuses on building a machine learning model that classifies waste into two categories: Recyclable and Non-recyclable. Using a pre-trained MobileNetV2 model, this solution enables quick and accurate waste classification. The project also includes a REST API for easy integration and real-time image classification.

## Technical Details

### Technologies/Components Used

### For Software:

  •Languages Used: Python,Javascript,HTML
  
  •Frameworks used: TensorFlow 2.x
  
  •Libraries Used: Pillow,Flask
               
  •Tools Used: Visual Studio Code,Git,Kaggle
  

Table of Contents
1. Features
2. Technologies Used
3. Dataset
4. Setup Instructions
5. Usage
   Training the Model
   Testing the Model
   Deploying the API
6. Project Structure
7. Future Improvements
8. Contact
   
Features

Binary Classification: Identifies waste as either recyclable or non-recyclable.
Pre-trained Model: Uses MobileNetV2, pre-trained on ImageNet for efficient feature extraction.
Data Augmentation: Augments training data for better generalization.
REST API Integration: Flask-based API for real-time waste classification.

Technologies Used

Programming Language: Python 3.7+,Javascript,HTML
Deep Learning Framework: TensorFlow 2.x
Libraries:  Pillow, Flask
Pre-trained Model: MobileNetV2

Dataset

The dataset must be organized in the following structure:

dataset/

├── train/

│   ├── recyclable/# Images of recyclable waste

│   └── non-recyclable/ # Images of non-recyclable waste

└── test/
    ├── recyclable/ 
    └── non-recyclable/

Download public datasets like TrashNet or Kaggle Waste Classification.
Each category folder should contain relevant images (e.g., recyclable materials like plastic bottles, and non-recyclable materials like food waste).
Setup Instructions

Follow these steps to set up the project locally:

1. Clone the Repository git clone <repository-url>
cd WasteClassification
2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install tensorflow numpy pillow flask
4. Prepare the Dataset
Place your dataset in the dataset/ folder, organized as shown in the Dataset section.
Usage

Training the Model
1. Run the waste_classifier.py script:
python  waste_classifier.py
2. The trained model will be saved as waste_classifier.h5.
Testing the Model
1. Open the classify.py script.
2. Replace the test_image_path with the path to your test image.
3. Run the script:
python classify.py
4. Output Example:
Classification Result: Recyclable
Project Structure

WasteClassification/

├── train.py          # Script to train the model

├── classify.py       # Script to classify a single image

├── app.py            # Flask app for deploying the model

├── waste_classifier.h5  # Trained model file

├── dataset/          # Dataset folder (contains train/test data)

└── README.md         # Project documentation


Screenshots:

Front-End
![Screenshot 2025-01-26 073854](https://github.com/user-attachments/assets/513a18ba-9854-483d-943d-74a34e3a3077)

Cascading Style Sheets
![Screenshot 2025-01-26 073917](https://github.com/user-attachments/assets/930cdc5d-4a1a-49f1-ab2c-7971aa4bcfe2)

JavaScrip code for a function named getRecyclingCenters
![Screenshot 2025-01-26 073956](https://github.com/user-attachments/assets/20361901-c90a-436b-8d8e-bd8bba7405ef)

 
 Workflow Diagram:

------------------+        +----------------------+        +------------------+
|   User Upload    | -----> | Image Preprocessing  | -----> | MobileNetV2 Model |
| (Waste Image)    |        | (Resize, Normalize)  |        | (Classify Image)  |
+------------------+        +----------------------+        +------------------+
                                   |                                |
                                   v                                v
                           +------------------+            +------------------+
                           | API Response     | <--------- | Classification   |
                           | (Recyclable or   |            | Result (JSON)    |
                           | Non-Recyclable)  |            +------------------+
                           +------------------+



  
Future Improvements

1. Enhance dataset size and diversity for better accuracy.
2. Implement multi-class classification for detailed waste categorization.
3. Integrate with IoT devices for automated waste management.
4. Deploy the model to the cloud for global accessibility

Team Contributions:
•Feba Asharaf :Front end and Back end
•Gayatri Sabin :Front end and Back end


Contact

For questions or collaboration:

Email: asharaffeba@gmail.com

GitHub: [https://github.com/your-febaasharaf-lgtm]





