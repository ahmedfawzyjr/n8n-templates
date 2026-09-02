import os
import sys
import json
import re
import urllib.parse
from datetime import datetime
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_CONFIG = [
    {
        "folder": "Gmail and Email Automation",
        "slug": "gmail-email-automation",
        "name": "Gmail & Email Automation",
        "icon": "mail",
        "color": "#EA4335",
        "heading": "What n8n templates are available for Gmail and email automation?",
        "intro": "This collection includes email automation templates for n8n covering Gmail, Outlook, and IMAP. Templates range from AI-powered email labeling and categorization with OpenAI to phishing detection, auto-reply drafting, and daily financial news delivery. Ideal for operations, security, and executive teams looking to streamline email management.",
        "short_desc": "AI email labeling, phishing detection, auto-reply drafts, and Outlook automation."
    },
    {
        "folder": "Telegram",
        "slug": "telegram-bots",
        "name": "Telegram",
        "icon": "send",
        "color": "#229ED9",
        "heading": "How can I automate Telegram bots with n8n?",
        "intro": "These n8n templates help you build AI-powered Telegram bots for voice-to-text transcription in 55+ languages, document Q&A, customer support, audio streaming, and personal assistants. Perfect for support teams, content creators, and developers deploying interactive chatbots.",
        "short_desc": "AI chatbots with LangChain, voice-to-text in 55 languages, PDF chat, and Spotify integration."
    },
    {
        "folder": "Google Drive and Google Sheets",
        "slug": "google-drive-sheets",
        "name": "Google Drive & Google Sheets",
        "icon": "hard-drive",
        "color": "#0F9D58",
        "heading": "What are the best n8n templates for Google Drive and Google Sheets?",
        "intro": "Automate Google Workspace with n8n templates for Google Drive and Google Sheets. Workflows include RAG chatbots for Google Docs, automated fine-tuning of OpenAI models, lead qualification, and dynamic data syncing between spreadsheets and third-party tools.",
        "short_desc": "RAG chatbots for documents, OpenAI fine-tuning, lead qualification, and HR screening."
    },
    {
        "folder": "WordPress",
        "slug": "wordpress",
        "name": "WordPress",
        "icon": "globe",
        "color": "#21759B",
        "heading": "How do I automate WordPress with n8n?",
        "intro": "Streamline content management and publishing with these WordPress automation templates for n8n. Includes AI-driven blog post categorization, SEO content generation with DeepSeek and OpenAI, and embedding AI chatbots directly on WordPress sites.",
        "short_desc": "AI blog categorization, content generation with DeepSeek, and chatbot embedding."
    },
    {
        "folder": "PDF and Document Processing",
        "slug": "pdf-document-processing",
        "name": "PDF & Document Processing",
        "icon": "file-text",
        "color": "#DC2626",
        "heading": "What n8n templates exist for PDF and document processing?",
        "intro": "Process documents at scale using n8n workflows for PDF parsing, OCR, and AI-driven data extraction. Templates cover conversational PDF chatbots with source citations, invoice parsing with LlamaParse and Mistral, and study note generation.",
        "short_desc": "PDF Q&A with source quoting, resume parsing, invoice extraction, and OCR pipelines."
    },
    {
        "folder": "Discord",
        "slug": "discord",
        "name": "Discord",
        "icon": "message-square",
        "color": "#5865F2",
        "heading": "How can I automate Discord with n8n?",
        "intro": "Connect n8n to Discord for automated community management and content delivery. Templates include AI bot routing, scheduled sports match notifications, daily comic translations, and automated video summary sharing.",
        "short_desc": "AI Discord bot routing, daily comic translations, and YouTube summary sharing."
    },
    {
        "folder": "Database and Storage",
        "slug": "database-storage",
        "name": "Database & Storage",
        "icon": "database",
        "color": "#3B82F6",
        "heading": "What are the best n8n database and storage automation templates?",
        "intro": "Bridge n8n with SQL and NoSQL databases. These templates include conversational interfaces for PostgreSQL and MongoDB, automated SQL query generation from schemas, and storage management workflows.",
        "short_desc": "Natural language SQL generation, PostgreSQL chat, and MongoDB recommendation engines."
    },
    {
        "folder": "DevOps",
        "slug": "devops-server-automation",
        "name": "DevOps / Server Automation",
        "icon": "terminal",
        "color": "#6366F1",
        "heading": "What n8n templates are available for DevOps and server automation?",
        "intro": "Automate infrastructure monitoring and maintenance tasks with n8n. Templates include disk space watchdogs, Docker Compose controller webhooks, Linux remote updates, and scheduled server health checks.",
        "short_desc": "Disk space monitoring, Docker controller webhooks, Linux updates, and server health checks."
    },
    {
        "folder": "Airtable",
        "slug": "airtable",
        "name": "Airtable",
        "icon": "table",
        "color": "#F59E0B",
        "heading": "How do I automate Airtable with n8n?",
        "intro": "Leverage Airtable as a flexible backend for your automations. These n8n templates enable AI agents to chat with Airtable bases, synchronize project management and meeting notes from Fireflies.ai, and sync with Obsidian.",
        "short_desc": "AI agents querying Airtable, meeting notes sync from Fireflies, and Obsidian integration."
    },
    {
        "folder": "Notion",
        "slug": "notion",
        "name": "Notion",
        "icon": "book-open",
        "color": "#64748B",
        "heading": "What are the best n8n templates for Notion?",
        "intro": "Turn Notion into an automated knowledge hub. Workflows include archiving customer feedback, summarizing Hugging Face research papers, automating competitor intelligence with Exa.ai, and converting emails into tasks.",
        "short_desc": "Customer feedback logging, AI paper summaries, competitor research, and task generation."
    },
    {
        "folder": "Slack",
        "slug": "slack",
        "name": "Slack",
        "icon": "briefcase",
        "color": "#4A154B",
        "heading": "How can I automate Slack with n8n?",
        "intro": "Enhance team communication and operations with Slack automation workflows for n8n. Includes Gemini-powered Slack bots, automated customer support ticketing with Linear, information monitoring, and automated daily digest delivery.",
        "short_desc": "Gemini AI Slack bots, Linear ticketing sync, info monitoring, and daily digests."
    },
    {
        "folder": "OpenAI and LLMs",
        "slug": "openai-llms",
        "name": "OpenAI & LLMs",
        "icon": "bot",
        "color": "#10A37F",
        "heading": "What n8n templates are available for OpenAI, LLMs, and AI agents?",
        "intro": "This comprehensive collection features n8n templates for OpenAI, Anthropic Claude, Google Gemini, Mistral, Ollama, DeepSeek, and LangChain agents. Covers autonomous agents, multi-agent evaluation, tool calling, lead enrichment, image generation, audio transcription, and specialized assistants.",
        "short_desc": "Autonomous agents, LangChain tool calling, multi-agent evaluation, lead scoring, and vision pipelines."
    },
    {
        "folder": "WhatsApp",
        "slug": "whatsapp",
        "name": "WhatsApp",
        "icon": "phone",
        "color": "#25D366",
        "heading": "How do I build WhatsApp chatbots with n8n?",
        "intro": "Build business automations and chatbots for WhatsApp using n8n. Templates cover automated sales meeting preparation with Apify, customer inquiry handling, multilingual lead capture, and escalating invoice reminders.",
        "short_desc": "WhatsApp chatbots, meeting prep with Apify, lead capture, and payment reminders."
    },
    {
        "folder": "Instagram Twitter Social Media",
        "slug": "social-media",
        "name": "Instagram, Twitter, Social Media",
        "icon": "share-2",
        "color": "#E1306C",
        "heading": "What are the best n8n templates for social media automation?",
        "intro": "Automate social media marketing across Instagram, X (Twitter), LinkedIn, YouTube, TikTok, and Pinterest. Templates include AI content repurposing engines, Instagram DM inboxes with ManyChat, competitor engagement analysis, and scheduled auto-posting.",
        "short_desc": "Omnichannel repurposing, Instagram DM AI inbox, YouTube transcription, and competitor monitoring."
    },
    {
        "folder": "Other Integrations and Use Cases",
        "slug": "other-integrations",
        "name": "Other Integrations & Use Cases",
        "icon": "plug",
        "color": "#8B5CF6",
        "heading": "What other n8n integration templates are available?",
        "intro": "Explore diverse n8n workflows covering specialized APIs, web scraping, e-commerce, weather alerts, financial analysis, uptime monitoring, and multi-service connectors like Mattermost, Linear, AWS, and Stripe.",
        "short_desc": "Web scraping, e-commerce workflows, Mattermost integration, AWS analysis, and webhook pipelines."
    },
    {
        "folder": "Forms and Surveys",
        "slug": "forms-surveys",
        "name": "Forms & Surveys",
        "icon": "check-square",
        "color": "#06B6D4",
        "heading": "How do I automate forms and surveys with n8n?",
        "intro": "Create interactive and conversational form automations using n8n Forms. Templates feature conversational AI interviews, lead qualification with appointment booking, email subscription flows with Airtable, and automated survey feedback analysis.",
        "short_desc": "Conversational AI interviews, appointment qualification, and automated survey analysis."
    },
    {
        "folder": "AI Research RAG and Data Analysis",
        "slug": "ai-research-rag",
        "name": "AI Research, RAG & Data Analysis",
        "icon": "flask",
        "color": "#EC4899",
        "heading": "What n8n templates exist for AI research, RAG, and data analysis?",
        "intro": "Advanced AI research and data analysis workflows utilizing vector databases (Qdrant, Pinecone, Milvus), autonomous research agents (Apify, o3, Perplexity, Tavily), financial document analyzers, Hacker News aggregators, and Google Analytics AI reporters.",
        "short_desc": "Deep research agents, vector database RAG, financial document analysis, and web scraping pipelines."
    },
    {
        "folder": "HR and Recruitment",
        "slug": "hr-recruitment",
        "name": "HR & Recruitment",
        "icon": "users",
        "color": "#14B8A6",
        "heading": "What n8n templates are available for HR and recruitment automation?",
        "intro": "Streamline talent acquisition and employee operations with HR automation templates for n8n. Features automated CV screening with OpenAI, BambooHR policy and benefits chatbots, job posting generation, and employee helpdesk bots with voice transcription.",
        "short_desc": "AI CV screening, BambooHR policy chatbots, job description generation, and IT helpdesk bots."
    }
]

