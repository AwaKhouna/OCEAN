# Author: Moises Henrique Pereira

# Import ui functions
from ui.app.MainApplication import MainApplication


def main():
    interfaceType = 'static'
    application = MainApplication(interfaceType)
    application.run()


if __name__ == '__main__':
    main()
