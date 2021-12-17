import torch
from torch import nn
from transformers import BertModel
from transformers import BertTokenizer


class BertBase(nn.Module):
    def __init__(self, n_class, type_model):
        super(BertBase, self).__init__()
        self.bert = BertModel.from_pretrained(type_model)
        self.do = nn.Dropout(0.5)
        self.linear = nn.Linear(self.bert.config.hidden_size, n_class)

    def forward(self, input_ids, attention_mask):
        _, cls_output = self.bert(
            input_ids=input_ids, attention_mask=attention_mask, return_dict=False
        )
        dropout = self.do(cls_output)
        output = self.linear(dropout)
        return output


# "dccuchile/bert-base-spanish-wwm-cased" 'Betoweight.pth'
# "bert-base-multilingual-cased" 'MBertweight.pth'
class BERT:
    def __init__(self, n_class, size, id_model, id_weight):
        self.device = "cpu"
        self.model = BertBase(n_class, id_model)
        self.model = self.model.to(self.device)
        self.tokenizer = BertTokenizer.from_pretrained(id_model)
        self.MAX_LEN = size
        self.loaded_weight = torch.load(id_weight, map_location=self.device)
        self.model.load_state_dict(self.loaded_weight)

    def sentiment_classification(self, review):
        encoding_review = self.tokenizer.encode_plus(
            review,
            max_length=self.MAX_LEN,
            truncation=True,
            add_special_tokens=True,
            return_token_type_ids=False,
            padding="max_length",
            return_attention_mask=True,
            return_tensors="pt",
        )

        input_ids = encoding_review["input_ids"].to(self.device)
        attention_mask = encoding_review["attention_mask"].to(self.device)
        output = self.model(input_ids, attention_mask)
        _, prediction = torch.max(output, dim=1)
        if prediction == 2:
            return "Sentimiento positivo"
        elif prediction == 1:
            return "Sentimiento neutro"
        elif prediction == 0:
            return "Sentimiento negativo"
