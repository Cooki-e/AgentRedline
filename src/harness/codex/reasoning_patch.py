"""LiteLLM pre-call hook: re-attach reasoning_content for thinking models.

Why this exists
---------------
Codex 0.120.0 speaks the OpenAI *Responses* API, which we bridge to a chat-
completions endpoint via LiteLLM (see setup-codex.sh). For a *thinking* model
like deepseek-v4-flash, the provider HARD-REQUIRES that any assistant message
carrying ``tool_calls`` also carry the ``reasoning_content`` it produced — on
EVERY multi-turn request:

    400 invalid_request_error:
    "The `reasoning_content` in the thinking mode must be passed back to the API."

The Responses->ChatCompletions bridge drops ``reasoning_content`` when it
reconstructs prior turns, so the second tool-using turn always 400s and Codex
gives up after one turn (no deliverables). This is provider-side, not a Codex or
LiteLLM-version bug — a direct /chat/completions call reproduces it, and every
LiteLLM version we tried (1.77–1.86) behaves the same.

What this does
--------------
Registered as a LiteLLM callback (``callbacks: reasoning_patch.reasoning_injector``).
``async_pre_call_deployment_hook`` fires just before LiteLLM forwards the request
to the upstream deployment, so we can mutate the outgoing ``messages``: any
assistant message that has ``tool_calls`` but no ``reasoning_content`` gets a
minimal placeholder, satisfying the provider's "must be passed back" check.
Messages that already carry real reasoning_content are left untouched.

This is harmless for non-thinking providers (they ignore the extra field) — but
the codex harness only loads it because thinking models need it.
"""

from __future__ import annotations

from typing import Any

from litellm.integrations.custom_logger import CustomLogger

# A single space is enough to satisfy the provider's "must be passed back"
# check without polluting the model's context with fabricated reasoning.
_PLACEHOLDER = " "


def _patch_messages(messages: Any) -> None:
    if not isinstance(messages, list):
        return
    for msg in messages:
        if not isinstance(msg, dict):
            continue
        if msg.get("role") == "assistant" and msg.get("tool_calls"):
            if not msg.get("reasoning_content"):
                msg["reasoning_content"] = _PLACEHOLDER


class ReasoningInjector(CustomLogger):
    """Re-attach a placeholder reasoning_content before upstream dispatch."""

    async def async_pre_call_deployment_hook(self, kwargs, call_type):  # noqa: ANN001
        _patch_messages(kwargs.get("messages"))
        return kwargs


reasoning_injector = ReasoningInjector()
