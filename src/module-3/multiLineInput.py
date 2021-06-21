
lines = []
print("Enter multiple line input:\n")
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

print(text.upper())