# Port Scanner 🔍

A lightweight Python utility for network port scanning and analysis.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-Unlicense-lightgrey)

## Features ✨
- IP/Domain target scanning
- Custom port range specification
- Basic port availability detection
- Simple CLI interface
- Fast single-threaded implementation

## Prerequisites ⚙️
- Python 3.6+
- Standard Python libraries:
  - `socket`
  - `argparse`
  - `sys`

## Installation 📦
```bash
git clone https://github.com/Abdallah-Sallem/Port_Scanner.git
cd Port_Scanner
```

## Usage 🚀
```bash
python3 port_scanner.py -t <target> -p <port-range>
```

### Options:
- `-t`, `--target`: Target IP or domain (required)
- `-p`, `--ports`: Port range (default: 1-1024)
- `-v`, `--verbose`: Show detailed output

## Example 📋
```bash
python3 port_scanner.py -t google.com -p 80-443
```

**Sample Output:**
```
Scanning google.com (142.250.179.142)
Port 80/tcp - OPEN
Port 443/tcp - OPEN
Scan completed in 2.18s
```

## Contributing 🤝
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄
This project is currently unlicensed. See [LICENSE](LICENSE) for future updates.

## Roadmap 🗺️
- [ ] Add multithreading support
- [ ] Implement service detection
- [ ] Add export formats (CSV/JSON)
- [ ] Create graphical interface

## Acknowledgments 🙏
Inspired by basic network security concepts and Python socket programming examples.