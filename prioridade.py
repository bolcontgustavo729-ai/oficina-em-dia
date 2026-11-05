import argparse


def classificar(horas):
    return "alta" if horas >= 24 else "normal"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("horas", type=int)
    args = parser.parse_args()
    if args.horas < 0:
        parser.error("informe um número de horas maior ou igual a zero")
    print(classificar(args.horas))
