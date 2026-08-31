import os
import sys
import json
import re
import urllib.parse
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_CONFIG = [
    {
        "folder": "Gmail and Email Automation",
        "slug": "gmail-email-automation",
        "name": "Gmail & Email Automation",
        "heading": "What n8n templates are available for Gmail and email automation?",
        "intro": "This collection includes email automation templates for n8n covering Gmail, Outlook, and IMAP. Templates range from AI-powered email labeling and categorization with OpenAI to phishing detection, auto-reply drafting, and daily financial news delivery. Ideal for operations, security, and executive teams looking to streamline email management.",
        "short_desc": "AI-powered email labeling, phishing detection, auto-reply drafts, and Outlook automation."
    },
    {
        "folder": "Telegram",
        "slug": "telegram-bots",
        "name": "Telegram",
        "heading": "How can I automate Telegram bots with n8n?",
        "intro": "These n8n templates help you build AI-powered Telegram bots for voice-to-text transcription in 55+ languages, document Q&A, customer support, audio streaming, and personal assistants. Perfect for support teams, content creators, and developers deploying interactive chatbots.",
        "short_desc": "AI chatbots with LangChain, voice-to-text in 55 languages, PDF chat, and Spotify integration."
    },
    {
        "folder": "Google Drive and Google Sheets",
        "slug": "google-drive-sheets",
        "name": "Google Drive & Google Sheets",
        "heading": "What are the best n8n templates for Google Drive and Google Sheets?",
        "intro": "Automate Google Workspace with n8n templates for Google Drive and Google Sheets. Workflows include RAG chatbots for Google Docs, automated fine-tuning of OpenAI models, lead qualification, and dynamic data syncing between spreadsheets and third-party tools.",
        "short_desc": "RAG chatbots for documents, OpenAI fine-tuning, lead qualification, and HR screening."
    },
    {
        "folder": "WordPress",
        "slug": "wordpress",
        "name": "WordPress",
        "heading": "How do I automate WordPress with n8n?",
        "intro": "Streamline content management and publishing with these WordPress automation templates for n8n. Includes AI-driven blog post categorization, SEO content generation with DeepSeek and OpenAI, and embedding AI chatbots directly on WordPress sites.",
        "short_desc": "AI blog categorization, content generation with DeepSeek, and chatbot embedding."
    },
    {
        "folder": "PDF and Document Processing",
        "slug": "pdf-document-processing",
        "name": "PDF & Document Processing",
        "heading": "What n8n templates exist for PDF and document processing?",
        "intro": "Process documents at scale using n8n workflows for PDF parsing, OCR, and AI-driven data extraction. Templates cover conversational PDF chatbots with source citations, invoice parsing with LlamaParse and Mistral, and study note generation.",
        "short_desc": "PDF Q&A with source quoting, resume parsing, invoice extraction, and OCR pipelines."
    },
    {
        "folder": "Discord",
        "slug": "discord",
        "name": "Discord",
        "heading": "How can I automate Discord with n8n?",
        "intro": "Connect n8n to Discord for automated community management and content delivery. Templates include AI bot routing, scheduled sports match notifications, daily comic translations, and automated video summary sharing.",
        "short_desc": "AI-powered Discord bot routing, daily comic translations, and YouTube summary sharing."
    },
    {
        "folder": "Database and Storage",
        "slug": "database-storage",
        "name": "Database & Storage",
        "heading": "What are the best n8n database and storage automation templates?",
        "intro": "Bridge n8n with SQL and NoSQL databases. These templates include conversational interfaces for PostgreSQL and MongoDB, automated SQL query generation from schemas, and storage management workflows.",
        "short_desc": "Natural language SQL generation, PostgreSQL chat, and MongoDB recommendation engines."
    },
    {
        "folder": "DevOps",
        "slug": "devops-server-automation",
        "name": "DevOps / Server Automation",
        "heading": "What n8n templates are available for DevOps and server automation?",
        "intro": "Automate infrastructure monitoring and maintenance tasks with n8n. Templates include disk space watchdogs, Docker Compose controller webhooks, Linux remote updates, and scheduled server health checks.",
        "short_desc": "Disk space monitoring, Docker controller webhooks, Linux updates, and server health checks."
    },
    {
        "folder": "Airtable",
        "slug": "airtable",
        "name": "Airtable",
        "heading": "How do I automate Airtable with n8n?",
        "intro": "Leverage Airtable as a flexible backend for your automations. These n8n templates enable AI agents to chat with Airtable bases, synchronize project management and meeting notes from Fireflies.ai, and sync with Obsidian.",
        "short_desc": "AI agents querying Airtable, meeting notes sync from Fireflies, and Obsidian integration."
    },
    {
        "folder": "Notion",
        "slug": "notion",
        "name": "Notion",
        "heading": "What are the best n8n templates for Notion?",
        "intro": "Turn Notion into an automated knowledge hub. Workflows include archiving customer feedback, summarizing Hugging Face research papers, automating competitor intelligence with Exa.ai, and converting emails into tasks.",
        "short_desc": "Customer feedback logging, AI paper summaries, competitor research, and task generation."
    },
    {
        "folder": "Slack",
        "slug": "slack",
        "name": "Slack",
        "heading": "How can I automate Slack with n8n?",
        "intro": "Enhance team communication and operations with Slack automation workflows for n8n. Includes Gemini-powered Slack bots, automated customer support ticketing with Linear, information monitoring, and automated daily digest delivery.",
        "short_desc": "Gemini AI Slack bots, Linear ticketing sync, info monitoring, and daily digests."
    },
    {
        "folder": "OpenAI and LLMs",
        "slug": "openai-llms",
        "name": "OpenAI & LLMs",
        "heading": "What n8n templates are available for OpenAI, LLMs, and AI agents?",
        "intro": "This comprehensive collection features n8n templates for OpenAI, Anthropic Claude, Google Gemini, Mistral, Ollama, DeepSeek, and LangChain agents. Covers autonomous agents, multi-agent evaluation, tool calling, lead enrichment, image generation, audio transcription, and specialized assistants.",
        "short_desc": "Autonomous agents, LangChain tool calling, multi-agent evaluation, lead scoring, and vision pipelines."
    },
    {
        "folder": "WhatsApp",
        "slug": "whatsapp",
        "name": "WhatsApp",
        "heading": "How do I build WhatsApp chatbots with n8n?",
        "intro": "Build business automations and chatbots for WhatsApp using n8n. Templates cover automated sales meeting preparation with Apify, customer inquiry handling, multilingual lead capture, and escalating invoice reminders.",
        "short_desc": "WhatsApp chatbots, meeting prep with Apify, lead capture, and payment reminders."
    },
    {
        "folder": "Instagram Twitter Social Media",
        "slug": "social-media",
        "name": "Instagram, Twitter, Social Media",
        "heading": "What are the best n8n templates for social media automation?",
        "intro": "Automate social media marketing across Instagram, X (Twitter), LinkedIn, YouTube, TikTok, and Pinterest. Templates include AI content repurposing engines, Instagram DM inboxes with ManyChat, competitor engagement analysis, and scheduled auto-posting.",
        "short_desc": "Omnichannel repurposing, Instagram DM AI inbox, YouTube transcription, and competitor monitoring."
    },
    {
        "folder": "Other Integrations and Use Cases",
        "slug": "other-integrations",
        "name": "Other Integrations & Use Cases",
        "heading": "What other n8n integration templates are available?",
        "intro": "Explore diverse n8n workflows covering specialized APIs, web scraping, e-commerce, weather alerts, financial analysis, uptime monitoring, and multi-service connectors like Mattermost, Linear, AWS, and Stripe.",
        "short_desc": "Web scraping, e-commerce workflows, Mattermost integration, AWS analysis, and webhook pipelines."
    },
    {
        "folder": "Forms and Surveys",
        "slug": "forms-surveys",
        "name": "Forms & Surveys",
        "heading": "How do I automate forms and surveys with n8n?",
        "intro": "Create interactive and conversational form automations using n8n Forms. Templates feature conversational AI interviews, lead qualification with appointment booking, email subscription flows with Airtable, and automated survey feedback analysis.",
        "short_desc": "Conversational AI interviews, appointment qualification, and automated survey analysis."
    },
    {
        "folder": "AI Research RAG and Data Analysis",
        "slug": "ai-research-rag",
        "name": "AI Research, RAG, and Data Analysis",
        "heading": "What n8n templates exist for AI research, RAG, and data analysis?",
        "intro": "Advanced AI research and data analysis workflows utilizing vector databases (Qdrant, Pinecone, Milvus), autonomous research agents (Apify, o3, Perplexity, Tavily), financial document analyzers, Hacker News aggregators, and Google Analytics AI reporters.",
        "short_desc": "Deep research agents, vector database RAG, financial document analysis, and web scraping pipelines."
    },
    {
        "folder": "HR and Recruitment",
        "slug": "hr-recruitment",
        "name": "HR & Recruitment",
        "heading": "What n8n templates are available for HR and recruitment automation?",
        "intro": "Streamline talent acquisition and employee operations with HR automation templates for n8n. Features automated CV screening with OpenAI, BambooHR policy and benefits chatbots, job posting generation, and employee helpdesk bots with voice transcription.",
        "short_desc": "AI CV screening, BambooHR policy chatbots, job description generation, and IT helpdesk bots."
    }
]

