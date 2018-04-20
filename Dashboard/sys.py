import psutil ,datetime , docker
class sys:
    client = docker.from_env()
    con_num = int(len(client.containers.list()))
    hostname = str(psutil.users()[0].name)
    nowtime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    cpu_num = psutil.cpu_count(logical=False)
    cpu_Lnum = psutil.cpu_count(logical=True)
    mem_persent = psutil.virtual_memory().percent
    mem_used = psutil.virtual_memory().used
    mem_free = psutil.virtual_memory().free
    mem_total = psutil.virtual_memory().total
    swap_used = psutil.swap_memory().used
    swap_total = psutil.swap_memory().total
    swap_free = psutil.swap_memory().free
    disk = psutil.disk_partitions()
    net_send = psutil.net_io_counters().bytes_sent
    net_recv = psutil.net_io_counters().bytes_recv
    ip = str(psutil.users()[0].host)
    def cpu_percent(self) :
        sum = 0
        for  persent in psutil.cpu_percent(interval=1,percpu=True) :
            sum += persent
        return round(sum / self.cpu_num,0)
    def disk_info(self):
        result = ""
        def optback(opt):
            if (opt == 'ro'):
                return ("Read-Only")
            elif (opt == 'rw'):
                return ("Read-Write")
            else:
                return ("Unknown")
        disk = psutil.disk_partitions()
        print("-----Device Information-----")
        for i in range(0, len(disk)):
              result += \
                  str(" Device:" + str(disk[i].device)+" Mount:" +
                  str(disk[i].mountpoint)+" Fstype:" +
                  str(disk[i].fstype)+" Opt: " +
                  str(optback(disk[i].opts))+ "\n")
        return result
    def uptime(self):
        Uptime = datetime.datetime.fromtimestamp(psutil.boot_time())
        Nowtime = datetime.datetime.now()
        return  int((Nowtime - Uptime).seconds/3600)


