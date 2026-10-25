#!/usr/bin/env bash
set -e

# Configuration
DOCKERHUB_USERNAME="${DOCKERHUB_USERNAME:-4 credkellar}"
IMAGE_NAME="ai-muse-trading-agent"
TAG="${1:-latest}"

FULL_IMAGE="${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${TAG}"

echo "🚀 Starting Docker publish process..."

# Check Docker Hub Token/Password
if [ -z "$DOCKERHUB_TOKEN" ]; then
  echo "❌ Error: DOCKERHUB_TOKEN environment variable is missing."
  echo "Please set it using: export DOCKERHUB_TOKEN='your_dockerhub_token'"
  exit 1
fi

echo "🔑 Authenticating with Docker Hub as user: '${DOCKERHUB_USERNAME}'..."
echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

echo "🔨 Building Docker image: ${FULL_IMAGE}..."
docker build -t "$FULL_IMAGE" .

echo "📤 Pushing image to Docker Hub..."
docker push "$FULL_IMAGE"

echo "✅ Successfully published ${FULL_IMAGE} to Docker Hub!"