def clean_title(fname):
    base = os.path.splitext(fname)[0]
    base = re.sub(r'^\s*-\s*💻\s*', '', base)
    base = re.sub(r'\s*-\s*-\s*', ' - ', base)
    base = re.sub(r'\s*–\s*', ' - ', base)
    base = re.sub(r'\s*—\s*', ' - ', base)
    base = re.sub(r'\s*-\s*S\s*', "'s ", base)
    base = re.sub(r'\s+', ' ', base).strip()
    return base

def infer_dept(cat, fname, json_data):
    fn_lower = fname.lower()
    cat_lower = cat.lower()
    
    if 'hr' in cat_lower or 'recruitment' in fn_lower or 'cv ' in fn_lower or 'bamboohr' in fn_lower or 'job' in fn_lower:
        return 'HR'
    if 'security' in fn_lower or 'phishing' in fn_lower or 'siem' in fn_lower or 'hmac' in fn_lower or 'guard' in fn_lower or 'audit' in fn_lower or 'vulnerability' in fn_lower:
        return 'Security'
    if 'sales' in fn_lower or 'lead' in fn_lower or 'crm' in fn_lower or 'cold email' in fn_lower or 'pipedrive' in fn_lower or 'hubspot' in fn_lower or 'deal' in fn_lower or 'invoice' in fn_lower or 'meeting' in fn_lower:
        return 'Sales'
    if 'marketing' in fn_lower or 'social' in cat_lower or 'instagram' in fn_lower or 'twitter' in fn_lower or 'seo' in fn_lower or 'content' in fn_lower or 'blog' in fn_lower or 'pinterest' in fn_lower or 'youtube' in fn_lower:
        return 'Marketing'
    if 'support' in fn_lower or 'ticket' in fn_lower or 'helpdesk' in fn_lower or 'customer' in fn_lower or 'feedback' in fn_lower or 'faq' in fn_lower or 'review' in fn_lower:
        return 'Support'
    if 'devops' in cat_lower or 'docker' in fn_lower or 'linux' in fn_lower or 'database' in cat_lower or 'postgres' in fn_lower or 'sql' in fn_lower or 'api' in fn_lower or 'github' in fn_lower or 'gitlab' in fn_lower:
        return 'Engineering'
    if 'executive' in fn_lower or 'ceo' in fn_lower or 'report' in fn_lower or 'kpi' in fn_lower or 'market news' in fn_lower or 'insights' in fn_lower:
        return 'Executive'
    if 'finance' in fn_lower or 'expense' in fn_lower or 'payment' in fn_lower or 'accounting' in fn_lower or 'rent' in fn_lower:
        return 'Finance'
    return 'Ops'

