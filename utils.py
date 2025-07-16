def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0
#To use in feature.py
