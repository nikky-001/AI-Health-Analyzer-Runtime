import psutil
import time

prev_sent = psutil.net_io_counters().bytes_sent
prev_recv = psutil.net_io_counters().bytes_recv
prev_time = time.time()

def collect_metrics():
    global prev_sent, prev_recv, prev_time

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    uptime = time.time() - psutil.boot_time()

    net = psutil.net_io_counters()
    current_time = time.time()

    time_diff = current_time - prev_time

    upload = (net.bytes_sent - prev_sent) / time_diff
    download = (net.bytes_recv - prev_recv) / time_diff

    # update previous values
    prev_sent = net.bytes_sent
    prev_recv = net.bytes_recv
    prev_time = current_time

    # Dummy temperature
    temperature = 60

    return {
        "cpu": cpu,
        "memory": memory,
        "temperature": temperature,
        "uptime": uptime,
        "upload": upload,
        "download": download
    }