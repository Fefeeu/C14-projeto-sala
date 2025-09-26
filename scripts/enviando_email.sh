set -e
echo "$CORPO_EMAIL" | mail -s "$TITULO_EMAIL" "$DESTINATARIO_EMAIL"
echo "Comando de envio de e-mail executado."