from deepface import DeepFace

# Paths to the images you want to compare
image_path1 = "data/thor.jpg"
image_path2 = "data/rdj.jpg"

# Use DeepFace.verify() to compare the images
result = DeepFace.verify(image_path1, image_path2)

# Print all the information in the result
for key, value in result.items():
    print(f"{key}: {value}")
