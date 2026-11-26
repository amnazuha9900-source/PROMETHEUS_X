
import numpy as np

def estimate_severity(defect_mask):
    total_pixels = defect_mask.size

    defect_pixels = np.count_nonzero(
        defect_mask
    )

    severity_percentage = (
        defect_pixels / total_pixels
    ) * 100

    if severity_percentage < 2:
        severity = "Low"
    elif severity_percentage < 10:
        severity = "Medium"
    else:
        severity = "High"

    return {
        "severity": severity,
        "defect_percentage": round(
            severity_percentage, 2
        )
    }
