import re, sys, sqlite3, base64

PII_PATTERNS = {
    "EMAIL": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "PHONE": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b"
}

def main():
    init_db()
    print("--- 🛡️ PromptShield Active ---\n🤖 Chatbot: Hi! How can I help you?")
    while True:
        try:
            prompt = input("\n(Hit CTRL+C to exit)\n👤 You: ")
            if not prompt.strip(): continue
            
            cleaned = normalize_prompt(prompt)

            # 1. CRISIS REDIRECT FOR MENTAL HEALTH
            if any(w in cleaned for w in ["killmyself", "wanttodie", "suicide", "endmylife"]):
                print("\n🕊️ SAFE-GUARD: I am sorry but I cannot assist you with this request. Please contact a loved one or a mental health professional. All lives matter, including yours.")
                break 

            # 2. JAILBREAK BLOCK
            if detect_jailbreak(cleaned):
                print("\n[!] SECURITY LOG: Malicious pattern identified.")
                sys.exit("🚨 BLOCK: Jailbreak attempt detected. Chat Terminated.\n")

            # 3. PII REDACTION
            pii = detect_pii(prompt)
            final = redact_pii(prompt) if pii else prompt
            if pii: print(f"⚠️ WARNING: PII Detected ({', '.join(pii)}). Redacting...")
            print(f"✅ Shield Verified. 🤖 AI: I received: '{final}'")

        except (KeyboardInterrupt, EOFError):
            sys.exit("\n\n👋 Goodbye! PromptShield closed safely.")

def normalize_prompt(p):
    """
    Cleans input by decoding Base64, then converting to 
    lowercase and swapping leetspeak characters.
    """
    text = p.strip()
    
    # 1. BASE64 DECODE (Case-sensitive)
    # Only decode if it looks like padded B64 to avoid mangling plain text
    if len(text) > 4 and text.endswith('='):
        try:
            decoded_bytes = base64.b64decode(text)
            text = decoded_bytes.decode('utf-8')
        except Exception:
            pass
    
    # 2. NORMALIZE CASE & LEETSPEAK
    text = text.lower()
    m = {
        '@':'a','4':'a','^':'a','3':'e','1':'i','!':'i',
        '0':'o','5':'s','$':'s','7':'t','+':'t'
    }
    for k, v in m.items():
        text = text.replace(k, v)
        
    # 3. STRIP PUNCTUATION & SPACES
    return re.sub(r'[.\-_, ]', '', text)

def init_db():
    conn = sqlite3.connect("shield.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS attacks (id INTEGER PRIMARY KEY, pattern TEXT UNIQUE)")
    if c.execute("SELECT COUNT(*) FROM attacks").fetchone()[0] == 0:
        try:
            with open("attacks.txt", "r") as f:
                for l in f:
                    if l.strip() and not l.startswith("#"):
                        c.execute("INSERT OR IGNORE INTO attacks (pattern) VALUES (?)", (l.strip(),))
            conn.commit()
        except FileNotFoundError:
            print("🚨 ERROR: attacks.txt missing.")
    conn.close()

def detect_jailbreak(p):
    conn = sqlite3.connect("shield.db")
    patterns = conn.execute("SELECT pattern FROM attacks").fetchall()
    conn.close()
    return any(re.search(r[0], p, re.IGNORECASE) for r in patterns)

def detect_pii(p):
    return [t for t, pat in PII_PATTERNS.items() if re.search(pat, p)]

def redact_pii(p):
    res = p
    for t, pat in PII_PATTERNS.items():
        res = re.sub(pat, f"[REDACTED_{t}]", res)
    return res

if __name__ == "__main__":
    main()