def generate_desc(cat, fname, json_data):
    title = clean_title(fname)
    nodes = json_data.get('nodes', [])
    node_types = [n.get('type', '') for n in nodes]
    node_names = [n.get('name', '') for n in nodes]
    
    integrations = []
    if any('openAi' in t or 'OpenAI' in n for t, n in zip(node_types, node_names)):
        integrations.append('OpenAI')
    if any('google' in t.lower() or 'Google' in n for t, n in zip(node_types, node_names)):
        integrations.append('Google Workspace')
    if any('qdrant' in t.lower() or 'Qdrant' in n for t, n in zip(node_types, node_names)):
        integrations.append('Qdrant')
    if any('telegram' in t.lower() or 'Telegram' in n for t, n in zip(node_types, node_names)):
        integrations.append('Telegram')
    if any('slack' in t.lower() or 'Slack' in n for t, n in zip(node_types, node_names)):
        integrations.append('Slack')
    if any('airtable' in t.lower() or 'Airtable' in n for t, n in zip(node_types, node_names)):
        integrations.append('Airtable')
    if any('notion' in t.lower() or 'Notion' in n for t, n in zip(node_types, node_names)):
        integrations.append('Notion')
    if any('agent' in t.lower() or 'Agent' in n for t, n in zip(node_types, node_names)):
        integrations.append('AI Agent')
    
    int_str = f" using {', '.join(integrations[:3])}" if integrations else ""
    return f"Automated workflow for {title.lower()}{int_str}, streamlining execution and data processing."

