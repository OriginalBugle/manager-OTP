import rich
from rich.console import Console
import datetime
import argparse
import pyotp
import time
import math
import sys
import os


console = Console()
# Exemple de TOTP
totp = pyotp.TOTP('base32secret3232')


otp_list = [['Exemple',pyotp.TOTP('VWB6TMY6OWFJXIE2A2JT3ZICTG3QW7MH')],['ETE',pyotp.TOTP('E4NN7L5DI25LOIHYLJRXUHQ2EDQ4NQD4')],['Jacque',pyotp.TOTP('7GGNG6Q2RQIMCOQCLGN4IQ24RML25FWK')]]


def OTPlist():
    os.system('cls')
    console.rule("[bold red]Code OTP")
    for i in range(len(otp_list)):
        tempory_value = otp_list[i]
        console.print(f"{tempory_value[0]}: {tempory_value[1].now()}")


OTPlist()
try:
    while True:
        time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
        time_remaining_int = int(math.trunc(time_remaining))
        sys.stdout.write(f"\r{(30-time_remaining_int)*"[]"} {(30-(30-time_remaining_int))*"  "} {time_remaining_int} seconde{"" if time_remaining_int == 0 or time_remaining_int == 1 else "s"} ")
        # {"" if time_remaining_int == 0 or time_remaining_int == 1 else "s"}
        if 0.0 <= time_remaining <= 0.1:
            OTPlist()
except KeyboardInterrupt:
    pass