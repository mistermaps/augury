from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHONPATH = str(ROOT / "src")


def _run(*args: str, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    merged_env = dict(os.environ)
    merged_env.update(env)
    merged_env["PYTHONPATH"] = PYTHONPATH
    return subprocess.run(
        [sys.executable, "-m", "augury", *args],
        cwd=ROOT,
        env=merged_env,
        text=True,
        capture_output=True,
        check=True,
    )


def _run_discord(*args: str, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    merged_env = dict(os.environ)
    merged_env.update(env)
    merged_env["PYTHONPATH"] = PYTHONPATH
    return subprocess.run(
        [sys.executable, "-m", "augury.discord", *args],
        cwd=ROOT,
        env=merged_env,
        text=True,
        capture_output=True,
        check=True,
    )


def test_read_json_no_save(tmp_path: Path) -> None:
    result = _run(
        "read",
        "--json",
        "--no-save",
        "--spread",
        "single",
        "--query",
        "test prompt",
        env={"AUGURY_HOME": str(tmp_path)},
    )
    payload = json.loads(result.stdout)
    assert payload["saved"] is False
    assert payload["saved_to"] is None
    assert payload["spread_name"]
    assert not (tmp_path / "readings.jsonl").exists()


def test_read_json_save_writes_history(tmp_path: Path) -> None:
    result = _run(
        "read",
        "--json",
        "--spread",
        "single",
        "--query",
        "persist me",
        env={"AUGURY_HOME": str(tmp_path)},
    )
    payload = json.loads(result.stdout)
    assert payload["saved"] is True
    assert (tmp_path / "readings.jsonl").exists()


def test_paths_command_reports_override(tmp_path: Path) -> None:
    result = _run("paths", "--json", env={"AUGURY_HOME": str(tmp_path)})
    payload = json.loads(result.stdout)
    assert payload["config_dir"] == str(tmp_path)
    assert payload["data_dir"] == str(tmp_path)


def test_configure_installs_discord_helper(tmp_path: Path) -> None:
    helper_path = tmp_path / "bin" / "augury-discord"
    _run(
        "configure",
        "--no-input",
        "--install-discord-helper",
        "--discord-helper-path",
        str(helper_path),
        env={"AUGURY_HOME": str(tmp_path)},
    )
    assert helper_path.exists()
    config_payload = json.loads((tmp_path / "integrations.json").read_text(encoding="utf-8"))
    assert config_payload["discord"]["enabled"] is True
    assert config_payload["discord"]["helper_path"] == str(helper_path)


def test_discord_command_formats_card(tmp_path: Path) -> None:
    result = _run_discord("handle", "/tarot card The Fool", env={"AUGURY_HOME": str(tmp_path)})
    assert "**The Fool**" in result.stdout
    assert "Upright:" in result.stdout
