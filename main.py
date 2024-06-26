import argparse

from utils.PortParser import *
from Scanner.TcpConnect import *
from Scanner.TcpSyn import *
from Scanner.Ping import *
from Scanner.Udp import *
from Scanner.TcpFin import *


def main():
    parser = argparse.ArgumentParser(
        description="Xscan_python - A simple port scanner written in Python"
    )
    parser.add_argument("-t", "--target", help="Target Ip")

    parser.add_argument("-p", "--ports", nargs="+", type=str)
    parser.add_argument(
        "-s",
        "--scan",
        choices=["connect", "syn", "udp", "fin", "ping"],
        default="connect",
    )

    args = parser.parse_args()

    target_ip = args.target
    scan_type = args.scan

    if scan_type == "connect":
        ports = parse_ports(args.ports)
        tcp_connect_scan(target_ip, ports)
    elif scan_type == "syn":
        ports = parse_ports(args.ports)
        tcp_syn_scan(target_ip, ports)
    elif scan_type == "udp":
        ports = parse_ports(args.ports)
        udp_scan(target_ip, ports)
    elif scan_type == "fin":
        ports = parse_ports(args.ports)
        tcp_fin_scan(target_ip, ports)
    elif scan_type == "ping":
        ping(target_ip)


if __name__ == "__main__":
    main()
