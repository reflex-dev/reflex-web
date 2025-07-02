"""Security page data configuration."""

# Feature data organized by category
SECURITY_FEATURES = {
    "Data Protection": [
        ("Data Encryption", "AES-256 encryption at rest, TLS 1.2+ in transit."),
        ("Database Backups", "Daily encrypted backups with 30-day retention."),
        ("Data Segregation", "Customer data is logically isolated per tenant."),
    ],
    "Product Security": [
        ("Penetration Testing", "External tests conducted annually."),
        ("Secure Development Lifecycle", "Code reviews, linting, and security scans."),
        ("Dependency Management", "Automated scanning for vulnerabilities."),
    ],
    "Enterprise Security": [
        ("SSO/SAML", "Supports major identity providers for centralized auth."),
        ("Granular Permissions", "Role-based access control across teams."),
        ("Audit Logs", "Track every access and change in the system."),
    ],
    "Data Privacy": [
        ("GDPR & CCPA Ready", "Compliant data handling and user rights."),
        ("Data Deletion Requests", "Users can request full data erasure."),
        ("Privacy by Design", "Privacy baked into product architecture."),
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
    }
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
            {"src": "/databricks-partner.svg", "alt": "Databricks Partner"}
        ]
    },
    "table": {
        "title": "Enterprise-Grade Security at Every Layer",
        "description": "From data protection to privacy compliance, Reflex is built with security-first principles to meet the needs of modern teams and enterprises."
    }
}
