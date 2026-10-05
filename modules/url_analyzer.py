from urllib.parse import urlparse


def analyze_url(url):

    result = {
        "url": url,
        "https": False,
        "long_url": False,
        "suspicious_symbols": False,
        "suspicious_words": False,
        "risk_score": 0,
        "risk_level": "Low"
    }

    # HTTPS check
    if url.startswith("https://"):
        result["https"] = True
    else:
        result["risk_score"] += 20

    # Parse URL
    parsed = urlparse(url)

    # URL length check
    if len(url) > 100:
        result["long_url"] = True
        result["risk_score"] += 20

    # Suspicious symbols check
    suspicious_symbols = ["@", "%"]

    if any(symbol in url for symbol in suspicious_symbols):
        result["suspicious_symbols"] = True
        result["risk_score"] += 20

    # Suspicious words check
    suspicious_words = [
        "login",
        "verify",
        "account",
        "password",
        "secure",
        "update",
        "bank"
    ]

    url_lower = url.lower()

    if any(word in url_lower for word in suspicious_words):
        result["suspicious_words"] = True
        result["risk_score"] += 20

    # Domain check
    if not parsed.netloc:
        result["risk_score"] += 20

    # Risk level
    if result["risk_score"] >= 60:
        result["risk_level"] = "High"

    elif result["risk_score"] >= 30:
        result["risk_level"] = "Medium"

    else:
        result["risk_level"] = "Low"

    return result