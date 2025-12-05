---
author: Alek Petuskey
date: 2025-12-05
title: Reflex Build On-Prem - A Secure Builder Running in Your Environment
description: Run Reflex Build on your own infrastructure with full control, security, and compliance.
image: /blog/on-prem.png
meta: [
    {
      "name": "keywords",
      "content": "
        on-premises deployment,
        self-hosted reflex,
        enterprise deployment,
        private cloud deployment,
        air-gapped deployment,
        reflex enterprise,
        secure app deployment,
        compliance-ready deployment,
        infrastructure control,
        enterprise security,
        data sovereignty,
        private infrastructure,
        reflex self-hosting,
        enterprise python apps,
        secure web app deployment,
      "
    },
]
---

```python exec
import reflex as rx
import reflex_ui as ui
from pcweb import pages, constants
from reflex_image_zoom import image_zoom
from reflex_ui.blocks.demo_form import demo_form_dialog
```

For organizations with strict security, compliance, or data sovereignty requirements, building applications on your own infrastructure isn't just a preference—it's a necessity. With Reflex Enterprise, you can now run **Reflex Build**—our AI-powered app builder—on-premises or in your own private cloud, giving you complete control over your development environment while maintaining all the productivity benefits of building apps with AI.

## Why On-Premises Deployment?

Many enterprises face unique challenges that require on-premises solutions:

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/blog/connection.png",
            class_name="p-2 rounded-md h-auto w-full",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer py-6",
)
```

### Security and Compliance

Organizations in regulated industries—finance, healthcare, government, and defense—often have strict requirements about where their data can reside and how applications must be secured. On-premises deployment ensures:

- **Data Sovereignty**: Your data never leaves your infrastructure
- **Compliance**: Meet HIPAA, SOC 2, GDPR, and other regulatory requirements
- **Air-Gapped Environments**: Deploy in completely isolated networks
- **Custom Security Policies**: Implement your own security controls and monitoring

### Infrastructure Control

Some organizations need full control over their infrastructure:

- **Existing Cloud Investments**: Leverage your current AWS, Azure, or GCP infrastructure
- **Custom Networking**: Integrate with your existing network architecture
- **Resource Management**: Allocate resources according to your policies
- **Integration Requirements**: Connect with internal systems and services

## What's Included

Reflex Enterprise on-premises deployment includes Reflex Build running securely in your environment:

### Infrastructure & Deployment

- **Complete Deployment on Your Infrastructure**: Full deployment with standard Helm charts and Docker containerization
- **Fully Maintained by Reflex Team**: Automatic updates with latest security patches and features
- **System Integration**: Full integration with your PostgreSQL databases and internal backend systems
- **Performance Optimization**: Container lifecycle optimization and real-time state synchronization

### Data Sovereignty & Security

- **Zero PII Collection**: No Personally Identifiable Information collected
- **Strict Data Confinement**: All data remains exclusively within your controlled infrastructure
- **Access Control**: Data accessible only by authorized personnel, compliant with your security protocols
- **SSO/SAML Integration**: Connect with your existing identity provider
- **Audit Logs**: Complete audit trail of all builder activities

### Builder Features

- **AI-Powered App Building**: Build full-stack Python web apps using natural language prompts
- **Private Projects**: Keep all projects private within your infrastructure
- **Team Collaboration**: Manage team members and access controls
- **Enterprise Integrations**: Connect with all your company's internal services, documentation, databases, and APIs
- **Download App Code**: Export generated app code for full control

## Use Cases

```python eval
rx.el.div(
    image_zoom(
        rx.image(
            src="/blog/industries.png",
            class_name="p-2 rounded-md h-auto w-full",
            border=f"0.81px solid {rx.color('slate', 5)}",
        ),
        class_name="rounded-md overflow-hidden",
    ),
    class_name="w-full flex flex-col rounded-md cursor-pointer py-6",
)
```

### Financial Services

Financial institutions need to build internal tools and customer-facing apps while ensuring all code generation and app development happens within their controlled infrastructure. Reflex Build on-premises enables secure AI-powered app building in air-gapped environments.

### Government and Defense

Organizations with strict security requirements can use Reflex Build in completely isolated networks, meeting the highest security standards while leveraging AI to build modern web applications without exposing sensitive data.

### Healthcare

Healthcare organizations can run Reflex Build on-premises to meet HIPAA requirements, ensuring all app building activities and generated code remain within their controlled infrastructure.

### Multi-Cloud Enterprises

Large enterprises can run Reflex Build inside their own AWS and Azure environments, integrating with their existing SSO, logging, and infrastructure management systems while maintaining complete control over the development process.

## What's Next

If you're interested in deploying Reflex on-premises, book a demo to discuss your specific requirements. Our team will work with you to design a deployment that meets your security, compliance, and infrastructure needs.

```python eval
demo_form_dialog(
    ui.button(
        "Book a Demo",
        variant="primary",
        class_name="font-semibold",
    ),
)
```

With Reflex Build on-premises, you get the best of both worlds: the power and productivity of AI-powered app building, with the control and security of your own infrastructure. Build full-stack Python web apps faster than ever, all while keeping your code, data, and development process completely within your controlled environment.

