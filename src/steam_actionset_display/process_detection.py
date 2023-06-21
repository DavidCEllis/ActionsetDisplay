import psutil
import win32process, win32gui


class ProcessRunningCheck:
    def __init__(self, exe_list: list[str]):
        """
        Tool to check if an application is running

        :param exe_list: list of executable names
        """
        self.exe_list = exe_list
        self.process: psutil.Process | None = None

    def __repr__(self):
        return f"{self.__class__.__name__}(game_exes={self.exe_list})"

    def is_running(self) -> bool:
        """
        Search for a process that matches any item in the .exe list

        If a match is found, store that process and return True otherwise
        return false.

        If a process has previously been found, just check if that is running
        return True if it is or False if it has stopped.

        If a process has been restarted in between checks this will return
        False the first time before returning True again to allow for
        resetting the configuration.
        """
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
            if proc.info['name'].lower() in self.exe_list:
                self.process = proc
                return True

        return False

    def has_focus(self):
        if not self.is_running():
            return False

        # Get focus window
        foreground_window = win32gui.GetForegroundWindow()
        foreground_pids = win32process.GetWindowThreadProcessId(foreground_window)

        return self.process.pid in foreground_pids



def main():
    import time
    check = ProcessRunningCheck(["darksouls.exe", "darksoulsremastered.exe"])

    for i in range(100):
        print(check.is_running())
        time.sleep(2)


if __name__ == "__main__":
    main()
