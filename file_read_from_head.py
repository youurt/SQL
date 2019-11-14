def file_read_from_head(fname, nlines):
    """Shows the n lines of a file."""
    from itertools import islice
    with open(file) as f:
        for line in islice(f, nlines):
            print(line)
