afe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError, TypeError):
        return(False)
