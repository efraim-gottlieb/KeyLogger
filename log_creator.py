from datetime import datetime

def create_log(text: dict) -> str:
    lines = []
    divider = "=" * 40
    line = '_' * 20

    for k, v in text.items():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"\n{divider}\n|| {k} ||\n({timestamp})\n{line}\nData:"
        lines.append(header)

        if isinstance(v, list):
            lines.append(" ".join(map(str, v)))
        else:
            lines.append(str(v))

    return "\n".join(lines) + "\n"
