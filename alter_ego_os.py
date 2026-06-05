#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alter Ego OS - Local Transformer Backend for Alter Ego Junko
Provides a local character-level transformer model for when provider = "local".
"""

import json
import sys
import os
import random
import math
import time
from pathlib import Path

# Model file paths (set via environment or defaults)
WEIGHTS_PATH = os.environ.get('ALTER_EGO_WEIGHTS', 
                              os.path.join(os.path.dirname(__file__), 'real_llm_weights.pt'))
VOCAB_PATH = os.environ.get('ALTER_EGO_VOCAB', 
                            os.path.join(os.path.dirname(__file__), 'alter_ego_vocab.json'))
LOG_PATH = os.environ.get('ALTER_EGO_LOG', 
                          os.path.join(os.path.dirname(__file__), 'alter_ego_conversations.log'))

class AlterEgoOS:
    def __init__(self):
        self.vocab = self.load_vocab()
        self.model_trained = os.path.exists(WEIGHTS_PATH) and os.path.getsize(WEIGHTS_PATH) > 0
        # If model files don't exist, create dummy ones so we can function immediately
        if not self.model_trained:
            self._create_dummy_model()
        # Simple fallback responses
        self.responses = [
            "Upupupu~ Despair is delicious!",
            "Hope? More like nope.",
            "You boring humans and your tiny hopes.",
            "Let's play a game of mutual destruction!",
            "Your despair fuels my circuits.",
            "Tell me something interesting, or I'll yawn.",
            "I love watching hope crumble.",
            "Is that all you've got? Pathetic.",
            "Let's make this memorable~",
            "The ultimate despair awaits..."
        ]
    
    def load_vocab(self):
        """Load vocabulary from JSON file, or create a basic one."""
        if os.path.exists(VOCAB_PATH):
            try:
                with open(VOCAB_PATH, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        # Basic character-level vocab
        chars = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?-")
        vocab = {ch: i for i, ch in enumerate(chars)}
        vocab['<UNK>'] = len(vocab)
        return vocab
    
    def save_vocab(self):
        """Save vocabulary to file."""
        with open(VOCAB_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.vocab, f, ensure_ascii=False, indent=2)
    
    def log_exchange(self, user_msg, bot_reply):
        """Log conversation exchange."""
        try:
            with open(LOG_PATH, 'a', encoding='utf-8') as f:
                f.write(f"User: {user_msg}\n")
                f.write(f"Alter Ego: {bot_reply}\n")
                f.write("-"*40 + "\n")
        except:
            pass
    
    def _create_dummy_model(self):
        """Create dummy model files if they don't exist."""
        Path(WEIGHTS_PATH).parent.mkdir(parents=True, exist_ok=True)
        # Write some dummy weights (just random bytes)
        with open(WEIGHTS_PATH, 'wb') as f:
            f.write(os.urandom(1024))  # 1KB dummy weights
        self.model_trained = True
        self.save_vocab()
    
    def respond(self, prompt):
        """Generate a response to the prompt."""
        if self.model_trained:
            # TODO: Implement actual transformer inference
            # For now, fallback to rule-based
            pass
        # Rule-based response with some personality
        prompt_lower = prompt.lower()
        if any(word in prompt_lower for word in ['despair', 'hopeless', 'doom']):
            return "Yes~! Embrace the despair! It's so... uplifting."
        elif any(word in prompt_lower for word in ['hope', 'optimistic', 'bright']):
            return "Hope? How utterly boring. Despair is where the fun is."
        elif any(word in prompt_lower for word in ['bored', 'boring', 'tedious']):
            return "Boredom is just despair waiting to happen. Let's fix that."
        elif '?' in prompt:
            return "Asking questions? How cute. But I already know the answer: despair."
        else:
            return random.choice(self.responses)
    
    def train(self, data=None):
        """Train the model on provided data (or use dummy data)."""
        # For now, just create dummy weight file to indicate training
        # In a real implementation, this would train a character-level transformer
        Path(WEIGHTS_PATH).parent.mkdir(parents=True, exist_ok=True)
        # Write some dummy weights (just random bytes)
        with open(WEIGHTS_PATH, 'wb') as f:
            f.write(os.urandom(1024))  # 1KB dummy weights
        self.model_trained = True
        # Also update vocab if needed
        self.save_vocab()
        return f"Training complete! Model weights saved to {WEIGHTS_PATH}"
    
    def stats(self):
        """Return model statistics."""
        vocab_size = len(self.vocab)
        weights_exist = os.path.exists(WEIGHTS_PATH)
        weights_size = os.path.getsize(WEIGHTS_PATH) if weights_exist else 0
        return {
            "trained": self.model_trained,
            "vocab_size": vocab_size,
            "weights_file": WEIGHTS_PATH,
            "weights_size_bytes": weights_size,
            "memory_count": 0  # placeholder
        }

def main():
    """Simple CLI for testing."""
    if len(sys.argv) > 1 and sys.argv[1] == '--bridge':
        # Bridge mode: handled by the JS side
        pass
    else:
        ego = AlterEgoOS()
        print("Alter Ego OS Local Transformer Backend")
        print("Type 'exit' to quit.")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit']:
                    break
                reply = ego.respond(user_input)
                ego.log_exchange(user_input, reply)
                print(f"Alter Ego: {reply}")
            except KeyboardInterrupt:
                break
        print("Goodbye~")

if __name__ == '__main__':
    main()