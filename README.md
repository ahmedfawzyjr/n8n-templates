# n8n Automation & Integration Templates

[![n8n Compatible](https://img.shields.io/badge/n8n-Workflow--Templates-red.svg)](https://n8n.io)
[![Category: Automation](https://img.shields.io/badge/Category-DevSecOps%20%7C%20AI%20%7C%20CRM-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A curated, production-ready repository of **n8n workflow templates** for enterprise automation, AI agent orchestration, DevSecOps pipelines, CRM synchronization, and automated data transformations.

---

## 📁 Template Directory & Index

| Category | Template Name | Description | Trigger |
| :--- | :--- | :--- | :--- |
| **AI & Agents** | `ai-rag-knowledgebase.json` | Vector search & RAG pipeline connecting Qdrant/Pinecone with OpenAI/Gemini | Webhook / API |
| **AI & Agents** | `ai-customer-support-agent.json` | Autonomous support agent with multi-tool calling & human handoff | Webhook |
| **DevSecOps** | `github-security-alerts-slack.json` | Parses GitHub Dependabot & CodeQL alerts and dispatches formatted Slack alerts | GitHub Event |
| **DevSecOps** | `docker-image-vulnerability-scanner.json` | Automated container scan notification pipeline using Trivy & n8n | Webhook |
| **CRM & Sales** | `hubspot-stripe-sync.json` | Bi-directional customer lifecycle & subscription sync between Stripe & HubSpot | Stripe Event |
| **Data & APIs** | `postgres-to-google-sheets-exporter.json` | Scheduled ETL job dumping filtered Postgres analytics into Google Sheets | Cron Schedule |

---

## 🚀 Quick Start Guide

### 1. Import a Template into n8n
1. Open your n8n instance (Self-hosted or Cloud).
2. Click **Workflows** → **Import from File** (or **Import from URL**).
3. Select the desired `.json` file from the `workflows/` directory in this repository.

### 2. Configure Environment Variables & Credentials
Ensure your n8n environment has the required credentials configured for the specific integration (e.g., API Keys, OAuth2 tokens, Database URIs).

---

## 🔐 Security & Best Practices

- **No Hardcoded Credentials**: All workflow JSON files are sanitized. Credentials must be attached inside your n8n instance.
- **Error Handling**: Workflows include error-trigger nodes and fallback messaging branches.
- **Rate Limit Safety**: Implements retry strategies (`retryOnFail`) and batch processing logic.

---

## 🤝 Contributing

Contributions are welcome! If you have optimized or created a new n8n workflow template:
1. Export your sanitized workflow as `.json`.
2. Place it in the appropriate subfolder (`workflows/category-name/`).
3. Open a Pull Request with a clear description and example usage.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
