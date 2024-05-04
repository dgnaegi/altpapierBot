VALID_POSTAL_CODES = [8004, 8032, 8041, 8047, 8051, 8057, 8143, 8001, 8005, 8037, 8052, 8063, 8044, 8002, 8006, 8038, 8045, 8049, 8053, 8064, 8003, 8008, 8040, 8046, 8050, 8055, 8093, 8048, 8800]

def get_postal_code(args):
    if len(args) != 1:
        return None
    elif args[0].isdigit() and int(args[0]) in VALID_POSTAL_CODES:
        return args[0]
    else:
        return None
