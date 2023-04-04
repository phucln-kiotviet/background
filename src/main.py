# import json
import os
import sys

# from ansibles import service
from consumer import channel


def main():
    print("[*] Consuming")
    print("[*] Waiting for message. To exit press CTR+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped manual")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