def load_curated_metadata():
    meta = {}
    readme_path = os.path.join(ROOT, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('|') and '[' in line and ']' in line and not line.strip().startswith('| Title') and not line.strip().startswith('|---'):
                    parts = [p.strip() for p in line.strip().split('|')[1:-1]]
                    if len(parts) >= 4:
                        t, d, dep, link_md = parts[0], parts[1], parts[2], parts[3]
                        m = re.search(r'\(([^)]+)\)', link_md)
                        if m:
                            path = urllib.parse.unquote(m.group(1)).replace('/', os.sep)
                            fname = os.path.basename(path)
                            meta[fname] = {'title': t, 'desc': d, 'dept': dep}
    
    docs_cat = os.path.join(ROOT, 'docs', 'categories')
    if os.path.exists(docs_cat):
        for cf in os.listdir(docs_cat):
            if cf.endswith('.md'):
                with open(os.path.join(docs_cat, cf), 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.strip().startswith('|') and '[' in line and not line.strip().startswith('| Template') and not line.strip().startswith('|---'):
                            parts = [p.strip() for p in line.strip().split('|')[1:-1]]
                            if len(parts) >= 3:
                                tmpl_md, d, dep = parts[0], parts[1], parts[2]
                                m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', tmpl_md)
                                if m:
                                    t = m.group(1)
                                    path = urllib.parse.unquote(m.group(2)).replace('/', os.sep)
                                    fname = os.path.basename(path)
                                    if fname not in meta:
                                        meta[fname] = {'title': t, 'desc': d, 'dept': dep}
    return meta

def main():
    curated = load_curated_metadata()
    
    all_categories_data = []
    total_templates = 0
    node_counter = Counter()
    
    for cfg in CATEGORY_CONFIG:
        folder = cfg['folder']
        cat_dir = os.path.join(ROOT, folder)
        if not os.path.exists(cat_dir):
            print(f"Warning: directory not found: {cat_dir}")
            continue
            
        json_files = sorted([f for f in os.listdir(cat_dir) if f.endswith('.json')])
        templates_in_cat = []
        
        for f in json_files:
            total_templates += 1
            fpath = os.path.join(cat_dir, f)
            with open(fpath, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
            
            for node in data.get('nodes', []):
                ntype = node.get('type')
                if ntype:
                    node_counter[ntype] += 1
            
            clean_name = clean_title(f)
            
            if f in curated:
                t_info = curated[f]
                title = t_info['title'] or clean_name
                desc = t_info['desc']
                dept = t_info['dept']
            else:
                title = clean_name
                desc = generate_desc(folder, f, data)
                dept = infer_dept(folder, f, data)
            
            desc = desc.replace('|', '/').replace('\n', ' ').strip()
            title = title.replace('|', '/').replace('\n', ' ').strip()
            
            enc_folder = urllib.parse.quote(folder)
            enc_file = urllib.parse.quote(f)
            readme_table_link = f"[Link to Template]({enc_folder}/{enc_file})"
            gh_link = f"https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/{enc_folder}/{enc_file}"
            
            templates_in_cat.append({
                'filename': f,
                'title': title,
                'desc': desc,
                'dept': dept,
                'readme_link': readme_table_link,
                'gh_link': gh_link,
                'clean_name': clean_name
            })
            
        templates_in_cat.sort(key=lambda x: x['title'].lower())
        
        all_categories_data.append({
            'config': cfg,
            'templates': templates_in_cat,
            'count': len(templates_in_cat)
        })

    print(f"Total Categories: {len(all_categories_data)}, Total Templates: {total_templates}")

    generate_readme(all_categories_data, total_templates)
    generate_docs_index(all_categories_data, total_templates)
    generate_docs_categories(all_categories_data)
    generate_unique_nodes_txt(node_counter, total_templates)
    
    print("All documentation, category files, and unique node references synchronized!")

def generate_readme(categories_data, total_templates):
    readme_path = os.path.join(ROOT, 'README.md')
    lines = []
    
    lines.append('# Awesome n8n Templates [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)')
    lines.append('')
    lines.append(f'> A curated list of {total_templates}+ awesome n8n workflow templates, integrations, and automation resources.')
    lines.append('')
    lines.append('Workflows are ready-to-import `.json` files. Download any template and import it directly into your n8n instance (Cloud or self-hosted). Always review and test imported templates before deploying them in production.')
    lines.append('')
    lines.append(f'[![Templates](https://img.shields.io/badge/Templates-{total_templates}+-blue.svg?style=flat-square)](#categories--template-list)')
    lines.append(f'[![Categories](https://img.shields.io/badge/Categories-18-green.svg?style=flat-square)](#categories--template-list)')
    lines.append('[![n8n](https://img.shields.io/badge/n8n-Compatible-FF6D5A.svg?style=flat-square&logo=n8n)](https://n8n.partnerlinks.io/h1pwwf5m4toe)')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('<p align="center">')
    lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">')
    lines.append('    <img src="https://img.shields.io/badge/n8n_Cloud-Start_Trial-orange?style=for-the-badge" alt="Start an n8n Cloud trial" />')
    lines.append('  </a>')
    lines.append('  <br />')
    lines.append('  <small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('</p>')
    lines.append('')
    lines.append('## Table of Contents')
    lines.append('')
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
    lines.append('<p align="center">')
    lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe">')
    lines.append('    <img src="https://img.shields.io/badge/n8n_Cloud-Start_Trial-orange?style=for-the-badge" alt="Start an n8n Cloud trial" />')
    lines.append('  </a>')
    lines.append('  <br />')
    lines.append('  <small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('</p>')
    lines.append('')
    lines.append('## FAQ')
    lines.append('')
    lines.append('### How do I import an n8n template from this repository?')
    lines.append('')
    lines.append('Download the `.json` file for any template you want to use. Open your n8n instance (either self-hosted or on [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe)), navigate to Workflows, click "Import from File," and select the downloaded JSON file. The workflow will appear in your editor ready for configuration. You will need to add your own credentials for each connected service before activating the workflow.')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('### What is n8n and why should I use it for automation?')
    lines.append('')
    lines.append('[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) is a fair-code, source-available workflow automation platform that gives you total control over your data and infrastructure. Unlike proprietary alternatives, n8n can be self-hosted on your own servers, supports 400+ native integrations, and includes advanced features like LangChain AI agents, custom JavaScript/Python execution, and sub-workflows.')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('### Are these templates free to use?')
    lines.append('')
    lines.append('Yes, all templates in this repository are free and open-source under the MIT license. You are free to download, modify, and use them in both personal and commercial projects.')
    lines.append('')
    lines.append('### Can I contribute my own templates?')
    lines.append('')
    lines.append('Contributions are welcome! If you have built an n8n workflow that solves a useful problem, please submit a pull request. Make sure to export your workflow without credentials or sensitive data, place it in the appropriate category folder, and add it to the README.')
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
    lines.append('4. Add an entry to the corresponding table in `README.md` with Title, Description, Department, and Link.')
    lines.append('5. Submit a pull request with a clear description of what the workflow does.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('### **Sponsors**')
    lines.append('')
    lines.append('Support this project and get your company or tool featured here.')
    lines.append('')
    lines.append('<a href="https://github.com/sponsors/ahmedfawzyjr">')
    lines.append('  <img src="https://img.shields.io/badge/Sponsor-Awesome_n8n_Templates-ea4aaa?style=for-the-badge&logo=github-sponsors" alt="Sponsor this project" />')
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

def generate_docs_index(categories_data, total_templates):
    index_path = os.path.join(ROOT, 'docs', 'index.md')
    lines = []
    
    lines.append('---')
    lines.append('layout: default')
    lines.append(f'title: "Awesome n8n Templates - {total_templates}+ Workflow Automations"')
    lines.append(f'description: "A curated collection of {total_templates}+ n8n automation workflow template files. AI agents, RAG chatbots, email automation, and more."')
    lines.append('---')
    lines.append('')
    lines.append('# Awesome n8n Templates')
    lines.append('')
    lines.append(f'**A curated collection of {total_templates}+ n8n workflow template files.** Browse examples covering Gmail, Telegram, OpenAI, WhatsApp, Slack, Discord, WordPress, Google Sheets, and dozens more platforms. Review, configure, and test each workflow before use.')
    lines.append('')
    lines.append('<a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial</a>')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('<div class="stats">')
    lines.append('  <div class="stat-card">')
    lines.append(f'    <span class="number">{total_templates}+</span>')
    lines.append('    <span class="label">Templates</span>')
    lines.append('  </div>')
    lines.append('  <div class="stat-card">')
    lines.append('    <span class="number">19k+</span>')
    lines.append('    <span class="label">GitHub Stars</span>')
    lines.append('  </div>')
    lines.append('  <div class="stat-card">')
    lines.append(f'    <span class="number">{len(categories_data)}</span>')
    lines.append('    <span class="label">Categories</span>')
    lines.append('  </div>')
    lines.append('  <div class="stat-card">')
    lines.append('    <span class="number">400+</span>')
    lines.append('    <span class="label">Integrations</span>')
    lines.append('  </div>')
    lines.append('</div>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Quick Start: How to Import These Templates')
    lines.append('')
    lines.append('1. **[Sign up for n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe)** (n8n Cloud trial available)')
    lines.append('   <br />')
    lines.append('   <small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('2. Download any `.json` template file from the [GitHub repository](https://github.com/ahmedfawzyjr/N8N-Templates)')
    lines.append('3. In n8n, go to **Workflows > Import from File** and select the JSON')
    lines.append('4. Configure your credentials for each connected service')
    lines.append('5. Activate the workflow and start automating')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Why n8n?')
    lines.append('')
    lines.append('[n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) is a fair-code, source-available workflow automation platform that connects services and systems. It can be self-hosted, giving you control over your data and infrastructure:')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('- **Fair-code, source-available, and self-hostable** -- run it on your own server with no vendor lock-in')
    lines.append('- **400+ built-in integrations** -- connect to virtually any service or API')
    lines.append('- **Visual workflow editor** -- build automations by dragging and dropping nodes')
    lines.append('- **AI-native capabilities** -- built-in support for OpenAI, Claude, Gemini, LangChain, and vector databases')
    lines.append('- **Deployment options** -- use the n8n Cloud trial or self-host Community Edition under n8n\'s license')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Browse Templates by Category')
    lines.append('')
    lines.append('<div class="category-grid">')
    lines.append('')
    for cat in categories_data:
        cfg = cat['config']
        lines.append('  <div class="category-card">')
        lines.append(f'    <h3><a href="{{{{ site.baseurl }}}}/categories/{cfg["slug"]}">{cfg["name"]}</a></h3>')
        lines.append(f'    <span class="count">{cat["count"]} templates</span>')
        lines.append(f'    <p>{cfg["short_desc"]}</p>')
        lines.append('  </div>')
        lines.append('')
    lines.append('</div>')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('## Frequently Asked Questions')
    lines.append('')
    lines.append('### How do I import a template into self-hosted n8n?')
    lines.append('')
    lines.append('Download the `.json` file from GitHub, open your self-hosted n8n instance, click **Workflows > Import from File**, and select the file. Configure any required credentials and save.')
    lines.append('')
    lines.append('### Can I use these templates with n8n Cloud?')
    lines.append('')
    lines.append('Yes. All templates are compatible with both self-hosted n8n and [n8n Cloud](https://n8n.partnerlinks.io/h1pwwf5m4toe). Import them the same way using the Import from File option.')
    lines.append('<br />')
    lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('')
    lines.append('### Do I need API keys to use the AI templates?')
    lines.append('')
    lines.append('Yes. For templates that use AI models (OpenAI, Anthropic, Gemini, Mistral, etc.), you will need an API key from the respective provider. Self-hosted models with Ollama do not require API keys.')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('<p style="text-align: center; margin: 40px 0;">')
    lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Get Started with n8n Cloud</a>')
    lines.append('  <br />')
    lines.append('  <small>* Referral link — this project receives a commission on eligible purchases.</small>')
    lines.append('</p>')
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
        lines.append(f'title: "{cfg["name"]} Templates for n8n | Awesome n8n Templates"')
        lines.append(f'description: "{cat["count"]} n8n {cfg["name"].lower()} templates. {cfg["short_desc"]}"')
        lines.append('---')
        lines.append('')
        lines.append(f'<nav class="breadcrumb"><a href="{{{{ site.baseurl }}}}/">Home</a> / {cfg["name"]}</nav>')
        lines.append('')
        lines.append(f'# {cfg["heading"]}')
        lines.append('')
        lines.append(f'{cfg["intro"]}')
        lines.append('')
        lines.append(f'<a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial -- Automate Your {cfg["name"]}</a>')
        lines.append('<br />')
        lines.append('<small>* Referral link — this project receives a commission on eligible purchases.</small>')
        lines.append('')
        lines.append('## Templates')
        lines.append('')
        lines.append('| Template | Description | Department |')
        lines.append('|---|---|---|')
        for t in cat['templates']:
            lines.append(f"| [{t['title']}]({t['gh_link']}) | {t['desc']} | {t['dept']} |")
        lines.append('')
        lines.append('## How to Use These Templates')
        lines.append('')
        lines.append('1. [Sign up for n8n](https://n8n.partnerlinks.io/h1pwwf5m4toe) (Cloud trial available)')
        lines.append('   <br />')
        lines.append('   <small>* Referral link — this project receives a commission on eligible purchases.</small>')
        lines.append('2. Download the JSON file for the template you want')
        lines.append('3. In n8n, go to **Workflows > Import from File**')
        lines.append('4. Connect your required credentials (API keys, OAuth tokens, etc.)')
        lines.append('5. Test the nodes and activate the workflow')
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('<p style="text-align: center; margin: 40px 0;">')
        lines.append('  <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial</a>')
        lines.append('  <br />')
        lines.append('  <small>* Referral link — this project receives a commission on eligible purchases.</small>')
        lines.append('</p>')
        lines.append('')
        lines.append('[Back to all categories]({{ site.baseurl }}/)')
        lines.append('')
        
        with open(cat_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"Generated docs/categories/{cfg['slug']}.md ({cat['count']} templates)")

def generate_unique_nodes_txt(node_counter, total_workflows):
    txt_path = os.path.join(ROOT, 'ALL_unique_nodes.txt')
    lines = []
    
    lines.append('# n8n Awesome Templates - Complete Unique Nodes Catalog')
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