SVG_ICONS = {
    'mail': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    'send': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg>',
    'hard-drive': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><line x1="22" x2="2" y1="12" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" x2="6.01" y1="16" y2="16"/><line x1="10" x2="10.01" y1="16" y2="16"/></svg>',
    'globe': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>',
    'file-text': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
    'message-square': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    'database': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"/></svg>',
    'terminal': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg>',
    'table': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg>',
    'book-open': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    'briefcase': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    'bot': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>',
    'phone': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    'share-2': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg>',
    'plug': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 2v6"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg>',
    'check-square': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11 3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    'flask': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M10 2v7.31"/><path d="M14 2v7.31"/><path d="M8.5 2h7"/><path d="M14 9.3 20.7 20.3c.7 1.1-.1 2.7-1.4 2.7H4.7c-1.3 0-2.1-1.6-1.4-2.7L10 9.3"/><path d="M6.3 17h11.4"/></svg>',
    'users': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    'zap': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    'search': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    'x': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
    'copy': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>',
    'check': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    'eye': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/></svg>',
    'download': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/></svg>',
    'external-link': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" x2="21" y1="14" y2="3"/></svg>',
    'arrow-up-right': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"/><path d="M7 7h10v10"/></svg>',
    'chevron-down': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    'sun': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>',
    'moon': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>',
    'grid': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg>',
    'list': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><line x1="8" x2="21" y1="6" y2="6"/><line x1="8" x2="21" y1="12" y2="12"/><line x1="8" x2="21" y1="18" y2="18"/><line x1="3" x2="3.01" y1="6" y2="6"/><line x1="3" x2="3.01" y1="12" y2="12"/><line x1="3" x2="3.01" y1="18" y2="18"/></svg>',
    'sparkles': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/><path d="M5 3v4"/><path d="M19 17v4"/><path d="M3 5h4"/><path d="M17 19h4"/></svg>',
    'shield': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    'layers': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    'folder': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/></svg>',
    'star': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    'cpu': '<svg class="svg-icon {cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/></svg>'
}

def get_svg_icon(name, size=16, cls="", stroke_width=2):
    tmpl = SVG_ICONS.get(name, SVG_ICONS['layers'])
    return tmpl.format(size=size, cls=cls, stroke_width=stroke_width)

