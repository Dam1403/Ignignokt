import argparse
import Executable
parser = argparse.ArgumentParser(description='Ignignokt')


args = parser.parse_args()


def main():

    PE = Executable.PortableExecutable("TestEXEs/putty.exe")
    print(PE)

if __name__ == "__main__":
    main()




