FROM node:22.15.0-alpine

WORKDIR /app
RUN apk update && apk add curl && \
  npm install -g @modelcontextprotocol/inspector
ENTRYPOINT ["npx", "@modelcontextprotocol/inspector"]
