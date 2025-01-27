import torch
import torch.nn as nn
import pytorch_lightning as pl
from torch.utils.data import DataLoader, TensorDataset

class WildfireLSTM(pl.LightningModule):
    def __init__(self, input_size=5, hidden_size=64):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)
        self.loss_fn = nn.BCEWithLogitsLoss()

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

def train_lstm():
    # Load data
    df = pd.read_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv")
    features = df[["day_of_year", "temp", "humidity", "month"]].values
    target = df["frp"].apply(lambda x: 1 if x > 10 else 0).values  # Binary classification
    
    # Convert to tensors
    dataset = TensorDataset(
        torch.FloatTensor(features).unsqueeze(1),  # Add sequence dim
        torch.FloatTensor(target).unsqueeze(1)
    )
    
    # Train
    model = WildfireLSTM()
    trainer = pl.Trainer(max_epochs=10)
    trainer.fit(model, DataLoader(dataset, batch_size=32))
    
    # Save
    torch.save(model.state_dict(), "models/lstm_model.pt")