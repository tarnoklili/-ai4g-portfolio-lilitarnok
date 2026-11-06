"""Settings you are expected to understand and own. Change them deliberately."""
import os
import re

# Topic: AI coding assistants (Copilot, Cursor, Claude Code and similar).
# SDG 9: innovation and the technological capability of industry.
# These are the search terms sent to the Hacker News API; the filter below then
# decides what is kept.
QUERIES = [
    "AI coding",
    "coding agents",
    "coding assistant",
    "vibe coding",
    "agentic coding",
    "Claude Code",
    "Copilot",
    "Cursor",
    "Codex",
    "Windsurf",
    "Gemini CLI",
    "Aider",
    "AI-generated code",
    "LLM code generation",
    "AI code review",
    "AI pair programming",
    "AI developer tools",
    "AI programming",
    "LLM programming",
    "LLM coding",
    "AI developers",
    "AI agents code",
    "Model Context Protocol",
    "MCP server",
    "AI pull requests",
    "AI replace programmers",
    "prompt engineering code",
]

# Relevance filter. The search API matches words anywhere in a comment, so every
# comment is checked again here. Set USE_RELEVANCE_FILTER = False to keep everything.
USE_RELEVANCE_FILTER = True

# Clearly about AI coding tools or practices (case-insensitive).
TOOLS_RE = re.compile(
    r"\b(?:"
    r"Claude Code|GitHub Copilot|Copilot|Codex|Windsurf|Gemini CLI|Aider|Cline|Kiro|"
    r"vibe[- ]?coding|AI coding|"
    r"AI[- ]assisted (?:coding|programming|development)|AI pair programming|"
    r"coding (?:agents?|assistants?)|agentic (?:coding|development|programming)|"
    r"AI[- ]generated code|LLM[- ]generated code|"
    r"AI code (?:review|completion|generation)|code completion"
    r")\b",
    re.I,
)
# "Cursor" is also the text cursor, so it only counts if spelled with a capital C
# AND the comment also talks about AI (see AI_CONTEXT_RE).
CURSOR_RE = re.compile(r"\bCursor\b")
AI_CONTEXT_RE = re.compile(
    r"\b(?:AI|LLMs?|agents?|prompts?|Claude|GPT\w*|Copilot|Sonnet|Opus|Codex|Windsurf)\b"
)


# Second rule (wider net): the comment is about AI/LLMs AND about programming work.
# Keeps adoption talk such as "LLMs change how developers review code".
AI_WORDS_RE = re.compile(r"\b(?:AI|LLMs?|AI agents?|GPT\w*|Claude|Gemini|Sonnet|Opus|MCP)\b")
CODING_RE = re.compile(
    r"\b(?:coding|programming|programmers?|developers?|software engineers?|engineers?|codebase|"
    r"pull requests?|code review|refactor\w*|unit tests?|IDE|repo|repository)\b",
    re.I,
)


def is_relevant(text):
    if not USE_RELEVANCE_FILTER:
        return True
    if TOOLS_RE.search(text):
        return True
    if CURSOR_RE.search(text) and AI_CONTEXT_RE.search(text):
        return True
    return bool(AI_WORDS_RE.search(text) and CODING_RE.search(text))


# Ignore very short comments ("This.", "lol") - nothing to measure.
MIN_CHARS = 40

# Safety limit on API pages per query per run (100 comments per page).
MAX_PAGES = 8

# No backfill: the tool collects live. The very first run looks back a minimum of
# 1 hour (so the first runs are not empty); say so in your README.
FIRST_RUN_BACKFILL_HOURS = 0

# Main model, chosen by you: trained on ~124M English tweets (2018-2021), labels
# negative / neutral / positive, licence CC-BY-4.0. Write YOUR reasons in the
# README. The raw text is stored, so everything can be re-scored with another
# model later without losing data.
MODEL_NAME = os.environ.get("MODEL_NAME", "cardiffnlp/twitter-roberta-base-sentiment-latest")
