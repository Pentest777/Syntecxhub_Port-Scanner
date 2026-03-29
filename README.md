# 🌐 Project 1: Port Scanner

A fast and simple **multi-threaded TCP Port Scanner** built in Python that scans open ports on a target host.

---

## 🚀 Features

* 🌐 Scan any **IP Address or Domain**
* 🔍 Scan a **range of ports**
* ⚡ **Multi-threaded scanning** (faster performance)
* 📄 Logs open ports to `scan_results.txt`
* ⏱ Displays scan start and end time
* 🧵 Thread-safe output using locks
* ❌ Handles errors and timeouts

---

## 🛠️ Technologies Used

* Python 3
* `socket` (network communication)
* `threading` (concurrency)
* `datetime` (logging time)

---

## 📂 Project Structure

```id="3p1xqz"
port-scanner/
│
├── scanner.py            # Main script
├── scan_results.txt      # Output log file (generated after scan)
└── README.md
```

---

## 🔧 How It Works

1. User enters:

   * Target (IP / Domain)
   * Start Port
   * End Port

2. Program:

   * Creates multiple threads
   * Each thread scans a port using TCP connection

3. Output:

   * Displays OPEN / CLOSED ports
   * Saves open ports to file

---

## ▶️ How to Run

### 1. Run the script

```bash id="n2j1kq"
python scanner.py
```

### 2. Input Example

```id="v8k3zm"
Enter Target IP or Domain: scanme.nmap.org
Start Port: 1
End Port: 100
```

---

## 📌 Sample Output

```id="h1k8lm"
[+] Scanning Target: scanme.nmap.org
[+] Time Started: 2026-03-29 10:00:00
--------------------------------------------------
[OPEN] Port 22
[CLOSED] Port 23
[OPEN] Port 80
...
[+] Scanning Completed at: 2026-03-29 10:00:05
```

---

## ⚠️ Important Notes

* ⚠️ Use only on **authorized systems**
* Unauthorized scanning may be illegal
* This tool is for **educational purposes only**

---

## 💡 Future Improvements

* GUI version (Tkinter)
* Service name detection (e.g., HTTP, FTP)
* Faster scanning using async (asyncio)
* Export results to JSON / CSV
* Banner grabbing

---

## 👨‍💻 Author

**Abhishek Anand**
Cyber Security Enthusiast 🔐

---

## ⭐ GitHub Tips

* Add `.gitignore`:

```id="j8m2op"
scan_results.txt
```

---

## 📜 License

This project is for educational purposes.

---

🔥 *Built to learn Networking & Cyber Security basics*
