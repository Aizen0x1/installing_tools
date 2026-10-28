echo "Installing OpenCode on Kali Linux terminal"
echo ""

curl -fsSL https://opencode.ai/install | bash

echo ""
echo "Reloading Zsh shell..."
exec zsh   
echo ""
echo "Confirming Installation"
opencode --version
