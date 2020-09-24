class areaCodeParser:
    @staticmethod
    def Parse(args):
        validAreaCodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L-OST", "L-WEST"]
        
        if len(args) < 1:
            return None
        elif args[0].upper() == "L-WEST":
            return "L WEST"
        elif args[0].upper() == "L-OST":
            return "L OST"
        elif args[0].upper() in validAreaCodes:
            return args[0].upper()
        else:
            return None