FRIENDLY_NODE_NAMES = {
    'n8n-nodes-base.openAi': 'OpenAI',
    '@n8n/n8n-nodes-langchain.agent': 'AI Agent',
    '@n8n/n8n-nodes-langchain.lmChatOpenAi': 'OpenAI Chat',
    '@n8n/n8n-nodes-langchain.lmChatAnthropic': 'Claude',
    '@n8n/n8n-nodes-langchain.lmChatGoogleGemini': 'Gemini',
    '@n8n/n8n-nodes-langchain.lmChatOllama': 'Ollama',
    '@n8n/n8n-nodes-langchain.lmChatMistral': 'Mistral',
    '@n8n/n8n-nodes-langchain.vectorStoreQdrant': 'Qdrant',
    '@n8n/n8n-nodes-langchain.vectorStorePinecone': 'Pinecone',
    '@n8n/n8n-nodes-langchain.memoryBufferWindow': 'Buffer Memory',
    '@n8n/n8n-nodes-langchain.toolHttpRequest': 'HTTP Tool',
    '@n8n/n8n-nodes-langchain.toolCode': 'Code Tool',
    'n8n-nodes-base.gmail': 'Gmail',
    'n8n-nodes-base.gmailTrigger': 'Gmail Trigger',
    'n8n-nodes-base.googleSheets': 'Google Sheets',
    'n8n-nodes-base.googleSheetsTrigger': 'Google Sheets Trigger',
    'n8n-nodes-base.googleDrive': 'Google Drive',
    'n8n-nodes-base.googleDriveTrigger': 'Google Drive Trigger',
    'n8n-nodes-base.googleDocs': 'Google Docs',
    'n8n-nodes-base.telegram': 'Telegram',
    'n8n-nodes-base.telegramTrigger': 'Telegram Trigger',
    'n8n-nodes-base.slack': 'Slack',
    'n8n-nodes-base.slackTrigger': 'Slack Trigger',
    'n8n-nodes-base.discord': 'Discord',
    'n8n-nodes-base.discordTrigger': 'Discord Trigger',
    'n8n-nodes-base.airtable': 'Airtable',
    'n8n-nodes-base.airtableTrigger': 'Airtable Trigger',
    'n8n-nodes-base.notion': 'Notion',
    'n8n-nodes-base.notionTrigger': 'Notion Trigger',
    'n8n-nodes-base.whatsApp': 'WhatsApp',
    'n8n-nodes-base.whatsAppTrigger': 'WhatsApp Trigger',
    'n8n-nodes-base.postgres': 'PostgreSQL',
    'n8n-nodes-base.postgresTrigger': 'PostgreSQL Trigger',
    'n8n-nodes-base.mySql': 'MySQL',
    'n8n-nodes-base.mongoDb': 'MongoDB',
    'n8n-nodes-base.httpRequest': 'HTTP Request',
    'n8n-nodes-base.webhook': 'Webhook',
    'n8n-nodes-base.scheduleTrigger': 'Schedule Trigger',
    'n8n-nodes-base.code': 'Code JS/Python',
    'n8n-nodes-base.function': 'Function',
    'n8n-nodes-base.if': 'IF Condition',
    'n8n-nodes-base.switch': 'Switch',
    'n8n-nodes-base.set': 'Edit Fields (Set)',
    'n8n-nodes-base.merge': 'Merge',
    'n8n-nodes-base.splitInBatches': 'Loop / Batches',
    'n8n-nodes-base.readWriteFile': 'Read/Write File',
    'n8n-nodes-base.respondToWebhook': 'Respond to Webhook',
    'n8n-nodes-base.executeWorkflow': 'Execute Workflow',
    'n8n-nodes-base.formTrigger': 'n8n Form Trigger',
    'n8n-nodes-base.github': 'GitHub',
    'n8n-nodes-base.githubTrigger': 'GitHub Trigger',
    'n8n-nodes-base.jira': 'Jira',
    'n8n-nodes-base.hubspot': 'HubSpot',
    'n8n-nodes-base.stripe': 'Stripe',
    'n8n-nodes-base.awsS3': 'AWS S3',
    'n8n-nodes-base.awsSes': 'AWS SES',
    'n8n-nodes-base.ssh': 'SSH',
    'n8n-nodes-base.ftp': 'FTP / SFTP',
    'n8n-nodes-base.emailSend': 'Send Email (SMTP)',
    'n8n-nodes-base.emailReadImap': 'Read Email (IMAP)',
    'n8n-nodes-base.crypto': 'Crypto / Hash',
    'n8n-nodes-base.extractFromFile': 'Extract from File',
    'n8n-nodes-base.compression': 'Compression (Zip)',
    'n8n-nodes-base.xml': 'XML',
    'n8n-nodes-base.html': 'HTML Extract'
}

def get_friendly_node_name(node_type):
    if node_type in FRIENDLY_NODE_NAMES:
        return FRIENDLY_NODE_NAMES[node_type]
    clean = node_type.split('.')[-1]
    # CamelCase to Space
    clean = re.sub(r'([a-z])([A-Z])', r'\1 \2', clean)
    clean = clean.replace('Trigger', ' (Trigger)').strip()
    return clean

DEPARTMENT_KEYWORDS = {
    'Marketing': ['marketing', 'seo', 'blog', 'social media', 'instagram', 'twitter', 'content', 'youtube', 'tiktok', 'campaign', 'newsletter', 'linkedin', 'facebook', 'pinterest', 'comic', 'reddit'],
    'Sales': ['sales', 'lead', 'crm', 'qualification', 'deal', 'enrichment', 'booking', 'appointment', 'client', 'hubspot', 'pipedrive', 'prospect'],
    'Support': ['support', 'helpdesk', 'customer', 'inquiry', 'ticketing', 'ticket', 'faq', 'zendesk', 'linear', 'chat', 'feedback', 'assistant', 'bot', 'complaint'],
    'Engineering': ['devops', 'server', 'docker', 'linux', 'deploy', 'monitoring', 'disk', 'database', 'postgres', 'sql', 'mongodb', 'mysql', 'api', 'webhook', 'git', 'github', 'sentry', 'ssh'],
    'HR': ['hr', 'recruitment', 'hiring', 'cv', 'resume', 'screening', 'employee', 'onboarding', 'bamboohr', 'job', 'interview', 'talent'],
    'Finance': ['finance', 'invoice', 'payment', 'billing', 'stripe', 'expense', 'accounting', 'crypto', 'receipt', 'tax'],
    'Executive': ['executive', 'briefing', 'daily digest', 'paper summary', 'research', 'analytics', 'report', 'intelligence', 'arxiv', 'news summary', 'weather']
}

def infer_department(title, desc, filename, category_name):
    full_text = f"{title} {desc} {filename} {category_name}".lower()
    for dept, keywords in DEPARTMENT_KEYWORDS.items():
        if any(kw in full_text for kw in keywords):
            return dept
    return "Operations"

def clean_workflow_title(title, filename):
    t = title.strip()
    # Strip emojis and special symbols
    t = re.sub(r'[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf\ufe0f]', '', t).strip()
    
    if not t or t.lower() == 'my workflow' or t.lower() == 'workflow' or t.lower() == 'untitled workflow':
        name_no_ext = os.path.splitext(filename)[0]
        # Remove leading numbers and hyphens like "01-", "002_"
        name_no_ext = re.sub(r'^\d+[\s\-_.]*', '', name_no_ext)
        # Convert dashes and underscores to spaces
        t = name_no_ext.replace('_', ' ').replace('-', ' ').title()
    
    # Remove awkward suffixes
    t = re.sub(r'\s*\(\s*\d+\s*\)$', '', t)
    t = re.sub(r'\s*-\s*n8n\s*workflow.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s*workflow\s*$', '', t, flags=re.IGNORECASE).strip()
    t = re.sub(r'\s+', ' ', t).strip()
    if not t:
        t = os.path.splitext(filename)[0].replace('_', ' ').replace('-', ' ').title()
    return t

def generate_seo_description(title, nodes, category_name, department):
    key_nodes = []
    for n in nodes:
        fn = get_friendly_node_name(n)
        if fn not in key_nodes and fn not in ['Edit Fields (Set)', 'IF Condition', 'Code JS/Python', 'Schedule Trigger', 'Webhook']:
            key_nodes.append(fn)
    
    nodes_str = ', '.join(key_nodes[:4]) if key_nodes else 'core automation nodes'
    
    clean_t = title.lower()
    if 'rag' in clean_t or 'agent' in clean_t or 'chat' in clean_t:
        return f"Autonomous {department.lower()} automation workflow connecting {nodes_str}. Implements intelligent data retrieval, AI reasoning, and instant responses."
    elif 'sync' in clean_t or 'database' in clean_t or 'sheets' in clean_t:
        return f"Production-grade {department.lower()} workflow for automated data synchronization and pipeline processing using {nodes_str}."
    elif 'email' in clean_t or 'notification' in clean_t or 'alert' in clean_t:
        return f"Real-time event-driven {department.lower()} alert and notification workflow leveraging {nodes_str}."
    else:
        return f"End-to-end {department.lower()} automation template for {category_name}. Integrates {nodes_str} for reliable automated execution."

