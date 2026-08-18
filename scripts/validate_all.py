#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys

root = Path(__file__).resolve().parents[1]
found = 0
failures = []

for pkg in sorted(root.glob('Part-*/**/package.json')):
    if 'node_modules' in pkg.parts:
        continue
    found += 1
    directory = pkg.parent
    data = json.loads(pkg.read_text(encoding='utf-8'))

    if (directory / 'pnpm-lock.yaml').exists():
        pm = ['pnpm']
        install = ['pnpm', 'install', '--frozen-lockfile']
    elif (directory / 'yarn.lock').exists():
        pm = ['yarn']
        install = ['yarn', 'install', '--immutable']
    else:
        pm = ['npm']
        install = ['npm', 'ci'] if (directory / 'package-lock.json').exists() else ['npm', 'install']

    commands = [install]
    for script in ['lint', 'test', 'build']:
        if script in data.get('scripts', {}):
            commands.append(pm + ['run', script])

    print(f'\n== {directory.relative_to(root)} ==')
    for command in commands:
        print('+', ' '.join(command))
        result = subprocess.run(command, cwd=directory)
        if result.returncode:
            failures.append((str(directory), command, result.returncode))
            break

print(f'\nDetected buildable package projects: {found}')
if failures:
    print('Failures:')
    for failure in failures:
        print(failure)
    sys.exit(1)

print('Validation complete. Empty scaffold folders were skipped.')
