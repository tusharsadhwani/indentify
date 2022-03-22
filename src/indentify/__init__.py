"""Indentify - Format any code-like snippet in an indented style."""
import sys


def indentify(source: str, indent_width: int = 2) -> str:
    """Formats a code-like snippet in an indented style."""
    # TODO: handle string parsing, and ignore escaped quotes inside it

    indent_markers = "([{"
    dedent_markers = ")]}"
    trailing_symbols = ",;"
    separators = ","

    indent = " " * indent_width

    indent_level = 0

    lines: list[str] = []
    next_line_chars: list[str] = []

    index = 0
    while index < len(source):
        char = source[index]
        index += 1

        if char in " \t\n\r":
            continue

        if char in separators:
            next_line_chars.append(char)
            line = indent * indent_level + "".join(next_line_chars)
            lines.append(line)
            next_line_chars = []

        elif char in indent_markers:
            next_line_chars.append(char)
            line = indent * indent_level + "".join(next_line_chars)
            lines.append(line)
            next_line_chars = []
            indent_level += 1

        elif char in dedent_markers:
            if next_line_chars:
                line = indent * indent_level + "".join(next_line_chars)
                lines.append(line)
                next_line_chars = []

            indent_level -= 1

            next_line_chars.append(char)
            while (char := source[index]) in trailing_symbols:
                next_line_chars.append(char)
                index += 1
                if index == len(source):
                    break

            line = indent * indent_level + "".join(next_line_chars)
            lines.append(line)
            next_line_chars = []
        else:
            next_line_chars.append(char)

    return "\n".join(lines)


def cli() -> None:
    """Indentify CLI interface."""
    # TODO: make it a CLI
    # TODO: sys.argv support
    # TODO: allow changing indent level
    print(indentify(sys.stdin.read()))
