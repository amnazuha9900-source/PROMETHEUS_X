
def calculate_confidence(anomaly_score, threshold):
    difference = abs(anomaly_score - threshold)

    confidence = min(difference * 100, 100)

    if anomaly_score > threshold:
        result = "Anomaly Detected"
    else:
        result = "Normal"

    return {
        "prediction": result,
        "confidence": round(confidence, 2)
    }


if __name__ == "__main__":
    result = calculate_confidence(0.8, 0.5)
    print(result)
