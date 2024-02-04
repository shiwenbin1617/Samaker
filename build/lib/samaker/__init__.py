from emoji import emojize
<<<<<<< HEAD
__version__ = "1.2.1"
=======
__version__ = "1.2.2"
>>>>>>> origin/main
__description__ = "Quickly Arrange,Quickly Test!"
__image__ = emojize(fr"""{__description__}:rocket::rocket::rocket:version:{__version__}""")

if __name__ == '__main__':
    print(__image__)