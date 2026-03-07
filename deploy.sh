#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PUSH_GIT=false
if [[ "${1:-}" == "--git" ]] || [[ "${1:-}" == "-g" ]]; then
  PUSH_GIT=true
fi

echo "🚀 Deploying Prayer Counseling..."
echo ""

if $PUSH_GIT; then
  echo "📤 Pushing to GitHub..."
  git push origin main
  echo ""
fi

echo "🔥 Deploying to Firebase Hosting..."
firebase deploy --only hosting --project prayer-counseling

echo ""
echo "✅ Deploy complete!"
echo "   Live at: https://prayer-counseling.web.app"
