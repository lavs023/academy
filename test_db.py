def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed
    assert docker.version.startswith("17.")

def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled

def test_por22_listening(host):
    socket = host.socket("tcp://0.0.0.0:22")
    assert socket.is_listening

def test_port_80_listening(host):
     socket = host.socket("tcp://0.0.0.0:3306")
     assert socket.is_listening

def test_system_info(host):
    os_type=host.system_info.type
    distribution=host.system_info.distribution
    release=host.system_info.release
    assert os_type == "linux"
    assert distribution == "centos"
    assert release == "7"
