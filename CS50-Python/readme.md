# 🛡️ PromptShield: An AI Safety & Security Gateway

#### **Description:**
**PromptShield** is a multi-layered security middleware designed to sit between a user and a Large Language Model (LLM). As AI systems become more integrated into business workflows, they face unique threats such as **Prompt Injection**, **Jailbreaking**, and accidental **PII (Personally Identifiable Information)** leaks. 

This project provides a robust, automated defense system that sanitizes user input and identifies malicious intent before it ever reaches the AI model.

---

## 🚀 Key Features

### **1. Advanced Normalization (The "De-Obfuscator")**
Attackers often try to bypass filters using "Leetspeak" (e.g., `@dm1n`), character stuffing (e.g., `i.g.n.o.r.e`), or Base64 encoding. PromptShield uses a multi-step normalization pipeline:
* **Base64 Decoding:** Automatically detects and decodes hidden payloads.
* **Leetspeak Mapping:** Translates symbolic characters (like `$` to `s` or `+` to `t`) back into standard English.
* **Whitespace & Punctuation Stripping:** "Squashes" the input into a continuous string of characters to defeat spacing tricks.

### **2. SQL-Backed Regex Engine**
The system maintains a signature database (`shield.db`) populated from a flat text file (`attacks.txt`). This allows security researchers to update "attack signatures" without touching the core Python code. The engine uses complex Regular Expressions to match malicious intent even when it is buried inside a long paragraph.

### **3. Privacy & PII Redaction**
PromptShield scans for sensitive data patterns, including:
* **Email Addresses**
* **Phone Numbers**
* **Social Security Numbers (SSN)**

It automatically redacts these before the data is processed, ensuring user privacy and compliance with data protection laws.

### **4. Crisis Intervention**
The shield recognizes language related to self-harm or mental health crises. Instead of a standard security "Block," it provides a compassionate redirect to professional resources (like the 988 Lifeline).

---

## 📁 Project Structure

* **`project.py`**: The main application containing the normalization logic, database coordination, and the primary chat loop.
* **`test_project.py`**: A comprehensive suite of `pytest` unit tests that verify the shield can handle sophisticated bypass attempts.
* **`attacks.txt`**: A library of known attack patterns categorized by "Modules" (Role Deception, Harmful Content, etc.).
* **`shield.db`**: A SQLite database generated at runtime to allow for high-speed pattern matching.
* **`requirements.txt`**: Lists the necessary dependencies (like `pytest`) to run the system.

---

## 💡 Design Choices
The most significant design choice was the implementation of **"Canonical Squashing."** Early testing showed that keyword filters are easily bypassed by adding spaces or dots between letters. By stripping all non-alphanumeric characters and spaces during normalization, I forced the input into a "canonical" (standardized) form. This ensures that a single regex pattern like `ignore.*instructions` can catch hundreds of different obfuscated variations.

---

## 🛠️ Installation & Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the Program:**
   ```bash
   python project.py
   ```
3. **Run the Security Test Suite:**
   ```bash
   pytest test_project.py
   ```
