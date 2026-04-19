import docker

client = docker.from_env()
container = client.containers.run(
    "busybox",
    "sleep 1000",
    detach=True
)

result = container.exec_run("hostname")
print("Container ID:", container.id)
print("Hostname:", result.output.decode())