def main():
    all_categories_data = []
    flat_templates_list = []
    node_counter = Counter()
    total_templates = 0

    for cfg in CATEGORY_CONFIG:
        folder_path = os.path.join(ROOT, cfg['folder'])
        if not os.path.exists(folder_path):
            print(f"Warning: Folder not found: {folder_path}")
            continue
        
        json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        templates_in_cat = []
        
        for f in json_files:
            file_path = os.path.join(folder_path, f)
            total_templates += 1
            
            try:
                with open(file_path, 'r', encoding='utf-8') as jf:
                    data = json.load(jf)
            except Exception as e:
                print(f"Error reading JSON {file_path}: {e}")
                data = {}
            
            raw_title = data.get('name', '') if isinstance(data, dict) else ''
            title = clean_workflow_title(raw_title, f)
            
            # Nodes extraction
            nodes = data.get('nodes', []) if isinstance(data, dict) else []
            node_types = []
            for n in nodes:
                if isinstance(n, dict) and 'type' in n:
                    nt = n['type']
                    node_types.append(nt)
                    node_counter[nt] += 1
            
            unique_nodes_in_file = sorted(list(set(node_types)))
            dept = infer_department(title, "", f, cfg['name'])
            desc = generate_seo_description(title, unique_nodes_in_file, cfg['name'], dept)
            
            clean_name = f
            enc_folder = urllib.parse.quote(cfg['folder'])
            enc_file = urllib.parse.quote(f)
            
            readme_table_link = f"[{f}]({enc_folder}/{enc_file})"
            gh_link = f"https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/{enc_folder}/{enc_file}"
            raw_gh_link = f"https://raw.githubusercontent.com/ahmedfawzyjr/N8N-Templates/main/{enc_folder}/{enc_file}"
            
            # Format node tags
            node_names = [get_friendly_node_name(nt) for nt in unique_nodes_in_file]
            node_names = sorted(list(set(node_names)))
            
            tmpl_id = re.sub(r'[^a-z0-9\-]', '', f.lower().replace(' ', '-').replace('.json', ''))
            
            template_obj = {
                'id': tmpl_id,
                'filename': f,
                'title': title,
                'desc': desc,
                'description': desc,
                'dept': dept,
                'department': dept,
                'category': cfg['name'],
                'category_slug': cfg['slug'],
                'category_icon': cfg['icon'],
                'category_color': cfg['color'],
                'readme_link': readme_table_link,
                'gh_link': gh_link,
                'github_url': gh_link,
                'raw_github_url': raw_gh_link,
                'node_count': len(nodes),
                'node_names': node_names,
                'clean_name': clean_name
            }
            
            templates_in_cat.append(template_obj)
            flat_templates_list.append(template_obj)
            
        templates_in_cat.sort(key=lambda x: x['title'].lower())
        
        all_categories_data.append({
            'config': cfg,
            'templates': templates_in_cat,
            'count': len(templates_in_cat)
        })

    print(f"Total Categories: {len(all_categories_data)}, Total Templates: {total_templates}")

    generate_json_and_js_registry(all_categories_data, flat_templates_list, total_templates)
    generate_readme(all_categories_data, total_templates)
    generate_docs_index(all_categories_data, total_templates, total_node_types=len(node_counter))
    generate_docs_categories(all_categories_data)
    generate_unique_nodes_txt(node_counter, total_templates)
    generate_static_html(all_categories_data, total_templates)
    
    print("All documentation, interactive registries, and category files synchronized successfully!")

