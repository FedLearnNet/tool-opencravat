from pyfedappwrap.engine.runtime import FedDBEngine

from app import OpenCravatApp

engine = FedDBEngine(test_mode=True)
engine.register(OpenCravatApp())

if __name__ == '__main__':
    engine.start()
    engine.wait_until_stop()
