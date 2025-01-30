# src/train_lstm.py
import pandas as pd
import torch
import torch.nn as nn
import pytorch_lightning as pl
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from config.settings import PROCESSED_DATA_DIR


class WildfireLSTM(pl.LightningModule):
    def __init__(self, input_size=7, hidden_size=64):  # Adjusted for lag features
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 2)  # Output 2 classes (fire risk high/low)
        self.loss_fn = nn.CrossEntropyLoss()  # Suitable for multi-class classification

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])  # Take only last time step output

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(
            y_hat, y.long()
        )  # Convert y to LongTensor for classification
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)


def train_lstm():
    # Load data
    df = pd.read_csv(f"{PROCESSED_DATA_DIR}/merged_dataset.csv")

    df["month"] = pd.to_datetime(df["date"]).dt.month

    # Print columns to verify presence
    print("Columns in merged dataset:", df.columns)

    # Select features (including lag features)
    feature_cols = [
        "temp",
        "humidity",
        "windspeed",
        "month",
        "frp_lag_1",
        "frp_lag_2",
        "frp_lag_3",
    ]
    features = df[feature_cols].values

    # Target: Convert FRP to binary classification
    target = (df["frp"] > 0.5).astype(int).values  # Assuming normalized FRP

    # Split into train & test sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    # Convert to PyTorch tensors
    train_dataset = TensorDataset(
        torch.FloatTensor(X_train).unsqueeze(1), torch.LongTensor(y_train)
    )
    test_dataset = TensorDataset(
        torch.FloatTensor(X_test).unsqueeze(1), torch.LongTensor(y_test)
    )

    # Train model
    model = WildfireLSTM(input_size=len(feature_cols))
    trainer = pl.Trainer(max_epochs=20)  # Increased epochs for better training
    trainer.fit(model, DataLoader(train_dataset, batch_size=32, shuffle=True))

    # Save model
    torch.save(model.state_dict(), "models/lstm_model.pt")


if __name__ == "__main__":
    train_lstm()