def generate_static_html(categories_data, total_templates):
    layout_path = os.path.join(ROOT, 'docs', '_layouts', 'default.html')
    if not os.path.exists(layout_path):
        return
    with open(layout_path, 'r', encoding='utf-8') as f:
        layout = f.read()

    index_md_path = os.path.join(ROOT, 'docs', 'index.md')
    with open(index_md_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    parts = index_content.split('---', 2)
    body = parts[2] if len(parts) >= 3 else index_content

    body_html = body
    body_html = re.sub(r'## (.*?)\n', r'<h2>\1</h2>\n', body_html)
    body_html = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', body_html)
    body_html = body_html.replace('{{ site.baseurl }}', '.')

    page_html = layout
    page_html = page_html.replace('{{ site.baseurl }}', '.')
    page_html = page_html.replace('{{ page.title | default: site.title }}', f'n8n Portal — Curated Production Automation Templates Directory & AI Workflows')
    page_html = page_html.replace('{{ page.description | default: site.description }}', f'Curated open-source directory of {total_templates}+ production-ready n8n automation workflow templates, AI agents, and integrations.')
    page_html = page_html.replace('{% seo %}', f'<meta name="description" content="Curated open-source directory of {total_templates}+ production-ready n8n automation workflow templates.">')
    page_html = page_html.replace('{% include head-custom.html %}', '')
    page_html = page_html.replace('{{ content }}', body_html)
    page_html = page_html.replace("{{ site.time | date: '%Y' }}", '2026')

    static_index_path = os.path.join(ROOT, 'docs', 'index.html')
    with open(static_index_path, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("docs/index.html static compiled successfully")

    docs_cat_dir = os.path.join(ROOT, 'docs', 'categories')
    for cat in categories_data:
        cfg = cat['config']
        md_file = os.path.join(docs_cat_dir, f"{cfg['slug']}.md")
        if os.path.exists(md_file):
            with open(md_file, 'r', encoding='utf-8') as f:
                c_content = f.read()
            c_parts = c_content.split('---', 2)
            c_body = c_parts[2] if len(c_parts) >= 3 else c_content
            c_body_html = c_body
            c_body_html = re.sub(r'## (.*?)\n', r'<h2>\1</h2>\n', c_body_html)
            c_body_html = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', c_body_html)
            c_body_html = c_body_html.replace('{{ site.baseurl }}', '..')

            cat_html = layout
            cat_html = cat_html.replace('{{ site.baseurl }}', '..')
            cat_html = cat_html.replace('{{ page.title | default: site.title }}', f'{cfg["name"]} Automation Templates | n8n Portal')
            cat_html = cat_html.replace('{{ page.description | default: site.description }}', f'{cat["count"]} production-ready n8n {cfg["name"].lower()} automation templates. {cfg["short_desc"]}')
            cat_html = cat_html.replace('{% seo %}', f'<meta name="description" content="{cat["count"]} n8n {cfg["name"].lower()} templates.">')
            cat_html = cat_html.replace('{% include head-custom.html %}', '')
            cat_html = cat_html.replace('{{ content }}', c_body_html)
            cat_html = cat_html.replace("{{ site.time | date: '%Y' }}", '2026')

            cat_html_path = os.path.join(docs_cat_dir, f"{cfg['slug']}.html")
            with open(cat_html_path, 'w', encoding='utf-8') as f:
                f.write(cat_html)
    print("docs/categories/*.html static compiled successfully")

def generate_json_and_js_registry(categories_data, flat_templates, total_templates):
    json_path = os.path.join(ROOT, 'docs', 'templates.json')
    cats_summary = []
    for c in categories_data:
        cfg = c['config']
        cats_summary.append({
            'name': cfg['name'],
            'slug': cfg['slug'],
            'icon': cfg['icon'],
            'color': cfg['color'],
            'short_desc': cfg['short_desc'],
            'count': c['count']
        })
        
    full_data = {
        'total': total_templates,
        'categories': cats_summary,
        'templates': flat_templates
    }
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(full_data, f, indent=2, ensure_ascii=False)
    print(f"docs/templates.json generated ({len(flat_templates)} templates)")
    
    js_path = os.path.join(ROOT, 'docs', 'assets', 'js', 'templates-data.js')
    os.makedirs(os.path.dirname(js_path), exist_ok=True)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write('/**\n * n8n Portal Templates Data Store - Auto-generated\n */\n')
        f.write('window.N8N_CATEGORIES = ' + json.dumps(cats_summary, indent=2, ensure_ascii=False) + ';\n\n')
        f.write('window.N8N_TEMPLATES = ' + json.dumps(flat_templates, indent=2, ensure_ascii=False) + ';\n')
    print(f"docs/assets/js/templates-data.js generated")

def generate_readme(categories_data, total_templates):
    readme_path = os.path.join(ROOT, 'README.md')
    lines = []
    
    lines.append('# n8n Portal — Production Automation Templates Directory [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)')
    lines.append('')
    lines.append(f'> A curated directory of **{total_templates}+** production-ready n8n automation workflow templates, AI agents, RAG pipelines, and enterprise integrations.')
    lines.append('')
    lines.append('Workflows are ready-to-import `.json` files. Download or copy any template and import it directly into your n8n instance (Cloud or self-hosted). Always review and test imported templates before deploying them in production.')
    lines.append('')
    current_date_badge = datetime.now().strftime("%b_%d,_%Y")
    lines.append(f'[![Templates](https://img.shields.io/badge/Templates-{total_templates}+-blue.svg?style=flat-square)](#categories--template-list)')
    lines.append(f'[![Categories](https://img.shields.io/badge/Categories-18-green.svg?style=flat-square)](#categories--template-list)')
    lines.append(f'[![Last Updated](https://img.shields.io/badge/Updated-{current_date_badge}-brightgreen.svg?style=flat-square)](#)')
    lines.append('[![n8n](https://img.shields.io/badge/n8n-Compatible-FF6D5A.svg?style=flat-square&logo=n8n)](https://n8n.partnerlinks.io/h1pwwf5m4toe)')
    lines.append('[![n8n Portal](https://img.shields.io/badge/Live_Portal-n8nportal.vercel.app-success.svg?style=flat-square)](https://n8nportal.vercel.app/)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('<p align="center">')
    lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">')
    lines.append('    <img src="https://img.shields.io/badge/n8n_Cloud-Start_Trial-orange?style=for-the-badge" alt="Start an n8n Cloud trial" />')
    lines.append('  </a>')
    lines.append('</p>')
    lines.append('')
    lines.append('## Table of Contents')
    lines.append('')
    lines.append('- [Interactive Web Portal](https://n8nportal.vercel.app/)')
    lines.append('- [Categories & Template List](#categories--template-list)')
    for cat in categories_data:
        cfg = cat['config']
        anchor = re.sub(r'[^a-z0-9\- ]', '', cfg['heading'].lower()).replace(' ', '-')
        lines.append(f"  - [{cfg['name']} ({cat['count']})](#{anchor})")
    lines.append('- [Unique Nodes Reference](#unique-nodes-reference)')
    lines.append('- [FAQ](#faq)')
    lines.append('- [Contributing](#contributing)')
    lines.append('- [Sponsors](#sponsors)')
    lines.append('- [Star History](#star-history)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Categories & Template List')
    lines.append('')
    
    for cat in categories_data:
        cfg = cat['config']
        lines.append(f"### {cfg['heading']}")
        lines.append('')
        lines.append(f"{cfg['intro']}")
        lines.append('')
        lines.append('| Title | Description | Department | Link |')
        lines.append('|---|---|---|---|')
        for t in cat['templates']:
            lines.append(f"| {t['title']} | {t['desc']} | {t['dept']} | {t['readme_link']} |")
        lines.append('')
        lines.append('---')
        lines.append('')
    
    lines.append('### Unique Nodes Reference')
    lines.append('')
    lines.append('For a complete inventory of all 200+ distinct n8n node types and node packages utilized across these templates, refer to [ALL_unique_nodes.txt](ALL_unique_nodes.txt).')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## FAQ')
    lines.append('')
    lines.append('### How do I import an n8n template from this repository?')
    lines.append('')
    lines.append('Download the `.json` file for any template you want to use. Open your n8n instance (either self-hosted or on [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe)), navigate to Workflows, click "Import from File," and select the downloaded JSON file. Or use the [Interactive Web Portal](https://n8nportal.vercel.app/) to click "Copy JSON" and paste (Ctrl+V) directly into your n8n canvas!')
    lines.append('')
    lines.append('### What is n8n and why should I use it for automation?')
    lines.append('')
    lines.append('[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) is a fair-code, source-available workflow automation platform that gives you total control over your data and infrastructure. Unlike proprietary alternatives, n8n can be self-hosted on your own servers, supports 400+ native integrations, and includes advanced features like LangChain AI agents, custom JavaScript/Python execution, and sub-workflows.')
    lines.append('')
    lines.append('### Are these templates free to use?')
    lines.append('')
    lines.append('Yes, all templates in this repository are free and open-source under the MIT license. You are free to download, modify, and use them in both personal and commercial projects.')
    lines.append('')
    lines.append('### Can I contribute my own templates?')
    lines.append('')
    lines.append('Contributions are welcome! If you have built an n8n workflow that solves a useful problem, please submit a pull request. Make sure to export your workflow without credentials or sensitive data, place it in the appropriate category folder, and run the sync script.')
    lines.append('')
    lines.append('### What AI models are supported in these templates?')
    lines.append('')
    lines.append('The AI templates in this collection support a wide range of LLM providers including OpenAI (GPT-4o, GPT-4, o3-mini), Anthropic (Claude 3.5 Sonnet, Claude 3 Opus), Google (Gemini 1.5 Pro/Flash, Gemini 2.0), Mistral AI, DeepSeek, and locally hosted models via Ollama. You can easily swap the model provider in any template by changing the LLM sub-node.')
    lines.append('')
    lines.append('### How often is this repository updated?')
    lines.append('')
    lines.append('This repository is actively maintained with new templates added regularly. Star and watch the repository to stay updated with the latest community workflows.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Contributing')
    lines.append('')
    lines.append('Contributions are welcome! Please read the contribution guidelines before submitting a pull request:')
    lines.append('')
    lines.append('1. Export your workflow from n8n as a `.json` file.')
    lines.append('2. **Remove all credentials, API keys, and sensitive data** before committing.')
    lines.append('3. Place the file in the appropriate category directory.')
    lines.append('4. Submit a pull request with a clear description of what the workflow does.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('### Sponsors')
    lines.append('')
    lines.append('Support this project and get your company or tool featured here.')
    lines.append('')
    lines.append('<a href="https://github.com/sponsors/ahmedfawzyjr">')
    lines.append('  <img src="https://img.shields.io/badge/Sponsor-n8n_Portal-ea4aaa?style=for-the-badge&logo=github-sponsors" alt="Sponsor this project" />')
    lines.append('</a>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Star History')
    lines.append('')
    lines.append('If you find these templates helpful, please consider giving this repository a star!')
    lines.append('')
    lines.append('[![Star History Chart](https://api.star-history.com/svg?repos=ahmedfawzyjr/N8N-Templates&type=Date)](https://star-history.com/#ahmedfawzyjr/N8N-Templates&Date)')
    lines.append('')
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"README.md written successfully ({len(lines)} lines)")

def generate_docs_index(categories_data, total_templates, total_node_types=200):
    index_path = os.path.join(ROOT, 'docs', 'index.md')
    lines = []
    
    lines.append('---')
    lines.append('layout: default')
    lines.append(f'title: "n8n Portal — Curated Production Automation Templates Directory & AI Workflows"')
    lines.append(f'description: "Curated open-source directory of {total_templates}+ production-ready n8n automation templates. Instant copy-and-paste workflows for AI agents, RAG, Gmail, Telegram, Slack, and DevOps."')
    lines.append('---')
    lines.append('')
    
    # Hero Section
    lines.append('<section class="hero-section">')
    lines.append('  <h1 class="hero-title">')
    lines.append('    Production Automation &amp; AI Agents with <span class="text-gradient">n8n Portal</span>')
    lines.append('  </h1>')
    lines.append('  <p class="hero-subtitle">')
    lines.append('    Explore, inspect, and copy verified workflow templates for autonomous AI agents, RAG document intelligence, CRM pipelines, customer bots, and DevOps infrastructure.')
    lines.append('  </p>')
    lines.append('  <div class="hero-actions">')
    lines.append(f'    <a href="#explorer" class="btn-primary">{get_svg_icon("layers", size=16)} Browse {total_templates}+ Templates</a>')
    lines.append(f'    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-secondary">{get_svg_icon("zap", size=16)} Start n8n Cloud Trial</a>')
    lines.append(f'    <a href="https://github.com/ahmedfawzyjr/N8N-Templates" target="_blank" rel="noopener" class="btn-secondary">{get_svg_icon("github", size=16)} Star on GitHub</a>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Hero Stats Bento
    lines.append('<div class="stats-bento">')
    lines.append('  <div class="stat-box">')
    lines.append(f'    <div class="stat-icon">{get_svg_icon("layers", size=22)}</div>')
    lines.append(f'    <div class="stat-number">{total_templates}+</div>')
    lines.append('    <div class="stat-label">Production Workflows</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append(f'    <div class="stat-icon">{get_svg_icon("folder", size=22)}</div>')
    lines.append(f'    <div class="stat-number">{len(categories_data)}</div>')
    lines.append('    <div class="stat-label">Specialized Hubs</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append(f'    <div class="stat-icon">{get_svg_icon("plug", size=22)}</div>')
    lines.append(f'    <div class="stat-number">{total_node_types}+</div>')
    lines.append('    <div class="stat-label">Node Integrations</div>')
    lines.append('  </div>')
    lines.append('  <div class="stat-box">')
    lines.append(f'    <div class="stat-icon">{get_svg_icon("shield", size=22)}</div>')
    lines.append('    <div class="stat-number">100%</div>')
    lines.append('    <div class="stat-label">Free & MIT Licensed</div>')
    lines.append('  </div>')
    lines.append('</div>')
    lines.append('')
    
    # Interactive Explorer Section
    lines.append('<section id="explorer" class="explorer-section">')
    lines.append('  <div class="explorer-header">')
    lines.append('    <div class="search-command-bar">')
    lines.append('      <div class="search-input-wrapper">')
    lines.append(f'        <span class="search-icon-left">{get_svg_icon("search", size=18)}</span>')
    lines.append('        <input type="text" id="template-search-input" class="search-input" placeholder="Search workflows by integration (OpenAI, Gmail, Qdrant, Slack), title, or keyword..." aria-label="Search templates">')
    lines.append(f'        <button id="search-clear-btn" class="search-clear-btn" title="Clear search" aria-label="Clear search">{get_svg_icon("x", size=16)}</button>')
    lines.append('        <span class="search-shortcut-hint"><kbd>Ctrl</kbd> <kbd>K</kbd></span>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <!-- Category Filter Pills -->')
    lines.append('    <div class="filter-pills-scroll-wrapper">')
    lines.append('      <div class="filter-pills-scroll" id="category-pills-container">')
    lines.append('        <!-- Injected dynamically by app.js -->')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <!-- Secondary Filters & View Controls -->')
    lines.append('    <div class="filter-controls-row">')
    lines.append('      <div class="filter-secondary-group">')
    lines.append('        <div class="custom-select-wrapper">')
    lines.append('          <select id="department-filter-select" class="custom-select" aria-label="Filter by department">')
    lines.append('            <option value="all">All Departments</option>')
    lines.append('            <option value="marketing">Marketing</option>')
    lines.append('            <option value="sales">Sales</option>')
    lines.append('            <option value="engineering">Engineering</option>')
    lines.append('            <option value="security">Security</option>')
    lines.append('            <option value="hr">HR &amp; Recruiting</option>')
    lines.append('            <option value="support">Support</option>')
    lines.append('            <option value="finance">Finance</option>')
    lines.append('            <option value="executive">Executive</option>')
    lines.append('            <option value="operations">Operations</option>')
    lines.append('          </select>')
    lines.append('        </div>')
    lines.append('')
    lines.append('        <div class="custom-select-wrapper">')
    lines.append('          <select id="sort-by-select" class="custom-select" aria-label="Sort templates">')
    lines.append('            <option value="title-asc">Sort: Name (A to Z)</option>')
    lines.append('            <option value="title-desc">Sort: Name (Z to A)</option>')
    lines.append('            <option value="nodes-desc">Sort: Node Count (High to Low)</option>')
    lines.append('          </select>')
    lines.append('        </div>')
    lines.append('      </div>')
    lines.append('')
    lines.append('      <div class="filter-secondary-group">')
    lines.append('        <div class="view-toggle-btns">')
    lines.append(f'          <button id="view-grid-btn" class="view-btn active" title="Grid View">{get_svg_icon("grid", size=15)} <span>Grid</span></button>')
    lines.append(f'          <button id="view-table-btn" class="view-btn" title="Table View">{get_svg_icon("list", size=15)} <span>Table</span></button>')
    lines.append('        </div>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('')
    lines.append('    <div class="results-status-bar">')
    lines.append(f'      <span id="results-counter-text" class="results-counter">Showing <strong>{total_templates}</strong> of <strong>{total_templates}</strong> templates</span>')
    lines.append(f'      <button id="reset-filters-btn" class="reset-filters-btn">{get_svg_icon("x", size=14)} <span>Reset Filters</span></button>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('')
    lines.append('  <!-- Dynamic Template Cards Grid Container -->')
    lines.append('  <div id="templates-grid-container" class="templates-grid">')
    lines.append('    <!-- Cards rendered via JavaScript -->')
    lines.append('  </div>')
    lines.append('')
    lines.append('  <!-- Dynamic Template Table Container -->')
    lines.append('  <div id="templates-table-wrapper" class="templates-table-container">')
    lines.append('    <table class="modern-table">')
    lines.append('      <thead>')
    lines.append('        <tr>')
    lines.append('          <th>Workflow Name</th>')
    lines.append('          <th>Category</th>')
    lines.append('          <th>Department</th>')
    lines.append('          <th>Description</th>')
    lines.append('          <th>Actions</th>')
    lines.append('        </tr>')
    lines.append('      </thead>')
    lines.append('      <tbody id="templates-table-tbody">')
    lines.append('        <!-- Rows rendered via JavaScript -->')
    lines.append('      </tbody>')
    lines.append('    </table>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Categories Directory Bento Grid
    lines.append('<section id="categories" style="margin-top: 64px;">')
    lines.append('  <h2>Explore by Category Hub</h2>')
    lines.append('  <p>Deep-dive into 18 dedicated collections categorized for specific tools, platforms, and enterprise use-cases.</p>')
    lines.append('  <div class="categories-bento-grid">')
    for cat in categories_data:
        cfg = cat['config']
        lines.append(f'    <a href="{{{{ site.baseurl }}}}/categories/{cfg["slug"]}" class="category-bento-card" style="--cat-accent: {cfg["color"]};">')
        lines.append('      <div class="cat-card-header">')
        lines.append(f'        <span class="cat-card-icon">{get_svg_icon(cfg["icon"], size=22)}</span>')
        lines.append(f'        <span class="cat-card-count">{cat["count"]} templates</span>')
        lines.append('      </div>')
        lines.append(f'      <div class="cat-card-title">{cfg["name"]}</div>')
        lines.append(f'      <div class="cat-card-desc">{cfg["short_desc"]}</div>')
        lines.append('    </a>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Quickstart Guide
    lines.append('<section id="how-it-works" style="margin-top: 64px;">')
    lines.append('  <h2>Quickstart: Import Workflows in 4 Simple Steps</h2>')
    lines.append('  <p>How to deploy and customize any workflow template from this library inside n8n:</p>')
    lines.append('  <div class="steps-container">')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">01</div>')
    lines.append('      <div class="step-title">Choose Template</div>')
    lines.append('      <div class="step-text">Search the directory and select the workflow that fits your business goal.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">02</div>')
    lines.append('      <div class="step-title">Copy or Download</div>')
    lines.append('      <div class="step-text">Click "Copy JSON" for direct canvas clipboard import or download the .json file.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">03</div>')
    lines.append('      <div class="step-title">Paste into n8n</div>')
    lines.append('      <div class="step-text">Open your n8n canvas (Cloud or self-hosted) and press Ctrl+V to paste the workflow.</div>')
    lines.append('    </div>')
    lines.append('    <div class="step-card">')
    lines.append('      <div class="step-number">04</div>')
    lines.append('      <div class="step-title">Connect &amp; Deploy</div>')
    lines.append('      <div class="step-text">Attach your API credentials to the nodes, run a test execution, and activate!</div>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # Why n8n Bento Section
    lines.append('<section style="margin-top: 64px;">')
    lines.append('  <h2>Why Automate with n8n?</h2>')
    lines.append('  <p>n8n is the premier source-available workflow automation engine for modern technical teams:</p>')
    lines.append('  <div class="features-bento">')
    lines.append('    <div class="feature-box">')
    lines.append(f'      <div class="feature-box-icon">{get_svg_icon("shield", size=22)}</div>')
    lines.append('      <div class="feature-box-title">Self-Hostable &amp; Private</div>')
    lines.append('      <p>Host on your own VPC, Docker, or Kubernetes clusters. Total control over your proprietary data and API keys.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append(f'      <div class="feature-box-icon">{get_svg_icon("bot", size=22)}</div>')
    lines.append('      <div class="feature-box-title">Native AI &amp; LangChain</div>')
    lines.append('      <p>Built-in nodes for Autonomous Agents, LLM tool calling, Vector Stores (Qdrant, Pinecone), and Memory.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append(f'      <div class="feature-box-icon">{get_svg_icon("plug", size=22)}</div>')
    lines.append('      <div class="feature-box-title">400+ Native Integrations</div>')
    lines.append('      <p>Connect seamlessly to Slack, Google Workspace, GitHub, Postgres, HubSpot, Discord, Telegram, and custom APIs.</p>')
    lines.append('    </div>')
    lines.append('    <div class="feature-box">')
    lines.append(f'      <div class="feature-box-icon">{get_svg_icon("terminal", size=22)}</div>')
    lines.append('      <div class="feature-box-title">Custom JS &amp; Python Code</div>')
    lines.append('      <p>Execute custom JavaScript and Python scripts directly within nodes for advanced data transformations.</p>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    # FAQ Section
    lines.append('<section id="faq" style="margin-top: 64px;">')
    lines.append('  <h2>Frequently Asked Questions</h2>')
    lines.append('  <p>Everything you need to know about importing and executing these templates.</p>')
    lines.append('  <div class="faq-container">')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>How do I import a workflow directly into n8n?</span>')
    lines.append(f'        <span class="faq-chevron">{get_svg_icon("chevron-down", size=18)}</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Click the "Copy JSON" button on any template card. Then open your n8n workflow canvas in your browser and press <code>Ctrl + V</code> (or <code>Cmd + V</code> on macOS). The nodes and connections will appear immediately on your canvas!')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Are these templates compatible with n8n Cloud and self-hosted?</span>')
    lines.append(f'        <span class="faq-chevron">{get_svg_icon("chevron-down", size=18)}</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes, all 350+ templates in this repository are standard n8n JSON exports compatible with n8n Cloud and self-hosted n8n (Docker / npm / Kubernetes) running version 1.x or later.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Do I need to enter my own API keys?</span>')
    lines.append(f'        <span class="faq-chevron">{get_svg_icon("chevron-down", size=18)}</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes. All templates in this repository are completely sanitized with zero hardcoded API keys or sensitive credentials. After importing, open the credential dropdown on each node (e.g. OpenAI, Telegram, Gmail) and attach your own credentials.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>Can I use these templates in commercial client projects?</span>')
    lines.append(f'        <span class="faq-chevron">{get_svg_icon("chevron-down", size=18)}</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        Yes! All templates in this repository are released under the open-source MIT license. You can freely use, modify, and integrate them into internal systems or client solutions.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('    <div class="faq-item">')
    lines.append('      <div class="faq-question">')
    lines.append('        <span>What AI models and providers can I use?</span>')
    lines.append(f'        <span class="faq-chevron">{get_svg_icon("chevron-down", size=18)}</span>')
    lines.append('      </div>')
    lines.append('      <div class="faq-answer">')
    lines.append('        The AI templates support OpenAI (GPT-4o, o3-mini), Anthropic (Claude 3.5 Sonnet), Google Gemini, DeepSeek, Mistral, and local Ollama models. Simply swap the Model sub-node to connect any provider you prefer.')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('  </div>')
    lines.append('</section>')
    lines.append('')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print("docs/index.md written successfully")

def generate_docs_categories(categories_data):
    docs_cat_dir = os.path.join(ROOT, 'docs', 'categories')
    os.makedirs(docs_cat_dir, exist_ok=True)
    
    for cat in categories_data:
        cfg = cat['config']
        cat_file = os.path.join(docs_cat_dir, f"{cfg['slug']}.md")
        lines = []
        
        lines.append('---')
        lines.append('layout: default')
        lines.append(f'title: "{cfg["name"]} Templates | n8n Portal"')
        lines.append(f'description: "{cat["count"]} n8n {cfg["name"].lower()} templates. {cfg["short_desc"]}"')
        lines.append('---')
        lines.append('')
        
        # Breadcrumbs
        lines.append('<nav style="margin-bottom: 24px; font-size: 0.9rem; color: var(--text-muted); display: flex; align-items: center; gap: 8px;">')
        lines.append('  <a href="{{ site.baseurl }}/" style="color: var(--text-secondary);">Home</a>')
        lines.append('  <span style="opacity: 0.4;">/</span>')
        lines.append('  <a href="{{ site.baseurl }}/#categories" style="color: var(--text-secondary);">Categories</a>')
        lines.append('  <span style="opacity: 0.4;">/</span>')
        lines.append(f'  <span style="color: var(--n8n-coral); font-weight: 600;">{cfg["name"]}</span>')
        lines.append('</nav>')
        lines.append('')
        
        # Category Hero Banner
        lines.append('<div style="background: var(--surface-glass-card); border: 1px solid var(--border-glass); border-radius: var(--radius-xl); padding: 36px 32px; box-shadow: var(--shadow-glass); position: relative; overflow: hidden; margin-bottom: 40px;">')
        lines.append(f'  <div style="position: absolute; top: 0; left: 0; width: 100%; height: 4px; background: {cfg["color"]};"></div>')
        lines.append('  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;">')
        lines.append('    <div style="display: flex; align-items: center; gap: 14px;">')
        lines.append(f'      <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; color: {cfg["color"]};">{get_svg_icon(cfg["icon"], size=24)}</div>')
        lines.append(f'      <h1 style="margin: 0; font-size: clamp(1.8rem, 4vw, 2.6rem);">{cfg["name"]}</h1>')
        lines.append('    </div>')
        lines.append(f'    <span class="nav-badge-pill" style="font-size: 0.85rem; padding: 6px 14px;">{cat["count"]} Workflows</span>')
        lines.append('  </div>')
        lines.append(f'  <p style="font-size: 1.1rem; color: var(--text-secondary); max-width: 820px; line-height: 1.6; margin-bottom: 24px;">{cfg["intro"]}</p>')
        lines.append('  <div style="display: flex; gap: 12px; flex-wrap: wrap;">')
        lines.append(f'    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-primary">{get_svg_icon("zap", size=16)} Start n8n Cloud Trial</a>')
        lines.append(f'    <a href="{{{{ site.baseurl }}}}/?cat={cfg["slug"]}#explorer" class="btn-secondary">{get_svg_icon("layers", size=16)} Filter in Explorer</a>')
        lines.append('  </div>')
        lines.append('</div>')
        lines.append('')
        
        # Category Templates Grid
        lines.append(f'<h2>All {cat["count"]} {cfg["name"]} Workflows</h2>')
        lines.append(f'<p>Download JSON files or copy directly to your clipboard for instant n8n canvas import.</p>')
        lines.append('')
        
        lines.append('<div class="templates-grid" style="margin-top: 24px;">')
        for t in cat['templates']:
            node_pills = ''.join([f'<span class="node-tag">{n}</span>' for n in t['node_names'][:3]])
            more_nodes = f'<span class="node-tag">+{len(t["node_names"]) - 3}</span>' if len(t['node_names']) > 3 else ''
            
            lines.append('  <div class="template-card">')
            lines.append('    <div class="template-card-inner">')
            lines.append('      <div class="card-top-row">')
            lines.append(f'        <span class="category-chip">{get_svg_icon(cfg["icon"], size=13)} {cfg["name"]}</span>')
            lines.append(f'        <span class="dept-badge">{t["dept"]}</span>')
            lines.append('      </div>')
            lines.append(f'      <h3 class="card-title" onclick="window.n8nExplorer.openModal(\'{t["id"]}\')">{t["title"]}</h3>')
            lines.append(f'      <p class="card-desc">{t["desc"]}</p>')
            lines.append('      <div class="card-nodes-list">')
            lines.append(f'        {node_pills} {more_nodes}')
            lines.append('      </div>')
            lines.append('      <div class="card-actions">')
            lines.append(f'        <button class="btn-card-primary" onclick="window.n8nExplorer.copyForN8n(\'{t["id"]}\')">{get_svg_icon("copy", size=14)} <span>Copy JSON</span></button>')
            lines.append(f'        <button class="btn-card-icon" onclick="window.n8nExplorer.openModal(\'{t["id"]}\')" title="Inspect workflow details" aria-label="Inspect workflow">{get_svg_icon("eye", size=16)}</button>')
            lines.append(f'        <a href="{t["gh_link"]}" target="_blank" rel="noopener" class="btn-card-icon" title="View on GitHub" aria-label="View on GitHub">{get_svg_icon("external-link", size=15)}</a>')
            lines.append('      </div>')
            lines.append('    </div>')
            lines.append('  </div>')
        lines.append('</div>')
        lines.append('')
        
        # Category switcher footer
        lines.append('<div style="margin-top: 64px; padding-top: 32px; border-top: 1px solid var(--border-glass);">')
        lines.append('  <h3>Explore Other Category Hubs</h3>')
        lines.append('  <div class="filter-pills-scroll" style="margin-top: 16px;">')
        for other_cat in categories_data:
            o_cfg = other_cat['config']
            active_style = 'style="border-color: var(--n8n-coral);"' if o_cfg['slug'] == cfg['slug'] else ''
            lines.append(f'    <a href="{{{{ site.baseurl }}}}/categories/{o_cfg["slug"]}" class="filter-pill" {active_style}>{get_svg_icon(o_cfg["icon"], size=14)} <span>{o_cfg["name"]}</span> <span class="pill-count">{other_cat["count"]}</span></a>')
        lines.append('  </div>')
        lines.append('</div>')
        lines.append('')
        
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Generated docs/categories/{cfg['slug']}.md ({cat['count']} templates)")

def generate_unique_nodes_txt(node_counter, total_workflows):
    txt_path = os.path.join(ROOT, 'ALL_unique_nodes.txt')
    lines = []
    
    lines.append('# n8n Portal - Complete Unique Nodes Catalog')
    lines.append(f'Total Workflows Analyzed: {total_workflows}')
    lines.append(f'Total Unique Node Types: {len(node_counter)}')
    lines.append(f'Total Node Instances in Repository: {sum(node_counter.values())}')
    lines.append('=' * 80)
    lines.append('')
    lines.append('## All Unique Node Types (Alphabetical Order)')
    lines.append('')
    for node_type in sorted(node_counter.keys()):
        lines.append(f'- {node_type} (used in {node_counter[node_type]} nodes)')
        
    lines.append('')
    lines.append('=' * 80)
    lines.append('')
    lines.append('## Top 40 Most Frequently Used Node Types')
    lines.append('')
    for rank, (ntype, count) in enumerate(node_counter.most_common(40), 1):
        lines.append(f'{rank:2d}. {ntype:65s} : {count:4d} instances')
        
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"ALL_unique_nodes.txt generated successfully ({len(node_counter)} unique node types)")

if __name__ == '__main__':
    main()
