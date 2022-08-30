# -*- coding: UTF-8 -*-
__author__ = "Jhong,Dong-You"
import eel
from random import randint

if __name__ == '__main__':
    eel.init("web")

    # Exposing the random_python function to javascript
    @eel.expose
    def random_python():
        print("Random function running")
        return randint(1, 100)


    # Start the index.html file
    eel.start(
        "index.html",
        geometry={'size': (400, 200), 'position': (500, 500)},
        mode='chrome-app',
        port=8787
    )
