from colorlog import ColoredFormatter, default_log_colors

default_log_colors.update({"DEBUG": "cyan"})


class ColoredFormatter(ColoredFormatter):
    log_colors = default_log_colors
