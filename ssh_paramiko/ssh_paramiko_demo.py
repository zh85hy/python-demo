import time
import paramiko

HOSTNAME = "192.168.3.56"
PORT = 22
USERNAME = "pi"
PASSWORD = "raspberry1"


def ssh_connect(ssh_client, hostname=HOSTNAME, port=PORT, username=USERNAME, password=PASSWORD):
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port, username, password)


def ssh_disconnect(ssh_client):
    ssh_client.close()


def send_then_receive_until_words(channel, command, words):
    channel.send(command + "\n")
    while True:
        if channel.recv_ready():
            break
        else:
            time.sleep(0.01)
    data_reader = channel.makefile()
    # date_reader = channel.makefile('rb')  # If not working on Windows, try this.
    # bytes_words = words.encode('GBK')
    while True:
        print("Start to read line.")
        line = data_reader.readline()
        print(line)
        if words in line:
            print("Expected words show up: ", words)
            break
        else:
            print("Go to read next line.")
            continue
    print("It is time to return.")
    return True


if __name__ == "__main__":
    ssh = paramiko.SSHClient()
    ssh_connect(ssh)
    print("SSH connect successfully.")
    time.sleep(5)
    chan = ssh.invoke_shell()
    send_then_receive_until_words(chan, "passwd", "（当前）UNIX 密码：")
    send_then_receive_until_words(chan, "raspberry1", "输入新的 UNIX 密码：")
    send_then_receive_until_words(chan, "raspberry001", "重新输入新的 UNIX 密码：")
    send_then_receive_until_words(chan, "raspberry001", "passwd：已成功更新密码")
    print("Password changed.")
    ssh_disconnect(ssh)
    print("SSH disconnect successfully.")
    time.sleep(10)
    print("Done.")
