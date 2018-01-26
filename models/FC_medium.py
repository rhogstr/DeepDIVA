
import torch.nn as nn


class FC_medium(nn.Module):

    def __init__(self, num_classes=10, **kwargs):
        """
        :param num_classes: the number of classes in the dataset
        """
        super(FC_medium, self).__init__()

        self.expected_input_size = (2)

        # First layer
        self.fc1 = nn.Sequential(
            nn.Linear(2, 1000),
            nn.Softsign(),
        )

        # Second layer
        self.fc2 = nn.Sequential(
            nn.Linear(1000, 1000),
            nn.Softsign(),
        )

        # Third layer
        self.fc3 = nn.Sequential(
            nn.Linear(1000, 100),
            nn.Softsign(),
        )

        # Classification layer
        self.cl = nn.Sequential(
            nn.Linear(100, num_classes)
        )

    def forward(self, x):
        """
        Computes forward pass on the network
        :param x: torch.Tensor
            The input to the model
        :return: torch.Tensor
            Activations of the fully connected layer
        """
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.cl(x)
        return x