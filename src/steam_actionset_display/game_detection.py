import psutil

GAME_EXES = ["darksouls.exe", "darksoulsremastered.exe"]


class GameRunningCheck:
    def __init__(self):
        self.process = None

    def is_game_running(self):
        # If we already have the process check if it is running
        if self.process:
            is_running = self.process.is_running()
            if is_running:
                return True
            else:
                self.process = None
                return False

        # If we don't have the process attempt to reacquire
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info['name'].lower() in GAME_EXES:
                self.process = proc
                return True

        return False


def main():
    import time
    check = GameRunningCheck()

    for i in range(100):
        print(check.is_game_running())
        time.sleep(2)


if __name__ == "__main__":
    main()
