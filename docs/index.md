---
layout: default
title: "n8n Portal — Curated Production Automation Templates Directory & AI Workflows"
description: "Curated open-source directory of 358+ production-ready n8n automation templates. Instant copy-and-paste workflows for AI agents, RAG, Gmail, Telegram, Slack, and DevOps."
---

<section class="hero-section">
  <h1 class="hero-title">
    Production Automation &amp; AI Agents with <span class="text-gradient">n8n Portal</span>
  </h1>
  <p class="hero-subtitle">
    Explore, inspect, and copy verified workflow templates for autonomous AI agents, RAG document intelligence, CRM pipelines, customer bots, and DevOps infrastructure.
  </p>
  <div class="hero-actions">
    <a href="#explorer" class="btn-primary"><svg class="svg-icon " width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg> Browse 358+ Templates</a>
    <a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" target="_blank" rel="noopener" class="btn-secondary"><svg class="svg-icon " width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg> Start n8n Cloud Trial</a>
    <a href="https://github.com/ahmedfawzyjr/N8N-Templates" target="_blank" rel="noopener" class="btn-secondary"><svg class="svg-icon " width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg> Star on GitHub</a>
  </div>
</section>

<div class="stats-bento">
  <div class="stat-box">
    <div class="stat-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg></div>
    <div class="stat-number">358+</div>
    <div class="stat-label">Production Workflows</div>
  </div>
  <div class="stat-box">
    <div class="stat-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/></svg></div>
    <div class="stat-number">18</div>
    <div class="stat-label">Specialized Hubs</div>
  </div>
  <div class="stat-box">
    <div class="stat-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 2v6"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg></div>
    <div class="stat-number">209+</div>
    <div class="stat-label">Node Integrations</div>
  </div>
  <div class="stat-box">
    <div class="stat-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
    <div class="stat-number">100%</div>
    <div class="stat-label">Free & MIT Licensed</div>
  </div>
</div>

<section id="explorer" class="explorer-section">
  <div class="explorer-header">
    <div class="search-command-bar">
      <div class="search-input-wrapper">
        <span class="search-icon-left"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></span>
        <input type="text" id="template-search-input" class="search-input" placeholder="Search workflows by integration (OpenAI, Gmail, Qdrant, Slack), title, or keyword..." aria-label="Search templates">
        <button id="search-clear-btn" class="search-clear-btn" title="Clear search" aria-label="Clear search"><svg class="svg-icon " width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></button>
        <span class="search-shortcut-hint"><kbd>Ctrl</kbd> <kbd>K</kbd></span>
      </div>
    </div>

    <!-- Category Filter Pills -->
    <div class="filter-pills-scroll-wrapper">
      <div class="filter-pills-scroll" id="category-pills-container">
        <!-- Injected dynamically by app.js -->
      </div>
    </div>

    <!-- Secondary Filters & View Controls -->
    <div class="filter-controls-row">
      <div class="filter-secondary-group">
        <div class="custom-select-wrapper">
          <select id="department-filter-select" class="custom-select" aria-label="Filter by department">
            <option value="all">All Departments</option>
            <option value="marketing">Marketing</option>
            <option value="sales">Sales</option>
            <option value="engineering">Engineering</option>
            <option value="security">Security</option>
            <option value="hr">HR &amp; Recruiting</option>
            <option value="support">Support</option>
            <option value="finance">Finance</option>
            <option value="executive">Executive</option>
            <option value="operations">Operations</option>
          </select>
        </div>

        <div class="custom-select-wrapper">
          <select id="sort-by-select" class="custom-select" aria-label="Sort templates">
            <option value="title-asc">Sort: Name (A to Z)</option>
            <option value="title-desc">Sort: Name (Z to A)</option>
            <option value="nodes-desc">Sort: Node Count (High to Low)</option>
          </select>
        </div>
      </div>

      <div class="filter-secondary-group">
        <div class="view-toggle-btns">
          <button id="view-grid-btn" class="view-btn active" title="Grid View"><svg class="svg-icon " width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg> <span>Grid</span></button>
          <button id="view-table-btn" class="view-btn" title="Table View"><svg class="svg-icon " width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" x2="21" y1="6" y2="6"/><line x1="8" x2="21" y1="12" y2="12"/><line x1="8" x2="21" y1="18" y2="18"/><line x1="3" x2="3.01" y1="6" y2="6"/><line x1="3" x2="3.01" y1="12" y2="12"/><line x1="3" x2="3.01" y1="18" y2="18"/></svg> <span>Table</span></button>
        </div>
      </div>
    </div>

    <div class="results-status-bar">
      <span id="results-counter-text" class="results-counter">Showing <strong>358</strong> of <strong>358</strong> templates</span>
      <button id="reset-filters-btn" class="reset-filters-btn"><svg class="svg-icon " width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg> <span>Reset Filters</span></button>
    </div>
  </div>

  <!-- Dynamic Template Cards Grid Container -->
  <div id="templates-grid-container" class="templates-grid">
    <!-- Cards rendered via JavaScript -->
  </div>

  <!-- Dynamic Template Table Container -->
  <div id="templates-table-wrapper" class="templates-table-container">
    <table class="modern-table">
      <thead>
        <tr>
          <th>Workflow Name</th>
          <th>Category</th>
          <th>Department</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody id="templates-table-tbody">
        <!-- Rows rendered via JavaScript -->
      </tbody>
    </table>
  </div>
