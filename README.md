# 🚀 Custom Hybrid VPN System

A custom-built, lightweight Hybrid VPN System combining the high performance of **Go** for network traffic handling, **PHP** for robust user authentication and backend panel API, and **JavaScript (Node.js)** for the client-side application. Data is seamlessly structured and transmitted between all layers using **JSON**.

---

## 🏗️ Architecture & Component Roles

[ JavaScript Client ] <=== JSON Data ===> [ PHP Auth API ]
||                                      ||
(UDP Tunnel)                            (Verify Token)
||                                      ||
v                                       v
[ Go VPN Server Daemon ] <========================//
*   **Go (Backend Daemon):** The core engine. It listens on a secure UDP port, intercepts networking traffic, validates user connection tokens via the PHP API, and handles encrypted routing.
*   **PHP (Control Panel & Database API):** Acts as the centralized gatekeeper. It processes authentication tokens, validates user account status (e.g., active subscriptions), and responds with configuration payloads.
*   **JavaScript (Client App):** The user interface gateway built with Node.js. It authenticates with the PHP API, receives the dynamically generated connection profile, and initializes the secure tunnel with the Go Server.
*   **JSON (Protocol Standard):** The universal data format used for seamless configuration and handshake exchanges across all environments.

---

## 🛠️ Getting Started

### 1. Prerequisites
Ensure you have the following installed on your target machine(s):
*   [Go](https://go.dev) (v1.18+)
*   [Node.js](https://nodejs.org) (v16+)
*   PHP Web Server environment (e.g., Apache, Nginx, or XAMPP)

---

## 🚀 Installation & Setup

### Step A: Deploy the PHP Authentication API
1. Move the `auth.php` file into your local web server root directory (e.g., `www/vpn_api/`).
2. Ensure your server is active. The default endpoint will be: 
   `http://localhost/vpn_api/auth.php`

### Step B: Fire Up the Go VPN Daemon
1. Navigate to the Go server directory.
2. Initialize and run the listener:
   ```bash
   go run main.go
   ```
3. The server will launch a dedicated UDP listener on port `51820`.

### Step C: Execute the Client Application
1. Open a separate terminal window and move to the JavaScript client directory.
2. Boot up the Node client to establish a tunnel handshake:
   ```bash
   node client.js
   ```

---

## 🔒 Security Disclaimer
This project is designed as an architectural proof-of-concept (PoC) to demonstrate how low-level system languages can interact with high-level web APIs to form networking pipelines. For enterprise production deployments, integrate robust cryptographic handshake suites (such as **WireGuard** or **AES-GCM-256**) alongside secure DB querying.

---

## 📝 License
This project is open-source and licensed under the [MIT License](LICENSE).
