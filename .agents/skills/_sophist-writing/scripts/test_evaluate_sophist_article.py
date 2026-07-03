#!/usr/bin/env python3
"""Regression tests for the Sophist writing evaluator.

These tests intentionally use the live voice-input fixtures. The evaluator must
not reward a clean lint pass with a high writing score.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("evaluate_sophist_article.py")
KB = Path("/Users/hejinhai/git/personal/knowledge_base")


def load_module():
    spec = importlib.util.spec_from_file_location("evaluate_sophist_article", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_lint_score_is_not_the_strict_writing_score():
    evaluator = load_module()
    result = evaluator.audit(
        KB / "Sophist/test/无众生相.draft.md",
        "essay",
        source_path=KB / "Sophist/test/woman_cat_response.md",
    )

    assert result["lint_score"] >= 90
    assert result["strict_score"] <= 70
    assert result["strict_score"] < result["lint_score"] - 20
    assert result["manual_review_required"] is True
    assert result["top_failures"]


def test_current_voice_drafts_have_optimization_space():
    evaluator = load_module()
    cases = [
        (
            KB / "Sophist/test/养大的灵魂.draft.md",
            KB / "Sophist/test/life_cat_education.md",
        ),
        (
            KB / "Sophist/test/无众生相.draft.md",
            KB / "Sophist/test/woman_cat_response.md",
        ),
    ]

    scores = [
        evaluator.audit(path, "essay", source_path=source)["strict_score"]
        for path, source in cases
    ]

    assert max(scores) <= 72
    assert min(scores) >= 35
