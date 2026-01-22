# Software — Lecture Notes

## Definition
- **Software:** A set of instructions, data, and documentation that tells computer hardware how to perform tasks. Software enables computation, automation, user interaction, and data processing.

## Broad Categories of Software
- **System Software:** Manages hardware and provides core services.
	- Examples: operating systems (Windows, macOS, Linux), device drivers, system utilities.
- **Application Software:** Programs designed for end-users to perform specific tasks.
	- Examples: web browsers, office suites, media players, database clients, mobile apps.
- **Programming Software (Developer Tools):** Tools that developers use to build, test, and maintain software.
	- Examples: compilers, interpreters, linkers, IDEs, debuggers, build systems.
- **Middleware:** Software that connects different applications or services and abstracts communication.
	- Examples: message brokers, application servers, API gateways.
- **Embedded Software / Firmware:** Software written for specialized hardware with constrained resources.
	- Examples: microcontroller firmware, IoT device software, router OS.
- **Libraries & Frameworks:** Reusable components and scaffolding used by application developers.
	- Examples: React, NumPy, TensorFlow, standard libraries.

## Distribution & Licensing Models
- **Proprietary:** Closed-source, licensed for use under terms (e.g., Microsoft Office).
- **Open-source:** Source code is publicly available and reusable under an OSS license (e.g., Apache, MIT, GPL).
- **Delivery models:** On-premise, packaged installs, cloud-hosted, and Software-as-a-Service (SaaS).

## How Software Is Organized
- **Monolithic vs Microservices:** Single large application vs multiple small services communicating over networks.
- **Client–Server:** Clients request services from servers (e.g., web apps: browser client + backend server).
- **Event-driven / Reactive:** Components react to events/messages (common in UI and distributed systems).

## Quality & Maintenance Concerns
- **Versioning:** Semantic versioning (MAJOR.MINOR.PATCH) for releases.
- **Testing:** Unit, integration, system, and acceptance testing to ensure correctness.
- **Security:** Patching, dependency management, secure coding practices, and access control.
- **Documentation:** User docs, API docs, and inline comments.

## Examples & Short Code Blocks
- Example: a minimal Python function (application-level code)
```python
def greet(name: str) -> str:
		return f"Hello, {name}!"

print(greet("World"))
```
- Example: check OS info on Unix-like systems (system-level interaction)
```bash
uname -a
lsb_release -a   # on some Linux distros
```

## Best Practices (high-level)
- Keep concerns separated: UI, business logic, and data access should be modular.
- Use version control (e.g., Git) from day one.
- Automate builds and tests (CI/CD) to catch regressions early.
- Apply security reviews and dependency scanning regularly.
- Prefer small, well-documented releases and maintain a changelog.

## Quick Study Tips
- Map real software you use to categories above (e.g., browser = application software).
- Inspect a simple open-source project to see how code, docs, and tests are organized.
- Try building a tiny embedded program (e.g., Arduino blink) to understand firmware constraints.

## Examples of Software (Detailed)
- **System software:**
	- Windows 10/11, macOS Monterey/Ventura, Ubuntu Linux, Android, iOS
	- Device drivers (GPU drivers from NVIDIA/AMD), system utilities (disk managers)
- **Application software:**
	- Web browsers: Google Chrome, Mozilla Firefox, Safari
	- Productivity: Microsoft Office, LibreOffice, Google Docs (SaaS)
	- Media & graphics: VLC, Adobe Photoshop, GIMP
	- Databases/clients: MySQL Workbench, pgAdmin, Microsoft SQL Server Management Studio
- **Programming & developer tools:**
	- Languages/runtimes: Python, Java, Node.js
	- Compilers/SDKs: GCC, Clang, JDK
	- IDEs/editors: Visual Studio Code, IntelliJ IDEA, PyCharm
	- Version control: Git (with GitHub/GitLab/Bitbucket integrations)
- **Middleware / backend components:**
	- Web servers: Nginx, Apache HTTP Server
	- Application servers: Apache Tomcat, WildFly
	- Message brokers: RabbitMQ, Apache Kafka
- **Embedded software / firmware:**
	- Arduino sketches, ESP32 firmware, Raspberry Pi OS images
	- Automotive ECU firmware, router firmware (OpenWrt)
- **Libraries & frameworks:**
	- Frontend: React, Angular, Vue.js
	- Backend: Django, Flask, Express
	- Data & ML: NumPy, Pandas, TensorFlow, PyTorch
- **Cloud & SaaS examples:**
	- Google Workspace, Salesforce, AWS Lambda (serverless), Dropbox, Slack

### Quick install / usage snippets
Install a Python library (library example):
```bash
pip install numpy pandas
```
Start a simple Nginx container (middleware example):
```bash
docker run --rm -p 8080:80 nginx
```


---

Prepared as concise lecture notes covering definition and types of software.

