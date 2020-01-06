from pyglet.event import EventDispatcher


class Emitter(EventDispatcher):
    def start(self):
        self.dispatch_event("on_event_1")
        self.dispatch_event("on_event_2", "hello")


Emitter.register_event_type("on_event_1")
Emitter.register_event_type("on_event_2")
