import torch.nn as nn
from transformers import AutoModel, AutoConfig

config = AutoConfig.from_pretrained("C:\\Users\\batur\\Bizzagi\\Bizzagi_Backend\\ML_Bizzagi\\app\models\\indobert_model")
model = AutoModel.from_pretrained("C:\\Users\\batur\\Bizzagi\\Bizzagi_Backend\\ML_Bizzagi\\app\\models\\indobert_model", config=config)

class BertForMultiTaskSequenceClassification(nn.Module):
    def __init__(self, model, hidden_size=1024, intermediate_size_1=128, intermediate_size_2=64, num_labels_sentiment=4, num_labels_confidence=4):
        super(BertForMultiTaskSequenceClassification, self).__init__()
        self.bert = model
        self.dropout = nn.Dropout(0.1)

        self.shared_layers = nn.Sequential(
            nn.Linear(config.hidden_size, intermediate_size_1),
            nn.ReLU(),
            nn.Linear(intermediate_size_1, intermediate_size_2),
            nn.ReLU()
        )

        self.sentiment_classifier = nn.Linear(intermediate_size_2, num_labels_sentiment)
        self.confidence_classifier = nn.Linear(intermediate_size_2, num_labels_confidence)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.last_hidden_state.mean(dim=1)
        pooled_output = self.dropout(pooled_output)

        shared_output = self.shared_layers(pooled_output)

        sentiment_logits = self.sentiment_classifier(shared_output)
        confidence_logits = self.confidence_classifier(shared_output)

        return sentiment_logits, confidence_logits