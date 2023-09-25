import os.path
import shutil
import sys


def check_reboot():
    """ Return True if the computer has a pending reboot"""
    return os.path.exists("run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn´t enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gygabites in the system
    gygabites_free = du.free / 2**30
    if percent_free < min_percent or gygabites_free < min_gb:
        return True
    return False


def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk ful.")
        sys.exit(1)

    print("Everything OK.")
    sys.exit(0)


main()

