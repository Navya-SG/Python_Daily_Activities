log_lines = (f"Line {i}" if i != 99999 else "ERROR: Something failed" for i in range(10**6))
for i, line in enumerate(log_lines, start=1):
    if "ERROR" in line:
        print(f"LINE: {i} -> {line}")
        break
