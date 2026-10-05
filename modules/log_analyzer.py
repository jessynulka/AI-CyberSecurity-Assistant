def analyze_logs(log_text):

    lines = log_text.splitlines()

    result = {
        "total_logs": len(lines),
        "failed_logins": 0,
        "suspicious_ips": 0,
        "high_risk_events": 0,
        "risk_level": "Low"
    }

    for line in lines:

        line_lower = line.lower()

        if "failed login" in line_lower or "login failed" in line_lower:
            result["failed_logins"] += 1

        if "suspicious ip" in line_lower:
            result["suspicious_ips"] += 1

        if "critical" in line_lower or "high risk" in line_lower:
            result["high_risk_events"] += 1

    total_risk = (
        result["failed_logins"]
        + result["suspicious_ips"]
        + result["high_risk_events"]
    )

    if total_risk >= 5:
        result["risk_level"] = "High"
    elif total_risk >= 2:
        result["risk_level"] = "Medium"
    else:
        result["risk_level"] = "Low"

    return result