import psutil ,datetime , docker,threading,time
class sys:
# Docker Information
    client = docker.from_env()
    con = client.containers.list(all=True)
    con_num = len(client.containers.list(all=True))
    con_ver = client.version()['Components'][0]['Version']
    con_arch = client.version()['Components'][0]['Details']['Arch']
    con_os = client.version()['Components'][0]['Details']['Os']
    image = client.images
    con_run_num = client.info()['ContainersRunning']
    con_stop_num  = client.info()['ContainersStopped']
    con_pause_num = client.info()['ContainersPaused']
    # con_mirrors = client.info()['RegistryConfig']['IndexConfigs']['docker.io']['Mirrors'][0]
    swarm_stat =  client.info()['Swarm']['LocalNodeState']
    swarm_nodeid = client.info()['Swarm']['NodeID']
    swarm_addr = client.info()['Swarm']['NodeAddr']
    swarm_num = client.info()['Swarm']['Nodes']
    events = client.events(decode=True, until=datetime.datetime.now())
# Systen Information
    #hostname = str(psutil.users()[0].name)
    nowtime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    cpu_num = psutil.cpu_count(logical=False)
    cpu_Lnum = psutil.cpu_count(logical=True)
    mem_persent = psutil.virtual_memory().percent
    mem_used = psutil.virtual_memory().used/1024/1024
    mem_free = psutil.virtual_memory().free/1024/1024
    mem_total = psutil.virtual_memory().total/1024/1024
    swap_used = psutil.swap_memory().used/1024/1024
    swap_total = psutil.swap_memory().total/1024/1024
    swap_free = psutil.swap_memory().free/1024/1024
    disk = psutil.disk_partitions()
    net_send = psutil.net_io_counters().bytes_sent
    net_recv = psutil.net_io_counters().bytes_recv
    #ip = str(psutil.users()[0].host)
    def cpu_percent(self) :
        sum = 0
        for  persent in psutil.cpu_percent(interval=1,percpu=True) :
            sum += persent
        return int( sum / self.cpu_num )
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
        return  int(round((Nowtime - Uptime).seconds/3600))

class sys_swarm:
    client = docker.from_env()
    con = client.containers.list(all=True)
    info = client.info()['Swarm']
    NodeID = info['NodeID']
    NodeAddr = info['NodeAddr']
    LocalNodeState = info['LocalNodeState']
    ControlAvailable = info['ControlAvailable']
    RemoteManagers = info['RemoteManagers']
    Remote_NodeID = RemoteManagers[0]['NodeID']
    Remote_Addr  = RemoteManagers[0]['Addr']
    Nodes = info['Nodes']
    Managers = info['Managers']
    Cluster_info = info['Cluster']
    Cluster_ID = Cluster_info['ID']
    Version = client.swarm.version
    def update(self):
        self.client.swarm.update()
    def reload(self):
        self.client.swarm.reload()








