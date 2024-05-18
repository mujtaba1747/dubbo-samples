from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

print(zk.get("/dubbo"))
print(zk.get("/dubbo/org.apache.dubbo.samples.api.GreetingService"))
print(zk.get_children("/dubbo"))
zk.stop()
