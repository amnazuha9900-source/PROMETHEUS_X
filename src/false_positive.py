
def manage_false_positive(
    anomaly_score,
    threshold,
    confidence
):
    if anomaly_score <= threshold:
        status = "Normal"
        alert = False

    elif confidence < 50:
        status = "Needs Manual Inspection"
        alert = False

    else:
        status = "Defect Detected"
        alert = True

    return {
        "status": status,
        "alert": alert
    }


if __name__ == "__main__":
    result = manage_false_positive(
        0.8, 0.5, 75
    )
    print(result)
