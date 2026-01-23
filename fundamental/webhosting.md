# Web Hosting — Lecture Notes

## Definition
- **Web hosting:** A service that provides storage space, compute resources, and network connectivity so websites, web applications, and online services are publicly accessible on the Internet.

## Core Components
- **Server:** Physical or virtual machine that stores files and runs server software (web server, application server).
- **Storage:** Persistent disk space (HDD/SSD) for site files, databases, and assets.
- **Bandwidth / Network:** Data transfer capacity between server and visitors.
- **DNS (Domain Name System):** Maps domain names to server IP addresses.
- **Control panel / Management:** Tools like cPanel, Plesk, or cloud consoles for managing hosting.

## Types of Web Hosting
- **Shared hosting:** Multiple customers share the same server and resources — low cost, limited control.
- **Virtual Private Server (VPS):** A physical server partitioned into virtual instances with dedicated resources and root access.
- **Dedicated server:** Entire physical server rented to a single customer — full control and high cost.
- **Cloud hosting:** Scalable virtual resources provided by cloud providers (AWS, GCP, Azure); pay-as-you-go and elasticity.
- **Managed hosting:** Provider handles maintenance, security, updates and backups — useful for teams wanting less ops work.
- **Colocation:** You place your own server hardware in a provider's datacenter; provider supplies power, cooling, and connectivity.

## Hosting Models & Use Cases
- **Static hosting:** Serves static files (HTML, CSS, JS) — simple and cost-effective (e.g., GitHub Pages, Netlify).
- **Dynamic hosting:** Runs server-side code and databases (e.g., Node.js, PHP, Python web apps).
- **Serverless / FaaS:** Run functions on demand (AWS Lambda, Azure Functions) without managing servers.
- **Platform-as-a-Service (PaaS):** Deploy apps without managing infrastructure (Heroku, Render).

## Hosting Stack (Typical)
- **Web server:** Nginx or Apache to serve HTTP(S) requests.
- **Application runtime:** Node, Python, PHP, Java, etc.
- **Database:** MySQL, PostgreSQL, MongoDB, or managed DB services.
- **Reverse proxy / load balancer:** Distribute traffic across multiple servers.
- **Cache layer:** Redis, Memcached, or CDN edge caching.
- **CDN (Content Delivery Network):** Cache static assets globally for speed (Cloudflare, Akamai).

## Common Operations & Commands
- Fetch a page with `curl`:
```bash
curl -I https://example.com
```
- Securely copy files to server:
```bash
scp site.zip user@server-ip:/var/www/
```
- Connect via SSH:
```bash
ssh user@server-ip
```

## Deploy & Release Patterns
- **FTP/SFTP:** Older method to upload files; use SFTP (SSH) for security.
- **Git-based deploys:** Push to a remote repo or provider trigger (e.g., deploy on push).
- **CI/CD pipelines:** Automated build, test, and deploy (GitHub Actions, GitLab CI, Jenkins).
- **Blue/green & rolling updates:** Reduce downtime during releases.

## Performance & Reliability Considerations
- Use a CDN for global delivery and lower latency.
- Enable caching (HTTP headers, reverse proxy) to reduce origin load.
- Monitor uptime and set up alerts (Prometheus, UptimeRobot, Datadog).
- Plan for backups and disaster recovery; test restores periodically.
- Use autoscaling (cloud) to handle traffic spikes.

## Security Best Practices
- Use HTTPS / TLS for all traffic; obtain certificates (Let’s Encrypt).
- Harden servers: close unused ports, keep software patched.
- Use firewalls, WAFs (Web Application Firewalls), and rate-limiting.
- Store secrets safely (managed secrets, environment variables) and avoid committing them to source control.
- Regularly scan for vulnerabilities and update dependencies.

## Cost Factors
- Pricing depends on compute, storage, bandwidth, managed services, and support levels.
- Compare reserved vs on-demand pricing on cloud providers for long-term workloads.

## Choosing a Host — Quick Checklist
- What traffic volume and performance do you expect?
- Do you need root access or managed support?
- Will you require relational or NoSQL databases, or serverless functions?
- What is your budget and desired SLA (uptime guarantee)?

## Glossary
- **Uptime:** Percentage of time a service is available.
- **SLA:** Service-level agreement; uptime and support terms.
- **Autoscaling:** Automatically adjust resources based on load.
- **TLS/SSL:** Encryption for web traffic.

## Resources & Further Reading
- MDN Web Docs — Server-side: https://developer.mozilla.org/
- DigitalOcean tutorials: https://www.digitalocean.com/community/tutorials
- Official docs for Nginx, Apache, and major cloud providers.

---

Prepared as concise lecture notes on web hosting for classroom or self-study.

