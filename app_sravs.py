from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("butterfly_model_sravs.h5")

classes = sorted(os.listdir("static/uploads/sample"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        f = request.files["image"]
        filepath = os.path.join("static/uploads", f.filename)
        f.save(filepath)

        img = image.load_img(filepath, target_size=(180, 180))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_class = classes[np.argmax(prediction)]

        return render_template("index.html", prediction=predicted_class, image_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
