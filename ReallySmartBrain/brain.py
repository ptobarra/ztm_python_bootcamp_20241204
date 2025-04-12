# https://github.com/OlafenwaMoses/ImageAI
# A python library built to empower developers to build applications and systems with self-contained Computer Vision capabilities

# New Version:
# imageai.Prediction no longer exists, replaced by imageai.Classification
from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()

# https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Classification

prediction = ImageClassification()
# SqueezeNet model also no longer exists, now the fastest is MobileNetV2
# prediction.setModelTypeAsMobileNetV2()
# prediction.setModelPath(os.path.join(exec_path, r'ReallySmartBrain/mobilenet_v2-b0353104.pth'))


# Set the model type and path
model_path = os.path.join(exec_path, r"ReallySmartBrain/resnet50-19c8e357.pth")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Please ensure the file exists.")

prediction.setModelTypeAsResNet50()
prediction.setModelPath(model_path)
print(model_path)


# Load the model
try:
    prediction.loadModel()
except Exception as e:
    raise RuntimeError(f"Failed to load the model. Error: {e}")

# predctions, probabilities = prediction.classifyImage(os.path.join(exec_path, r'ReallySmartBrain/giraffe.jpg'), result_count=5) 
# predctions, probabilities = prediction.classifyImage(os.path.join(exec_path, r'ReallySmartBrain/godzilla.jpg'), result_count=5) 
predctions, probabilities = prediction.classifyImage(os.path.join(exec_path, r'ReallySmartBrain/godzilla.jpg'), result_count=5) 
# result_count=5 means top 5 predictions (how many predictions we want the model to give us)
# Print the predictions and their probabilities (the conifidence you have on these predictions)
# The predictions are now a list of tuples (label, probability)
# The probabilities are now a list of floats, probabilities
# The predictions are now a list of labels
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')



# -------------
# Old Version:
# from imageai.Prediction import ImagePrediction
# import os
# execution_path=os.getcwd()

# prediction = ImagePrediction()
# prediction.setModelTypeAsSqueezeNet()
# prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
# prediction.loadModel()

# predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
# for eachPrediction, eachProbability in zip(predictions, probabilities):
#     print(eachPrediction , " : " , eachProbability)