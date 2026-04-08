def compute_error(cpu, memory, temp):
    error = 0
    if cpu > 85:
        error += 1
    if memory > 85:
        error += 1
    if temp > 80:
        error += 1
    return error


def process_features(metrics):
    error = compute_error(
        metrics["cpu"],
        metrics["memory"],
        metrics["temperature"]
    )

    return [
        metrics["cpu"],
        metrics["memory"],
        metrics["temperature"],
        metrics["uptime"],
        metrics["upload"],
        metrics["download"],
        error
    ]