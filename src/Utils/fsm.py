class State(object):

    def __init__(self, handlers, behavior):
        self.handlers = handlers
        self.behavior = behavior

    def on(self, evt, *args, **kwargs):
        if evt in self.handlers:
            self.handlers[evt](*args, **kwargs)
        else:
            print(f'No handler for event {evt}')
            raise Exception(f'No handler for event {evt}')

    def do(self, gc, *args, **kwargs):
        self.behavior(gc, *args, **kwargs)


class Wait(State):
    def __init__(self, handlers, behavior):
        self.super().__init__(handlers, behavior)

    def on(self, evt, arg1, arg2):
        if evt == 'wait':
            return self

        return self.super().on(evt, arg1, arg2)

    def do(self, gc, arg1, arg2):
        self.super().do(gc, arg1, arg2)


class Wait(object):
    name = 'wait'

    def on(self, event, *args):
        print(self.name, event)

        if event == 'alert':
            return Alert()
        # elif event == 'wait':
        #     return self
        elif event == 'exit':
            return None

        return self

    def do(self, gc):
        print('wait', gc.idx)


# class Terminate(object):
#     name = 'terminate'
#
#     def on(self, event, *args):
#         print(self.name, event)
#         return self
#
#     def do(self, gc):
#         print('terminate', gc.idx)


class Alert(object):
    name = 'alert'

    def on(self, event, *args, **kwargs):
        print(self.name, event)

        if event == 'wait':
            return Wait()
        # elif event == 'alert':
        #     return self
        elif event == 'exit':
            return None

        return self.super().on(event, *args, **kwargs)

    def do(self, gc):
        print('alert', gc.idx)


class StateMachine(object):
    def __init__(self):
        self.curState = Wait()
        self.active = True

    def on(self, event):
        newState = self.curState.on(event)
        if newState is None:
            self.active = False

        self.curState = newState

    def do(self, gc):
        self.curState.do(gc)

    def isActive(self):
        return self.active


class GameContext(object):
    def __init__(self):
        self.events = ['wait', 'alert', 'alert', 'wait', 'exit']
        self.idx = 0

    def getEvent(self):
        result = self.events[self.idx]
        self.idx += 1
        return result


if __name__ == '__main__':
    sm = StateMachine()
    gc = GameContext()

    while sm.isActive():
        sm.do(gc)
        event = gc.getEvent()
        sm.on(event)


