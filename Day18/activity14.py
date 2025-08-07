log_lines = (f"Line {i}" if i != 99999 else "ERROR: Something failed" for i in range(10**6))
for i, line in enumerate(log_lines, start=1):
    if "ERROR" in line:
        print(f"LINE: {i} -> {line}")
        break

#
log_lines=(f"Line {i}" if i != 99999 else "ERROR: Something failed" for i in range(10**6))
error_line=next((f"LINE: {line_number} -> {line}" for line_number, line in enumerate(log_lines, start=1) if "ERROR" in line))
print(error_line)