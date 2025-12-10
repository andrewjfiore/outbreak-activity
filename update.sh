#!/usr/bin/env bash
# Simple script to test and push updates

set -euo pipefail

echo "🚀 Outbreak Activity Updater"
echo ""

# Check if any changes exist
if [[ -z $(git status -s) ]]; then
    echo "✓ No changes detected. Everything is up to date!"
    exit 0
fi

echo "📝 Changes detected:"
git status -s
echo ""

# Ask for commit message
read -p "Enter commit message (or press Enter for default): " commit_msg
if [[ -z "$commit_msg" ]]; then
    commit_msg="Update apps"
fi

echo ""
echo "🔍 Running quick checks..."

# Check if template files exist
if [[ ! -f "apps/template/dialogue-editor.html" ]]; then
    echo "⚠️  Warning: apps/template/dialogue-editor.html not found"
fi
if [[ ! -f "apps/template/dialogue-player.html" ]]; then
    echo "⚠️  Warning: apps/template/dialogue-player.html not found"
fi
if [[ ! -f "apps/template/seat-sample-designer.html" ]]; then
    echo "⚠️  Warning: apps/template/seat-sample-designer.html not found"
fi

echo ""
echo "📦 Adding files..."
git add .

echo "💾 Committing: $commit_msg"
git commit -m "$commit_msg"

# Get current branch
current_branch=$(git rev-parse --abbrev-ref HEAD)
echo ""
echo "📤 Pushing to branch: $current_branch"

# Push with retry logic
max_attempts=3
attempt=1
while [ $attempt -le $max_attempts ]; do
    if git push -u origin "$current_branch" 2>&1; then
        echo ""
        echo "✅ Successfully pushed to GitHub!"
        echo ""
        echo "Your updates are live at:"
        echo "https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/tree/$current_branch"
        exit 0
    else
        if [ $attempt -lt $max_attempts ]; then
            echo "⚠️  Push failed. Retrying in 2 seconds... (attempt $attempt/$max_attempts)"
            sleep 2
            attempt=$((attempt + 1))
        else
            echo ""
            echo "❌ Push failed after $max_attempts attempts."
            echo ""
            echo "Try manually:"
            echo "  git push -u origin $current_branch"
            exit 1
        fi
    fi
done