</section>

<section id="categories" style="margin-top: 64px;">
  <h2>Explore by Category Hub</h2>
  <p>Deep-dive into 18 dedicated collections categorized for specific tools, platforms, and enterprise use-cases.</p>
  <div class="categories-bento-grid">
    <a href="{{ site.baseurl }}/categories/gmail-email-automation" class="category-bento-card" style="--cat-accent: #EA4335;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></span>
        <span class="cat-card-count">26 templates</span>
      </div>
      <div class="cat-card-title">Gmail & Email Automation</div>
      <div class="cat-card-desc">AI email labeling, phishing detection, auto-reply drafts, and Outlook automation.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/telegram-bots" class="category-bento-card" style="--cat-accent: #229ED9;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></span>
        <span class="cat-card-count">26 templates</span>
      </div>
      <div class="cat-card-title">Telegram</div>
      <div class="cat-card-desc">AI chatbots with LangChain, voice-to-text in 55 languages, PDF chat, and Spotify integration.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/google-drive-sheets" class="category-bento-card" style="--cat-accent: #0F9D58;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" x2="2" y1="12" y2="12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><line x1="6" x2="6.01" y1="16" y2="16"/><line x1="10" x2="10.01" y1="16" y2="16"/></svg></span>
        <span class="cat-card-count">21 templates</span>
      </div>
      <div class="cat-card-title">Google Drive & Google Sheets</div>
      <div class="cat-card-desc">RAG chatbots for documents, OpenAI fine-tuning, lead qualification, and HR screening.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/wordpress" class="category-bento-card" style="--cat-accent: #21759B;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg></span>
        <span class="cat-card-count">6 templates</span>
      </div>
      <div class="cat-card-title">WordPress</div>
      <div class="cat-card-desc">AI blog categorization, content generation with DeepSeek, and chatbot embedding.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/pdf-document-processing" class="category-bento-card" style="--cat-accent: #DC2626;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg></span>
        <span class="cat-card-count">19 templates</span>
      </div>
      <div class="cat-card-title">PDF & Document Processing</div>
      <div class="cat-card-desc">PDF Q&A with source quoting, resume parsing, invoice extraction, and OCR pipelines.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/discord" class="category-bento-card" style="--cat-accent: #5865F2;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>
        <span class="cat-card-count">4 templates</span>
      </div>
      <div class="cat-card-title">Discord</div>
      <div class="cat-card-desc">AI Discord bot routing, daily comic translations, and YouTube summary sharing.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/database-storage" class="category-bento-card" style="--cat-accent: #3B82F6;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"/></svg></span>
        <span class="cat-card-count">5 templates</span>
      </div>
      <div class="cat-card-title">Database & Storage</div>
      <div class="cat-card-desc">Natural language SQL generation, PostgreSQL chat, and MongoDB recommendation engines.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/devops-server-automation" class="category-bento-card" style="--cat-accent: #6366F1;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg></span>
        <span class="cat-card-count">6 templates</span>
      </div>
      <div class="cat-card-title">DevOps / Server Automation</div>
      <div class="cat-card-desc">Disk space monitoring, Docker controller webhooks, Linux updates, and server health checks.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/airtable" class="category-bento-card" style="--cat-accent: #F59E0B;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/><path d="M9 3v18"/><path d="M15 3v18"/></svg></span>
        <span class="cat-card-count">5 templates</span>
      </div>
      <div class="cat-card-title">Airtable</div>
      <div class="cat-card-desc">AI agents querying Airtable, meeting notes sync from Fireflies, and Obsidian integration.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/notion" class="category-bento-card" style="--cat-accent: #64748B;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></span>
        <span class="cat-card-count">10 templates</span>
      </div>
      <div class="cat-card-title">Notion</div>
      <div class="cat-card-desc">Customer feedback logging, AI paper summaries, competitor research, and task generation.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/slack" class="category-bento-card" style="--cat-accent: #4A154B;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></span>
        <span class="cat-card-count">9 templates</span>
      </div>
      <div class="cat-card-title">Slack</div>
      <div class="cat-card-desc">Gemini AI Slack bots, Linear ticketing sync, info monitoring, and daily digests.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/openai-llms" class="category-bento-card" style="--cat-accent: #10A37F;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></span>
        <span class="cat-card-count">93 templates</span>
      </div>
      <div class="cat-card-title">OpenAI & LLMs</div>
      <div class="cat-card-desc">Autonomous agents, LangChain tool calling, multi-agent evaluation, lead scoring, and vision pipelines.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/whatsapp" class="category-bento-card" style="--cat-accent: #25D366;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
        <span class="cat-card-count">8 templates</span>
      </div>
      <div class="cat-card-title">WhatsApp</div>
      <div class="cat-card-desc">WhatsApp chatbots, meeting prep with Apify, lead capture, and payment reminders.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/social-media" class="category-bento-card" style="--cat-accent: #E1306C;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg></span>
        <span class="cat-card-count">20 templates</span>
      </div>
      <div class="cat-card-title">Instagram, Twitter, Social Media</div>
      <div class="cat-card-desc">Omnichannel repurposing, Instagram DM AI inbox, YouTube transcription, and competitor monitoring.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/other-integrations" class="category-bento-card" style="--cat-accent: #8B5CF6;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 2v6"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg></span>
        <span class="cat-card-count">47 templates</span>
      </div>
      <div class="cat-card-title">Other Integrations & Use Cases</div>
      <div class="cat-card-desc">Web scraping, e-commerce workflows, Mattermost integration, AWS analysis, and webhook pipelines.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/forms-surveys" class="category-bento-card" style="--cat-accent: #06B6D4;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11 3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span>
        <span class="cat-card-count">4 templates</span>
      </div>
      <div class="cat-card-title">Forms & Surveys</div>
      <div class="cat-card-desc">Conversational AI interviews, appointment qualification, and automated survey analysis.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/ai-research-rag" class="category-bento-card" style="--cat-accent: #EC4899;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 2v7.31"/><path d="M14 2v7.31"/><path d="M8.5 2h7"/><path d="M14 9.3 20.7 20.3c.7 1.1-.1 2.7-1.4 2.7H4.7c-1.3 0-2.1-1.6-1.4-2.7L10 9.3"/><path d="M6.3 17h11.4"/></svg></span>
        <span class="cat-card-count">45 templates</span>
      </div>
      <div class="cat-card-title">AI Research, RAG & Data Analysis</div>
      <div class="cat-card-desc">Deep research agents, vector database RAG, financial document analysis, and web scraping pipelines.</div>
    </a>
    <a href="{{ site.baseurl }}/categories/hr-recruitment" class="category-bento-card" style="--cat-accent: #14B8A6;">
      <div class="cat-card-header">
        <span class="cat-card-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
        <span class="cat-card-count">4 templates</span>
      </div>
      <div class="cat-card-title">HR & Recruitment</div>
      <div class="cat-card-desc">AI CV screening, BambooHR policy chatbots, job description generation, and IT helpdesk bots.</div>
    </a>
  </div>
