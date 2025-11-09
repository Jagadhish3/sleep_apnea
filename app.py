from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load your model
model = tf.keras.models.load_model("model/sleep_apnea_model_streaming.h5")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "No file key in request. Please upload an image."

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    import io
    from tensorflow.keras.preprocessing import image
    import numpy as np

    # Convert uploaded file → bytes
    img_bytes = io.BytesIO(file.read())

    img = image.load_img(img_bytes, target_size=(64,64), color_mode="grayscale")
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0

    prediction = model.predict(img)[0][0]

    result = "Sleep Apnea Detected" if prediction > 0.5 else "Normal Breathing"

    return render_template("result.html", prediction=result)


    result = "Sleep Apnea Detected" if prediction > 0.5 else "Normal Breathing"

    return render_template("result.html", prediction=result)




if __name__ == "__main__":
    app.run(debug=True)
