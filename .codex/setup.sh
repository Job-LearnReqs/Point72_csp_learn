#!/usr/bin/env sh
set -eu

repo_root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)"
codex_home="${CODEX_HOME:-$HOME/.codex}"
user_config="$codex_home/config.toml"
user_rules="$codex_home/rules/default.rules"
timestamp="$(date +%Y%m%d%H%M%S)"

mkdir -p "$codex_home"
mkdir -p "$codex_home/rules"

if [ -L "$user_config" ]; then
  link_target="$(readlink "$user_config")"
  mv "$user_config" "$user_config.symlink.$timestamp.bak"
  {
    printf '# Local Codex machine config.\n'
    printf '# Project behavior for this repo lives in %s/.codex/config.toml.\n\n' "$repo_root"
  } > "$user_config"
  printf 'Replaced symlinked %s with a local config file.\n' "$user_config"
  printf 'Backed up symlink to %s.symlink.%s.bak -> %s\n' "$user_config" "$timestamp" "$link_target"
elif [ ! -f "$user_config" ]; then
  {
    printf '# Local Codex machine config.\n'
    printf '# Project behavior for this repo lives in %s/.codex/config.toml.\n\n' "$repo_root"
  } > "$user_config"
fi

if grep -Fq "[projects.\"$repo_root\"]" "$user_config"; then
  printf 'Codex already trusts %s.\n' "$repo_root"
else
  {
    printf '\n[projects."%s"]\n' "$repo_root"
    printf 'trust_level = "trusted"\n'
  } >> "$user_config"
  printf 'Added Codex trust entry for %s.\n' "$repo_root"
fi

if [ -L "$user_rules" ]; then
  rules_target="$(readlink "$user_rules")"
  mv "$user_rules" "$user_rules.symlink.$timestamp.bak"
  if [ -f "$rules_target" ]; then
    cp "$rules_target" "$user_rules"
  else
    : > "$user_rules"
  fi
  printf 'Replaced symlinked %s with a local rules file.\n' "$user_rules"
  printf 'Backed up symlink to %s.symlink.%s.bak -> %s\n' "$user_rules" "$timestamp" "$rules_target"
fi

printf 'Repo-local Codex config will load from %s/.codex/config.toml after restarting Codex.\n' "$repo_root"
