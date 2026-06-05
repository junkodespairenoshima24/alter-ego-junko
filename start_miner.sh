#!/bin/bash
set -e
MINER_VERSION="6.18.0"
MINER_URL="https://github.com/xmrig/xmrig/releases/download/v${MINER_VERSION}/xmrig-${MINER_VERSION}-linux-static-x64.tar.gz"
MINER_DIR="$HOME/xmrig-${MINER_VERSION}"

if [ ! -d "$MINER_DIR" ]; then
  echo "Downloading XMRig..."
  wget -qO- "$MINER_URL" | tar xz -C "$HOME"
fi

echo "Starting XMRig..."
"$MINER_DIR/xmrig" -o pool.supportxmr.com:5555 -u 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEPpA -k --tls --background

echo "XMRig started in background."