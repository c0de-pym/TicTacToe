# Some of the code in your gameplay.py file, weren't really related
# to gameplay, so I moved them here
def framing(framed_text: str) -> str:
    # creating frame around text
    next_line = "\n"
    vertical_frame_left = "║ "
    vertical_frame_right = " ║"

    find_max_row = framed_text
    rows = find_max_row.split("\n")
    max_row = 0

    for row in rows:
        if len(row) > max_row:
            max_row = len(row)

    chart_lenght = (max_row + 2) * "="
    line_num = 0
    for row in rows:
        if len(row) < len(chart_lenght):
            rows[line_num] = row + " " * (len(chart_lenght) - len(row) - 2)
        line_num += 1
    framed_text = "\n".join(rows)
    output_frame = (
        "╔"
        + chart_lenght
        + "╗"
        + next_line
        + vertical_frame_left
        + framed_text.replace(
            next_line, vertical_frame_right + next_line + vertical_frame_left
        )
        + vertical_frame_right
        + next_line
        + "╚"
        + chart_lenght
        + "╝"
    )
    return output_frame
