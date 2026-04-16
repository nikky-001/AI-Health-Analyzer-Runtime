# 🖥️ AI System Health Analyzer

A lightweight, deployment-ready AI system that performs real-time **health prediction**, **trend analysis**, and **alert generation** for system monitoring.

This project is designed for easy integration into systems such as PCs, routers, and embedded devices.

---

## 🚀 Features

* Real-time health score prediction using ONNX model
* Trend-based future prediction using recent history
* Intelligent alert system (popup-based, non-intrusive)
* Modular architecture for easy integration
* Works with Python and non-Python systems


### Health Categories:

* Above 90 → Healthy
* Above 65 → Good
* Above 40 → Degrading
* Below 40 → Critical

---

## 📦 Project Structure

```
ai-health-monitor/
│
├── model/
│   └── health_model.onnx
│
├── src/
│   ├── collector.py
│   ├── feature_engineering.py
│   ├── health_engine.py
|   ├── trend_analyzer.py
|   └── runtime_engine.py
│
├── docs/
│   ├── input_format.md
│   ├── feature_logic.md
│   └── integration_guide.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation (Python Systems)

Install dependencies:

pip install -r requirements.txt

---

## ▶️ Running the System

python main.py

---

## 🔧 Configuration

Update `src/collector.py` to fetch metrics from your system:

* CPU usage
* Memory usage
* Temperature
* Network data
* Uptime

---

## 🔌 Integration Overview

This project supports two types of integration:

### ✅ Python-Based Systems

* Run `main.py` for continuous monitoring
                   Or
* Directly use the prediction function from `runtime_engine.py`

### 🔥 Non-Python Systems (Router / Embedded)

* Use the ONNX model (`model/health_model.onnx`)
* Implement logic using documentation in `docs/`

---

## 📚 Documentation

Detailed integration and implementation steps are available in:

* docs/input_format.md
* docs/feature_logic.md
* docs/integration_guide.md

---

## 🖥️ Output Example

Health Score: 78
Status: Good

---

## 🤝 Use Cases

* System monitoring tools
* Router firmware integration
* IoT device health tracking
* Performance analysis systems

---

## 🚀 Future Enhancements

* Advanced time-series forecasting
* Enhanced anomaly detection
* Alert severity levels
* Extended UI integration

---

## 👨‍💻 Author

Developed as part of an AI-based system monitoring and prediction project.

