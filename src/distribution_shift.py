
import numpy as np

def detect_distribution_shift(
    reference_images,
    new_images,
    threshold=0.15
):
    reference_mean = np.mean(reference_images)
    new_mean = np.mean(new_images)

    shift_score = abs(
        reference_mean - new_mean
    )

    shifted = shift_score > threshold

    return {
        "shift_detected": bool(shifted),
        "shift_score": round(
            float(shift_score), 4
        ),
        "status": (
            "Distribution Shift Detected"
            if shifted else "Normal Distribution"
        )
    }