</section>

<section id="how-it-works" style="margin-top: 64px;">
  <h2>Quickstart: Import Workflows in 4 Simple Steps</h2>
  <p>How to deploy and customize any workflow template from this library inside n8n:</p>
  <div class="steps-container">
    <div class="step-card">
      <div class="step-number">01</div>
      <div class="step-title">Choose Template</div>
      <div class="step-text">Search the directory and select the workflow that fits your business goal.</div>
    </div>
    <div class="step-card">
      <div class="step-number">02</div>
      <div class="step-title">Copy or Download</div>
      <div class="step-text">Click "Copy JSON" for direct canvas clipboard import or download the .json file.</div>
    </div>
    <div class="step-card">
      <div class="step-number">03</div>
      <div class="step-title">Paste into n8n</div>
      <div class="step-text">Open your n8n canvas (Cloud or self-hosted) and press Ctrl+V to paste the workflow.</div>
    </div>
    <div class="step-card">
      <div class="step-number">04</div>
      <div class="step-title">Connect &amp; Deploy</div>
      <div class="step-text">Attach your API credentials to the nodes, run a test execution, and activate!</div>
    </div>
  </div>
</section>

<section style="margin-top: 64px;">
  <h2>Why Automate with n8n?</h2>
  <p>n8n is the premier source-available workflow automation engine for modern technical teams:</p>
  <div class="features-bento">
    <div class="feature-box">
      <div class="feature-box-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
      <div class="feature-box-title">Self-Hostable &amp; Private</div>
      <p>Host on your own VPC, Docker, or Kubernetes clusters. Total control over your proprietary data and API keys.</p>
    </div>
    <div class="feature-box">
      <div class="feature-box-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg></div>
      <div class="feature-box-title">Native AI &amp; LangChain</div>
      <p>Built-in nodes for Autonomous Agents, LLM tool calling, Vector Stores (Qdrant, Pinecone), and Memory.</p>
    </div>
    <div class="feature-box">
      <div class="feature-box-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 2v6"/><path d="M18 8v5a6 6 0 0 1-12 0V8z"/></svg></div>
      <div class="feature-box-title">400+ Native Integrations</div>
      <p>Connect seamlessly to Slack, Google Workspace, GitHub, Postgres, HubSpot, Discord, Telegram, and custom APIs.</p>
    </div>
    <div class="feature-box">
      <div class="feature-box-icon"><svg class="svg-icon " width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/></svg></div>
      <div class="feature-box-title">Custom JS &amp; Python Code</div>
      <p>Execute custom JavaScript and Python scripts directly within nodes for advanced data transformations.</p>
    </div>
  </div>
