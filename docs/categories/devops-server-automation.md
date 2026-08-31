---
layout: default
title: "DevOps / Server Automation Templates for n8n | Awesome n8n Templates"
description: "6 n8n devops / server automation templates. Disk space monitoring, Docker controller webhooks, Linux updates, and server health checks."
---

<nav class="breadcrumb"><a href="{{ site.baseurl }}/">Home</a> / DevOps / Server Automation</nav>

# What n8n templates are available for DevOps and server automation?

Automate infrastructure monitoring and maintenance tasks with n8n. Templates include disk space watchdogs, Docker Compose controller webhooks, Linux remote updates, and scheduled server health checks.

<a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial -- Automate Your DevOps / Server Automation</a>
<br />
<small>* Referral link — this project receives a commission on eligible purchases.</small>

## Templates

| Template | Description | Department |
|---|---|---|
| [Audit a Public Page and Build an Automation Acceptance Pack](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/Audit%20a%20Public%20Page%20and%20Build%20an%20Automation%20Acceptance%20Pack.json) | Validate one public URL, collect bounded integration-readiness evidence, generate launch gates and acceptance tests, and route the result for implementation or review. | Engineering |
| [Disk Space Watchdog with Tiered Thresholds](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/Disk%20-%20Space%20-%20Watchdog.json) | Check disk usage over SSH on a schedule, warn at 80% and 90%, and alert only when a mountpoint changes level - no repeated alerts for the same full disk. Telegram with e-mail fallback. | SSH Tools |
| [Docker Compose Controller via Webhook](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/Docker%20-%20Compose%20-%20Controller.json) | Start or stop Docker Compose services on your server via authenticated HTTP POST request with n8n + SSH. | SSH Tools |
| [Linux - Update - Via - Webhook](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/Linux%20-%20Update%20-%20Via%20-%20Webhook.json) | Automated workflow for linux - update - via - webhook, streamlining execution and data processing. | Engineering |
| [n8n Failed Execution Doctor](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/n8n%20-%20Failed%20-%20Execution%20-%20Doctor.json) | Diagnose exported failed n8n execution data locally, identify the failing node, classify common root causes such as 401/403, 429, timeouts, network, invalid input, and expression errors, and return a focused next diagnostic step. No external API key or LLM required. | Engineering |
| [Uptime Ping Alert](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/DevOps/Uptime%20-%20Ping%20-%20Alert.json) | Pings a URL every 5 minutes and notifies Telegram only when the up/down state actually changes (no repeated alerts while it stays down). No external API key beyond a Telegram bot token. | SSH Tools |

## How to Use These Templates

1. [Sign up for n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) (Cloud trial available)
   <br />
   <small>* Referral link — this project receives a commission on eligible purchases.</small>
2. Download the JSON file for the template you want
3. In n8n, go to **Workflows > Import from File**
4. Connect your required credentials (API keys, OAuth tokens, etc.)
5. Test the nodes and activate the workflow

---

<p style="text-align: center; margin: 40px 0;">
  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial</a>
  <br />
  <small>* Referral link — this project receives a commission on eligible purchases.</small>
</p>

[Back to all categories]({{ site.baseurl }}/)
