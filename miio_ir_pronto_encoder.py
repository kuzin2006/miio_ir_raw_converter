# Utility to convert Pronto HEX IR code format to raw codes for use with
# Xiaomi/Mijia Universal IR Remote (chuangmi.remote.v2)
#
# This allows to avoid embedded learn IR code procedure,
# which fails to learn some remote controllers codes (i.e. Sony RM-U305)
#
# Developed by Eugene Kuzin, 2020

import base64
import heatshrink2
import miio


def pronto_convert(pronto):
    old_raw, freq = miio.ChuangmiIr.pronto_to_raw(pronto)
    signal = miio.chuangmi_ir.ChuangmiIrSignal.parse(base64.b64decode(old_raw))
    times = []
    for pair in signal.edge_pairs:
        times.append(signal.times_index[pair.pulse])
        times.append(signal.times_index[pair.gap])
    times = '{}\x00'.format(','.join(map(str, times)))
    return f"raw:{base64.b64encode(heatshrink2.encode(times.encode())).decode()}:{freq}"



