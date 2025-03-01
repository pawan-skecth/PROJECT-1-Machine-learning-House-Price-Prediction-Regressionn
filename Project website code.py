!pip install gradio
import gradio as gr
import pickle
import pandas as pd

# Load the model
with open('pipe.pkl', 'rb') as file:
    pipe = pickle.load(file)

# Updated function to predict house price
def predict_price(location, total_sqft, bath, bhk):
    try:
        # Strip leading/trailing whitespace and remove newline characters
        location = location.strip()

        # Create input data as a dictionary
        input_data = {
            'location': [location],
            'total_sqft': [float(total_sqft)],
            'bath': [float(bath)],
            'bhk': [int(bhk)]
        }

        # Convert dictionary to DataFrame
        input_df = pd.DataFrame(input_data)

        # Predict using the loaded pipeline
        prediction = pipe.predict(input_df)[0]
        return f"The predicted house price is ₹{prediction:,.2f}"
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.HTML("""
    <style>
        body { background-color: #6A1B9A; color: white; font-family: Arial, sans-serif; }
        .gradio-container { background-color: #6A1B9A; color: white; padding: 20px; border-radius: 15px; }
        h1 { text-align: center; color: white; margin-bottom: 30px; }
        label { color: white; font-weight: bold; }
    </style>
    """)

    gr.Markdown("<h1>House Price Prediction</h1>")
    with gr.Row():
        with gr.Column():
            location = gr.Textbox(label="Location", placeholder="e.g., 1st Block Jayanagar")
            total_sqft = gr.Textbox(label="Total Sqft", placeholder="e.g., 2850")
            bath = gr.Textbox(label="Number of Bathrooms", placeholder="e.g., 4")
            bhk = gr.Textbox(label="Number of BHKs", placeholder="e.g., 4")
            predict_button = gr.Button("Predict")

        with gr.Column():
            output = gr.Textbox(label="Prediction")

    # Set the button action
    predict_button.click(
        fn=predict_price,
        inputs=[location, total_sqft, bath, bhk],
        outputs=output
    )

# Launch the Gradio App
demo.launch()
