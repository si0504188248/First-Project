import docker

try:
    client = docker.from_env()

    container = client.containers.run(
        "busybox",
        "sleep 1000",
        detach=True
    )

    try:
        result = container.exec_run("hostname")

        if result.exit_code != 0:
            print("Error: failed to execute command inside container")
        else:
            print("Container ID:", container.id)
            print("Hostname:", result.output.decode().strip())

    except Exception as e:
        print("Error while executing command inside container:", str(e))

except Exception as e:
    print("Docker error:", str(e))
