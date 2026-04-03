# Smart-Contract-Anomaly-Detector

An AI-driven security model developed to detect anomalies and potential exploits in Smart Contract interactions on decentralized networks. By leveraging a RandomForestClassifier, this tool analyzes on-chain transaction patterns—such as gas usage and method call frequency—to classify transactions as either normal or suspicious (potential exploits like Reentrancy or DoS).

## Project Status: Testnet

This model is currently deployed and tested on the OpenGradient Testnet.

## How it Works

The model evaluates a Smart Contract transaction based on 4 core features to determine if it is normal or an anomaly:

1.  Gas_Used: The total gas consumed by the transaction.
2.  Gas_Price: The price of gas for the transaction.
3.  Method_Call_Frequency: The number of times the same method has been called within a recent block range.
4.  Value_Transferred: The amount of cryptocurrency transferred in the transaction.

The model generates a classification label:

* [0] = Normal Transaction (Low Risk).
* [1] = Anomaly/Suspicious (High Risk of Exploit).

## On-chain Validation (Proof of Execution)

Here is a screenshot showing the successful inference of the Smart Contract Anomaly Detector model on the OpenGradient Testnet.

<img width="1350" height="600" alt="image" src="https://github.com/user-attachments/assets/b2ca5269-3083-4994-a4b3-7b76169c4623" />
