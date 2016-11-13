import genRdep
import genSdep
from multiprocessing import Process

if __name__ == "__main__":
    rDepThread = Process(target= genRdep.gen, args=())
    sDepThread = Process(target= genSdep.gen, args=())

    rDepThread.start()
    sDepThread.start()