import time
from src.collector import collect_metrics
from src.feature_engineering import process_features
from src.health_engine import predict_health
from src.health_engine import display_output

print("🚀 Starting AI Health Monitor....\n")

current_output = {
    "score": None,
    "category": None
}

while True:
    try:
        metrics = collect_metrics()
        features = process_features(metrics)

        score, category = predict_health(features)

        # store latest output
        current_output["score"] = score
        current_output["category"] = category

        # display output
        display_output(score, category)

        time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user")
        break


        