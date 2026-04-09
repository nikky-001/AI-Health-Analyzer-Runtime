import time
from src.collector import collect_metrics
from src.feature_engineering import process_features
from src.health_engine import predict_health, display_output

print("🚀 Starting AI Health Monitor...\n")

while True:
    try:
        # Step 1: Collect system metrics
        metrics = collect_metrics()

        # Step 2: Process features
        features = process_features(metrics)

        # Step 3: Predict health score & category
        score, category = predict_health(features)

        # Step 4: Display result
        display_output(score, category)

        # Run every 1 second
        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
        break

    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(1)