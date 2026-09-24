def judge(question, expects, answer, results):
    if not expects:
        return False
    return expects.strip().lower() in (answer or "".lower)