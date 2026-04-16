# Feature Engineering Logic

This document explains how raw system metrics are transformed into model-ready inputs.

---

## 1. Upload & Download Speed Calculation

Upload and download speeds are calculated using byte differences over time.

Formula:

Upload Speed = (Current Bytes Sent - Previous Bytes Sent) / Time Difference
Download Speed = (Current Bytes Received - Previous Bytes Received) / Time Difference

---

## 2. Error Count Logic

Error count is derived based on system stress conditions.

Example Logic:

* CPU > 80% → +1 error
* Memory > 90% → +1 error
* Temperature > 85°C → +1 error

Total error count is the sum of triggered conditions.

---

## 3. Default Handling

If certain metrics are unavailable:

* Temperature → Use default value (e.g., 60°C)
* Uptime → Use system uptime or fallback value
* Network → Set to 0 if unavailable

---

## 4. Data Consistency

* Ensure all values are in correct units
* Ensure consistent time intervals for speed calculation
* Avoid sudden unrealistic spikes

---

## 5. Trend Analysis Logic

To enable predictive monitoring, the system maintains a short history of recent health scores.

Steps:

1. Store last N health scores (e.g., last 10–20 values)
2. Calculate trend using slope of values over time

Example:

Slope = rate of change of health score

* Negative slope → health decreasing
* Positive slope → health improving

Future prediction:

Predicted Score = Current Score + (Slope × Future Steps)

---

## 6. Alert Generation Logic

Alerts are generated based on trend and predicted future condition.

Example Conditions:

* If slope < -2 → Trigger warning alert
* If predicted score < 40 → Trigger critical alert

Example Alerts:

* ⚠️ "Health dropping rapidly"
* 🚨 "System may become CRITICAL soon"

---

## 7. Important Notes

* Maintain a rolling history (fixed size) to avoid memory issues
* Avoid repeated alerts for the same condition
* Alerts should be triggered only when condition changes
* Trend and alert logic must run continuously with incoming data

---

## 8. Implementation Note

This logic must be implemented in the target system (C/C++ or other language) if Python is not supported.
