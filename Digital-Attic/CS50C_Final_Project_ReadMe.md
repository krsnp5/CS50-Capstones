# DNS Redirection Demo (CS50 Cybersecurity)

## Ethical Disclaimer
This project is an educational simulation performed in a local, isolated environment.
It does not target real domains, real organizations, or real users. The demo domain
`realbank.test` is fictional and used only for local testing.

## Case Study Context (Information Integrity & Online Reputation)

Publicly reported cases of online reputation management have demonstrated how search engines can significantly influence public perception. In some instances, coordinated content campaigns have been used to shape search results by publishing large volumes of optimized content, registering multiple related domains, and targeting high-frequency search queries.

While such efforts may involve aggressive search engine optimization (SEO) rather than direct infrastructure compromise, they highlight a broader cybersecurity concern: the integrity of information systems that users rely on as sources of truth.

This project does not assert that infrastructure-level attacks occurred in any specific case. However, it uses these publicly discussed scenarios as inspiration to explore a related but more severe threat model — namely, how DNS redirection attacks could undermine trust in web systems by silently directing users to malicious lookalike websites.

By modeling DNS-based redirection in a controlled local environment, this project examines:

- How trust in domain resolution works
- How impersonation attacks could occur
- How TLS and X.509 certificates help mitigate such risks
- Why protecting information integrity is a core cybersecurity concern
- This simulation is strictly educational and does not involve any real domains, individuals, or services.

## What this demonstrates
- How "DNS redirection" can cause a user to reach a lookalike website
- Why HTTPS/TLS and X.509 certificates matter (certificate validation warnings)
- Integrity risks when name resolution is compromised

## Requirements
- Python 3.10+
- `pip install -r requirements.txt`

## How to run (HTTP demo)
Terminal 1:
python legit_server.py

Terminal 2:
python evil_server.py

Terminal 3:
python client.py

## Optional: HTTPS certificate demo
1) Generate a self-signed certificate:
python generate_cert.py

2) Run the HTTPS clone server:
python evil_https_server.py

Open:
https://127.0.0.1:8443
You should see a browser warning because the certificate is self-signed.

## Notes
This project models the threat class (DNS redirection) without modifying any real DNS
infrastructure. The "DNS" behavior is simulated inside `client.py`.# CS50
