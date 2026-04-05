# 🏎️ F1 Race Result Simulator

## 📌 Project Description
This project is a machine learning simulator that predicts the final standings of a Formula 1 race based on historical data. By utilizing a Random Forest regression algorithm, the model analyzes driver performance, constructor (team) capabilities, circuit characteristics, and qualifying grid positions to simulate the final race outcomes.

Moving beyond simple statistical probabilities, this tool learns complex correlations between various racing factors to provide data-driven insights into motorsport strategy.

## ✨ Features
* **Historical Data Training**: Cleans and trains on modern F1 race data from the 2010 season onwards.
* **Result Simulation**: Predicts the final finishing position based on custom input conditions (e.g., specific driver, team, circuit, and starting grid).
* **Ready to Run**: The required dataset is already included in the repository, making it easy to clone and test immediately.

## 📊 Dataset
This project utilizes the **Ergast F1 Database**. For your convenience, the essential dataset files are **already included in this repository**:
* `results.csv`: Final race results and standings.
* `races.csv`: Historical Grand Prix schedules and circuit mappings.
* `qualifying.csv`: Qualifying session records and grid placements.

## 🛠️ Installation & Usage

### 1. Prerequisites
You need Python installed on your machine along with the `pandas` and `scikit-learn` libraries.
```bash
pip install pandas scikit-learn
