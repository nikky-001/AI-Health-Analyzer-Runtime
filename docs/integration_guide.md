# Integration Guide for AI System Health Analyzer

This document explains how to integrate the health prediction model into different systems.

---

## 1. Overview

This system provides real-time health monitoring along with predictive alerts.

Output:

- Health Score (0–100)
- Category:
  - Above 90 → Healthy
  - Above 65 → Good
  - Above 40 → Degrading
  - Below 40 → Critical
- Alerts (if system degrades)

---

## 2. Python-Based Systems

### Steps:

1. Install dependencies:
   pip install -r requirements.txt

2. Modify metric collection:
   Update `collector.py` to fetch system-specific data.

3. Run system:
   python main.py

### Integration Option:

Instead of running main.py, directly call:

from src.runtime_engine import get_system_health

data = get_system_health()

Output format:

{
  "score": 78,
  "category": "Good",
  "alert": None
}

---

## 3. Non-Python Systems (Router / Embedded Systems)

### Requirements:

- ONNX Runtime (C/C++ or supported language)
- Ability to collect system metrics

### Steps:

1. Load ONNX model:
   health_model.onnx

2. Implement feature logic:
   Refer to feature_logic.md

3. Prepare input array:
   Follow input_format.md

4. Run inference:
   Pass input to ONNX model

5. Get output:
   Health Score
   Health category
   Alerts(if system degrades)

---

## 4. UI Integration

The model does not include UI.

The system should:

- Continuously compute health score
- Provide latest value to UI
- UI displays:
  Health Score + Category + Alert

---

## UI Behavior

* Health Score and Category should be displayed continuously
* Alert should appear as a temporary popup notification only when present

---

## 5. Execution Flow

1. Collect metrics from system
2. Apply feature engineering
3. Pass data to model
4. Get prediction (score + category)
5. Apply trend analysis
6. Generate alert (if required)
7. Send output to UI  

---

## 6. Notes

- No need to store all predictions (real-time use)
- Ensure correct feature order
- Ensure correct units
- Model should run continuously in background
- Alerts should not be repeatedly triggered for same condition