# Protocol — Lecture Notes

## Definition
- **Protocol:** A set of rules and conventions that define how two or more entities communicate and exchange information. In computing and networking, protocols specify message formats, timing, error handling, and procedures for connection setup and teardown.

## Why protocols matter
- Ensure interoperability between different systems and vendors.
- Provide reliability, ordering, and error detection where required.
- Define security, authentication, and access control behaviors.

## Layers & Models
- **OSI model (7 layers):** Physical, Data Link, Network, Transport, Session, Presentation, Application — conceptual for understanding.
- **TCP/IP model (4 layers):** Link, Internet, Transport, Application — practical Internet model.
- Protocols operate at different layers (e.g., Ethernet at link layer, IP at network layer, TCP/UDP at transport, HTTP at application layer).

## Common Protocol Types & Examples
- **Network / Internet protocols:** IP, ICMP, ARP
- **Transport protocols:** TCP (connection-oriented, reliable), UDP (connectionless, low-latency)
- **Application protocols:** HTTP/HTTPS, FTP, SMTP, POP3, IMAP, DNS, SSH, Telnet
- **Security protocols:** TLS/SSL, IPSec
- **Routing protocols:** OSPF, BGP, RIP

## Connection Types
- **Connection-oriented (e.g., TCP):** Establishes a session (handshake), ensures ordered delivery, performs retransmission on packet loss.
- **Connectionless (e.g., UDP):** Sends independent packets without a handshake; lower overhead, suitable for streaming or DNS.

## Protocol Mechanics (Key Concepts)
- **Handshake:** Procedure to establish parameters (e.g., TCP three-way handshake: SYN → SYN-ACK → ACK).
- **Headers & Payloads:** Protocol messages usually contain headers (metadata) and payload (data).
- **Ports & Sockets:** Ports identify services on a host (e.g., HTTP uses port 80, HTTPS 443). A socket pairs IP + port.
- **Stateful vs Stateless:** Stateful protocols maintain session state (e.g., TCP), stateless protocols treat each request independently (e.g., HTTP without cookies/session storage).

## Example Commands & Code
- Use `curl` to interact with HTTP:
```bash
curl -i https://example.com
```
- Check open TCP port with `nc` (netcat):
```bash
nc -vz example.com 443
```
- Simple TCP client in Python:
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
sock.sendall(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
print(sock.recv(4096).decode())
sock.close()
```

## Security Considerations
- Prefer encrypted protocols (HTTPS/TLS) for confidentiality and integrity.
- Use authentication and authorization to limit access.
- Be aware of protocol-specific attacks (e.g., TCP SYN flood, DNS spoofing, SSL/TLS misconfiguration).

## Design & Best Practices
- Choose the right transport: TCP for reliability, UDP for low-latency/real-time.
- Keep protocol messages minimal and well-documented.
- Version protocols to allow safe evolution and backward compatibility.
- Validate and sanitize all incoming data to avoid injection or buffer-overflow vulnerabilities.

## Troubleshooting Tips
- Use packet capture (Wireshark, tcpdump) to inspect protocol exchanges.
- Check logs on both client and server; use verbose tools (`curl -v`, `ssh -v`).
- Verify DNS resolution, routing, and firewall/ACL rules when connectivity fails.

## Short Glossary
- **Handshake:** Setup sequence to start a session.
- **Throughput:** Data transfer rate achieved.
- **Latency:** Delay between sending and receiving data.
- **Retransmission:** Resending lost packets (TCP).
- **Checksum:** Error-detection field in headers.

## Resources
- RFCs (Request for Comments) — official protocol specifications: https://www.rfc-editor.org/
- Wireshark tutorials for protocol analysis: https://www.wireshark.org/

---

Prepared as concise lecture notes on protocols for classroom or self-study.