</section>

<section id="faq" style="margin-top: 64px;">
  <h2>Frequently Asked Questions</h2>
  <p>Everything you need to know about importing and executing these templates.</p>
  <div class="faq-container">
    <div class="faq-item">
      <div class="faq-question">
        <span>How do I import a workflow directly into n8n?</span>
        <span class="faq-chevron"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>
      </div>
      <div class="faq-answer">
        Click the "Copy JSON" button on any template card. Then open your n8n workflow canvas in your browser and press <code>Ctrl + V</code> (or <code>Cmd + V</code> on macOS). The nodes and connections will appear immediately on your canvas!
      </div>
    </div>
    <div class="faq-item">
      <div class="faq-question">
        <span>Are these templates compatible with n8n Cloud and self-hosted?</span>
        <span class="faq-chevron"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>
      </div>
      <div class="faq-answer">
        Yes, all 350+ templates in this repository are standard n8n JSON exports compatible with n8n Cloud and self-hosted n8n (Docker / npm / Kubernetes) running version 1.x or later.
      </div>
    </div>
    <div class="faq-item">
      <div class="faq-question">
        <span>Do I need to enter my own API keys?</span>
        <span class="faq-chevron"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>
      </div>
      <div class="faq-answer">
        Yes. All templates in this repository are completely sanitized with zero hardcoded API keys or sensitive credentials. After importing, open the credential dropdown on each node (e.g. OpenAI, Telegram, Gmail) and attach your own credentials.
      </div>
    </div>
    <div class="faq-item">
      <div class="faq-question">
        <span>Can I use these templates in commercial client projects?</span>
        <span class="faq-chevron"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>
      </div>
      <div class="faq-answer">
        Yes! All templates in this repository are released under the open-source MIT license. You can freely use, modify, and integrate them into internal systems or client solutions.
      </div>
    </div>
    <div class="faq-item">
      <div class="faq-question">
        <span>What AI models and providers can I use?</span>
        <span class="faq-chevron"><svg class="svg-icon " width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg></span>
      </div>
      <div class="faq-answer">
        The AI templates support OpenAI (GPT-4o, o3-mini), Anthropic (Claude 3.5 Sonnet), Google Gemini, DeepSeek, Mistral, and local Ollama models. Simply swap the Model sub-node to connect any provider you prefer.
      </div>
    </div>
  </div>
</section>
