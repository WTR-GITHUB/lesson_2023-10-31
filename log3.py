import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

def check_engine(all_systems: str = "ok"):
    if all_systems == "ok":
        logging.info(f"Angine sistems is: {all_systems} ")
    else:
        logging.warning(f"Angine sistems is: Not ok")
    return all_systems

def start_car(egnite: str) -> bool:
    if egnite == "ok":
        logging.info("Engine started!")
        return True
    else:
        logging.info("Engine not started!")
        return False

def drive():
    check = input("Is the engine is ok? (posible answers 'ok' / 'no'): ")
    if start_car(check_engine(check)):
        print("Wroomm")
    else:
        print("Chir chir chir chir")

drive()


