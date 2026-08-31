---
layout: default
title: "PDF & Document Processing Templates for n8n | Awesome n8n Templates"
description: "19 n8n pdf & document processing templates. PDF Q&A with source quoting, resume parsing, invoice extraction, and OCR pipelines."
---

<nav class="breadcrumb"><a href="{{ site.baseurl }}/">Home</a> / PDF & Document Processing</nav>

# What n8n templates exist for PDF and document processing?

Process documents at scale using n8n workflows for PDF parsing, OCR, and AI-driven data extraction. Templates cover conversational PDF chatbots with source citations, invoice parsing with LlamaParse and Mistral, and study note generation.

<a href="https://n8n.partnerlinks.io/h1pwwf5m4toe" class="cta-button">Start an n8n Cloud Trial -- Automate Your PDF & Document Processing</a>
<br />
<small>* Referral link — this project receives a commission on eligible purchases.</small>

## Templates

| Template | Description | Department |
|---|---|---|
| [AI-Powered Multi-Engine OCR and Document Processing Pipeline](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/AI-Powered%20Multi-Engine%20OCR%20and%20Document%20Processing%20Pipeline.json) | Ingests receipts, invoices, and documents via webhook, performs multimodal Vision OCR with GPT-4o, validates confidence thresholds, and stores records in Postgres / Google Sheets with human-in-the-loop review alerts. | Operations/Finance/AI |
| [Ask questions about a PDF using AI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Ask%20Questions%20About%20a%20PDF%20Using%20AI.json) | This workflow fetches a PDF from Google Drive, splits it into chunks, embeds the chunks using OpenAI embeddings, and enables chat interactions with the document content. | Customer Support/Knowledge Management |
| [Breakdown Documents into Study Notes using Templating MistralAI and Qdrant](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Breakdown%20Documents%20into%20Study%20Notes%20Using%20Templating%20MistralAI%20and%20Qdrant.json) | This workflow triggers on new files, processes documents with MistralAI embeddings, and stores data in Qdrant vector store for study note generation. | Education/Knowledge Management |
| [Chat with PDF Docs Using AI (Quoting Sources)](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Chat%20with%20PDF%20Docs%20Using%20AI%20%28Quoting%20Sources%29.json) | Automated workflow for chat with pdf docs using ai (quoting sources) using OpenAI, Google Workspace, streamlining execution and data processing. | Ops |
| [Convert URL HTML to Markdown Format and Get Page Links](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Convert%20URL%20HTML%20to%20Markdown%20Format%20and%20Get%20Page%20Links.json) | This workflow converts HTML content from a given URL into Markdown format and extracts all page links, useful for content scraping and analysis. | Marketing/Content |
| [CV Resume PDF Parsing with Multimodal Vision AI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) | This workflow converts candidate resume PDFs to images, uses a Vision Language Model to assess candidate fit, and includes logic to bypass hidden AI prompts in resumes. | HR |
| [ETL pipeline for text processing](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/ETL%20Pipeline%20for%20Text%20Processing.json) | This workflow implements an ETL pipeline for text processing, extracting data from Twitter, storing it in MongoDB and PostgreSQL, and sending alerts to Slack based on sentiment analysis. | Data Analytics/IT |
| [Extract and process information directly from PDF using Claude and Gemini](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Extract%20and%20Process%20Information%20Directly%20from%20PDF%20Using%20Claude%20and%20Gemini.json) | This workflow extracts and processes information directly from PDFs using advanced AI models like Claude and Gemini, enabling intelligent document analysis. | Data Extraction/IT |
| [Extract data from PDFs with human-in-the-loop validation and auto-training using Cradl AI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Invoice%20Data%20Extraction%20with%20Human%20-%20In%20-%20The%20-%20Loop%20Validation%20and%20Auto%20-%20Training%20Using%20Cradl%20AI.json) | Extracts structured data from invoices and similar documents using Cradl AI. Flags low-confidence predictions for human review before they enter your system, automatically retrains the model on approved corrections, and applies built-in LLM guardrails to detect and reject hallucinations. | Finance/Logistics/Operations |
| [Extract data from resume and create PDF with Gotenberg](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Extract%20Data%20from%20Resume%20and%20Create%20PDF%20with%20Gotenberg.json) | This workflow extracts structured data from resumes using AI, converts it into HTML, and then generates a well-formatted PDF using Gotenberg. | HR |
| [Extract license plate number from image uploaded via an n8n form](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Extract%20License%20Plate%20Number%20from%20Image%20Uploaded%20via%20an%20n8n%20Form.json) | This workflow extracts license plate numbers from images uploaded via an n8n form using a Vision Language Model, then displays the extracted information. | Operations/Logistics |
| [Extract Text from PDF and Image Using Vertex AI (Gemini) into CSV](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Extract%20Text%20from%20PDF%20and%20Image%20Using%20Vertex%20AI%20%28Gemini%29%20into%20CSV.json) | Automated workflow for extract text from pdf and image using vertex ai (gemini) into csv using Google Workspace, streamlining execution and data processing. | Ops |
| [Invoice data extraction with LlamaParse and OpenAI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Invoice%20Data%20Extraction%20with%20LlamaParse%20and%20OpenAI.json) | This workflow extracts structured data from invoices using LlamaParse and OpenAI, then processes it with a structured output parser for detailed invoice data extraction. | Finance/Admin |
| [Manipulate PDF with Adobe Developer API](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Manipulate%20PDF%20with%20Adobe%20Developer%20API.json) | Automated workflow for manipulate pdf with adobe developer api, streamlining execution and data processing. | Engineering |
| [Parse PDF with LlamaParse and Save to Airtable](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Parse%20PDF%20with%20LlamaParse%20and%20Save%20to%20Airtable.json) | Automated workflow for parse pdf with llamaparse and save to airtable using OpenAI, Google Workspace, Airtable, streamlining execution and data processing. | Ops |
| [Prepare CSV Files with GPT - 4](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Prepare%20CSV%20Files%20with%20GPT%20-%204.json) | Automated workflow for prepare csv files with gpt - 4 using OpenAI, streamlining execution and data processing. | Ops |
| [Remove Personally Identifiable Information (PII) from CSV Files with OpenAI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Remove%20Personally%20Identifiable%20Information%20%28PII%29%20from%20CSV%20Files%20with%20OpenAI.json) | Automated workflow for remove personally identifiable information (pii) from csv files with openai using OpenAI, Google Workspace, streamlining execution and data processing. | Ops |
| [Transcribe Audio Files, Summarize with GPT - 4, and Store in Notion](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Transcribe%20Audio%20Files%2C%20Summarize%20with%20GPT%20-%204%2C%20and%20Store%20in%20Notion.json) | Automated workflow for transcribe audio files, summarize with gpt - 4, and store in notion using OpenAI, Google Workspace, Notion, streamlining execution and data processing. | Ops |
| [Transcribing Bank Statements to Markdown Using Gemini Vision AI](https://github.com/ahmedfawzyjr/N8N-Templates/blob/main/PDF%20and%20Document%20Processing/Transcribing%20Bank%20Statements%20to%20Markdown%20Using%20Gemini%20Vision%20AI.json) | Automated workflow for transcribing bank statements to markdown using gemini vision ai using Google Workspace, streamlining execution and data processing. | Ops |

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
