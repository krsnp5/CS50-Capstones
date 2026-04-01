from datetime import datetime, timedelta

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

DOMAIN = "realbank.test"


def main():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "PH"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "DNS Redirection Demo"),
            x509.NameAttribute(NameOID.COMMON_NAME, DOMAIN),
        ]
    )

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow() - timedelta(minutes=5))
        .not_valid_after(datetime.utcnow() + timedelta(days=30))
        .add_extension(
            x509.SubjectAlternativeName([x509.DNSName(DOMAIN)]),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )

    with open("key.pem", "wb") as f:
        f.write(
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open("cert.pem", "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print(f"Generated cert.pem and key.pem (self-signed) for {DOMAIN}")


if __name__ == "__main__":
    main()
