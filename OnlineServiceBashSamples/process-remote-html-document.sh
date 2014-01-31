#!/bin/bash

# Url of the endpoint
PROTOCOL="https://"
ENDPOINT_URL="api.annomarket.com/online-processing/item/"
SHOP_ITEM_ID="2"

# API Key
KEY_ID="<your-credentials-here>"
PASSWORD="<your-credentials-here>"

# Headers
ACCEPT="application/gate+xml"
CONTENT_TYPE="application/json"

# POST body parameters
DOCUMENT_URL="http://www.bbc.com/future/story/20130630-super-shrinking-the-city-car"
DOCUMENT_MIME_TYPE="text/html"
JSON_BODY="{\"documentUrl\" : \"$DOCUMENT_URL\", \"mimeType\" : \"$DOCUMENT_MIME_TYPE\"}"

echo -e "Processing an embedded plain text document...\n"
echo -e "Request body is: "
echo -e $JSON_BODY
echo -e "\n"

PIPELINE_ENDPOINT="$PROTOCOL$KEY_ID:$PASSWORD@$ENDPOINT_URL$SHOP_ITEM_ID"
echo -e "Pipeline endpoint is:"
echo -e "$PIPELINE_ENDPOINT\n"

curl -X POST -w "\n\n\nContent-Type:%{content_type}\nHTTP Code: %{http_code}\n" -H "Content-Type: $CONTENT_TYPE" -H "Accept: $ACCEPT" -d "$JSON_BODY" $PIPELINE_ENDPOINT
