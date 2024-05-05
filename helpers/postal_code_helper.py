VALID_POSTAL_CODES = [8001, 8002, 8003, 8004, 8005, 8006, 8008, 8032, 8037, 8038, 8040, 8041, 8044, 8045, 8046, 8047, 8048, 8049, 8050, 8051, 8052, 8053, 8055, 8057, 8063, 8064, 8093, 8143, 8800]

def get_postal_code(args: list[str]):
    if len(args) != 1:
        return None
    elif args[0].isdigit() and int(args[0]) in VALID_POSTAL_CODES:
        return args[0]
    else:
        return None
