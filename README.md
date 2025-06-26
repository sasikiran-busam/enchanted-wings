🦋 Butterfly Species Classification Using VGG16
This project uses a pre-trained VGG16 deep learning model to classify images of butterflies into 75 different species. The model is trained using transfer learning on a labeled butterfly dataset, with data augmentation and early stopping to improve generalization and prevent overfitting.

📁 Dataset
The dataset consists of 75 classes of butterfly species, containing labeled images for each species. The dataset was manually collected and organized into training, validation, and test sets.

🚀 Features
Dataset split into training, validation, and test sets

Image augmentation for better generalization

Transfer learning using VGG16 model (pre-trained on ImageNet)

Prediction support for individual butterfly images

Model saved for future use and deployment in web applications

⚙️ Usage
Prepare the dataset and organize it into train, val, and test folders (with subfolders for each class).

Run the training script/notebook to train the model.

Use the saved model (model.h5) to perform inference on new butterfly images.

Deploy the model using a Flask web application with a user-friendly interface.

