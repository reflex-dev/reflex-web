"""Security page data configuration."""

from pcweb.pages.pricing.table import Feature

SECURITY_FEATURES = {
    "Data Protection": [
        Feature(
            name="Data Encryption",
            free="AES-256 encryption at rest, TLS 1.2+ in transit.",
        ),
        Feature(
            name="Database Backups",
            free="Daily encrypted backups with 30-day retention.",
        ),
        Feature(
            name="Data Segregation",
            free="Customer data is logically isolated per tenant.",
        ),
    ],
    "Product Security": [
        Feature(
            name="Penetration Testing",
            free="External tests conducted annually.",
        ),
        Feature(
            name="Secure Development Lifecycle",
            free="Code reviews, linting, and security scans.",
        ),
        Feature(
            name="Dependency Management",
            free="Automated scanning for vulnerabilities.",
        ),
    ],
    "Enterprise Security": [
        Feature(
            name="SSO/SAML",
            free="Supports major identity providers for centralized auth.",
        ),
        Feature(
            name="Granular Permissions",
            free="Role-based access control across teams.",
        ),
        Feature(
            name="Audit Logs",
            free="Track every access and change in the system.",
        ),
    ],
    "Data Privacy": [
        Feature(
            name="GDPR & CCPA Ready",
            free="Compliant data handling and user rights.",
        ),
        Feature(
            name="Data Deletion Requests",
            free="Users can request full data erasure.",
        ),
        Feature(
            name="Privacy by Design",
            free="Privacy baked into product architecture.",
        ),
    ],
}

# Trust services criteria for the grid cards
TRUST_SERVICES_CRITERIA = [
    {
        "title": "Security",
        "description": "Protection of systems and data from unauthorized access through firewalls, multi-factor authentication, and continuous monitoring.",
        "icon": "shield",
    },
    {
        "title": "Availability",
        "description": "Ensures that systems are operational and accessible as promised, with redundancy, failover systems, and uptime monitoring in place.",
        "icon": "globe",
    },
    {
        "title": "Confidentiality",
        "description": "Restricts access to sensitive information using encryption, role-based access controls, and secure data handling policies.",
        "icon": "backend_auth",
    },
    {
        "title": "Processing Integrity",
        "description": "Guarantees that system operations are accurate, timely, and authorized, using code reviews, automated tests, and deployment controls.",
        "icon": "code_custom",
    },
    {
        "title": "Privacy",
        "description": "Covers the collection, use, retention, and disposal of personal information according to regulatory and contractual obligations.",
        "icon": "clipboard",
    },
]

# Page content configuration
PAGE_CONTENT = {
    "title": "Security, Compliance, and Trust at Reflex",
    "subtitle": "We're committed to protecting your data through enterprise-grade security practices and full SOC 2 compliance.",
    "showcase": {
        "title": "Secure by default",
        "subtitle": "SOC 2 compliant with enterprise-grade security and flexible deployment options.",
        "logos": [
            {"src": "/soc2.webp", "alt": "SOC 2 Compliance"},
            {"src": "/databricks-partner.svg", "alt": "Databricks Partner"},
        ],
    },
    "table": {
        "title": "Enterprise-Grade Security at Every Layer",
        "description": "From data protection to privacy compliance, Reflex is built with security-first principles to meet the needs of modern teams and enterprises.",
    },
}
