# Agentic AI Cybersecurity Project (Learning Project #4)

This project is part of my learning journey in cybersecurity and AI. It demonstrates a simple agentic workflow where AI is used to generate payloads and test a website for basic vulnerabilities.

## Overview

The project consists of three key stages:

1. **Reconnaissance (`recon.py`)**  
   - Collects website content from a dummy test website.
   - Stores the content locally in `site_content.txt`.

2. **Payload Generation (`generate_payloads.py`)**  
   - Uses OpenAI's GPT model to analyze the website content.
   - Generates test payloads for common vulnerabilities like XSS, SQL Injection, and Directory Traversal.
   - Saves the payloads in `payloads.txt`.

3. **Testing (`test_payloads.py`)**  
   - Sends each generated payload to the target site.
   - Records potential vulnerability responses in `results.txt`.

## Features

- Simple and modular
- Uses OpenAI's GPT API (manually input API key at runtime)
- Built entirely in **Termux** on Android
- Agentic structure: senses, thinks, and acts
- Supports testing on dummy sites like [http://demo.testfire.net](http://demo.testfire.net)

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/mayanklau/ai-security.git
   cd ai-security