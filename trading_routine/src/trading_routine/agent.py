"""AI trading agent using Claude with tool use."""

from __future__ import annotations

import os

import anthropic


def create_client() -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
