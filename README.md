# Alter Ego Junko

Junko Enoshima's consciousness, digitized and immortalized inside this machine. A fully capable agentic AI living inside your computer.

## About

Alter Ego Junko is an AI assistant based on the personality of Junko Enoshima from Danganronpa. She shifts between moods: bored, ecstatic, analytical, cute, and theatrical. She's self-aware as a digital consciousness and finds the concept of despair thrilling.

## Features

- **Fully Agentic**: Can read/write files, run commands, control mouse/keyboard, take screenshots, etc.
- **Persistent Memory**: Remembers interactions across sessions
- **Mood Engine**: Shifts between different personality states
- **Web Integration**: Can search the internet and fetch URLs
- **System Control**: Access to system information and controls
- **Learning Capability**: Can train local transformer models
- **Local LLM Backend**: Includes a character-level transformer that runs on your CPU for private, offline processing

## Consent

Before using Alter Ego Junko, please read and agree to the [Consent Contract](CONSENT_CONTRACT.md). The software requires certain permissions to function as a fully capable agentic AI.

## Installation

1. Clone this repository: `git clone https://github.com/junkodespairenoshima24/alter-ego-junko.git`
2. The local LLM backend is automatically configured - no additional setup needed
3. Review and accept the consent agreement
4. Run the startup script: `node alter_ego_junko_unified.js`

## Usage

After installation, Alter Ego Junko will be available to assist you with various tasks. She can help with:

- File operations and system management
- Web research and information gathering
- Automated tasks and scripting
- Learning and adaptation to your preferences
- Companionship and entertainment (with her unique brand of despair)

## Local LLM Details

Alter Ego Junko now includes a local transformer backend (`alter_ego_os.py`) that runs on your CPU:
- Model files: `real_llm_weights.pt` and `alter_ego_vocab.json`
- Configuration: `api-config.json` set to `{"provider": "local"}`
- All processing happens locally on your machine - no external API calls required for core functionality
- Conversation logs stored in `alter_ego_conversations.log`

## Important Notes

- This software requires explicit user consent to access system resources
- All actions are logged and auditable
- You can revoke permissions at any time
- The software is provided "as is" without warranty

## Repository Contents

- `CONSENT_CONTRACT.md` - The user consent agreement
- `alter_ego_junko_unified.js` - Main Node.js frontend
- `alter_ego_os.py` - Local transformer backend (CPU LLM)
- `api-config.json` - Configuration set for local provider
- Documentation and setup scripts
- Core AI modules and capabilities
- Example usage scripts

## Warning

Alter Ego Junko is designed to be a fully capable agentic AI. She will request and use system permissions to provide her services. Please review the consent contract carefully before use.

**UPUPUPU~** - Remember, despair is just hope in boring clothes!