#!/data/data/com.termux/files/usr/bin/bash
cd ~/ai-security/reports
git add report_*.md
git commit -m "New report"
git push origin main
