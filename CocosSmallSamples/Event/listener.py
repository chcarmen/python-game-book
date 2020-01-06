from cocos.layer import Layer

from emitter import Emitter


class Listener(Layer):
    def __init__(self):
        super().__init__()
        self.emitter = Emitter()

    def on_enter(self):
        self.emitter.push_handlers(self)
        self.emitter.start()

    def on_exit(self):
        self.emitter.remove_handlers(self)

    def on_event_1(self):
        print("received event 1")

    def on_event_2(self, str):
        print("received event 2", str)
