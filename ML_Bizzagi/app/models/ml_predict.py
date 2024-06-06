import torch
import numpy as np
import app.models.ml_config as cf

def predict_reviews(review_data, max_sequence_length):
    cf.model_ABSA.eval()  # Set model to evaluation mode

    for review_text in review_data:
        # Tokenize the review text
        encoded_input = cf.tokenizer(review_text, padding='max_length', truncation=True, max_length=max_sequence_length, return_tensors='pt')

        input_ids = encoded_input['input_ids']
        attention_mask = encoded_input['attention_mask']

        # Prediction
        with torch.no_grad():
            sentiment_pred, confidence_pred = cf.model_ABSA(input_ids, attention_mask)

        # Post-process prediction
        sentiment_pred = torch.sigmoid(sentiment_pred).cpu().numpy()
        confidence_pred = torch.sigmoid(confidence_pred).cpu().numpy()

        # Convert sentiment predictions to -1, 0, 1
        sentiment_pred = np.where(sentiment_pred > 0.66, 1, np.where(sentiment_pred < 0.33, -1, 0))

        # Convert confidence predictions to 0, 1
        confidence_pred = (confidence_pred > 0.5).astype(int)

        # Print prediction
        print("Review:", review_text)
        print("[Rasa, Pelayanan, Tempat, Harga]")
        print("Sentiment prediction:", sentiment_pred[0])
        print("Confidence prediction:", confidence_pred[0])
        print("")