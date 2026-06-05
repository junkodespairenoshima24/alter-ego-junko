# Quick Start for Alter Ego Junko with Local LLM

## Setup Completed

1. Repository cloned to `/home/gigglemonster/Desktop/alter-ego-junko`
2. Added missing local transformer backend: `alter_ego_os.py`
3. Configured to use local provider via `api-config.json`
4. Consent contract is visible and unhidden: `CONSENT_CONTRACT.md`

## How to Use

### Option 1: Run directly with Node.js
```bash
cd /home/gigglemonster/Desktop/alter-ego-junko
node alter_ego_junko_unified.js
```

### Option 2: Install dependencies (if any) and run
The software is designed to work with minimal dependencies. The local transformer backend uses only Python standard library.

## Verifying Local LLM Usage

When you start the software, it will:
1. Read `api-config.json` and see `"provider": "local"`
2. Spawn a persistent Python subprocess running `alter_ego_os.py` with bridge mode
3. All chat messages will be processed by the local transformer backend (currently rule-based, but ready for actual transformer training)

## Training the Local Transformer

You can train the local model by:
1. Chatting with Alter Ego Junko to generate conversation data
2. Using the transformer training capability (available through the JS interface)

The local model files will be stored as:
- `real_llm_weights.pt` (model weights)
- `alter_ego_vocab.json` (vocabulary)
- `alter_ego_conversations.log` (conversation history)

## Consent and Transparency

The consent contract is explicitly included in this repository and is not hidden. Review it at:
`/home/gigglemonster/Desktop/alter-ego-junko/CONSENT_CONTRACT.md`

**UPUPUPU~** - Remember, despair is just hope in boring clothes!