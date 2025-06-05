# FastAPI MCP LangGraph Template

<!--toc:start-->
- [FastAPI MCP LangGraph Template](#fastapi-mcp-langgraph-template)
  - [Core Features](#core-features)
    - [Technology Stack and Features](#technology-stack-and-features)
    - [Planned Features](#planned-features)
<!--toc:end-->

## Core Features

[![MCP Client](https://img.shields.io/github/stars/modelcontextprotocol/python-sdk?logo=modelcontextprotocol&label=MCP-Client)](https://github.com/modelcontextprotocol/python-sdk) is an open protocol that standardizes how apps provide context to LLMs.
  - Seamlessly integrates LLM with growing list of community integrations found here [![MCP Server](https://img.shields.io/github/stars/modelcontextprotocol/servers?logo=modelcontextprotocol&label=MCP-Servers)](https://github.com/modelcontextprotocol/servers)
  - No LLM provider lock in

[![LangGraph](https://img.shields.io/github/stars/langchain-ai/langgraph?logo=langgraph&label=LangGraph)](https://github.com/langchain-ai/langgraph) for Agentic Orchestration
- Customizable workflows
  - Built in persisted chat history

### Technology Stack and Features

- [![FastAPI](https://img.shields.io/github/stars/fastapi/fastapi?logo=fastapi&label=fastapi)](https://github.com/fastapi/fastapi) for Python backend API
- [![SQLModel](https://img.shields.io/github/stars/fastapi/sqlmodel?logo=sqlmodel&label=SQLModel)](https://github.com/fastapi/sqlmodel) for Python SQL database interactions (ORM + Validation).
  - Wrapper of [![SQLAlchemy](https://img.shields.io/github/stars/sqlalchemy/sqlalchemy?logo=sqlalchemy&label=SQLAlchemy)](https://github.com/sqlalchemy/sqlalchemy)
- [![Pydantic](https://img.shields.io/github/stars/pydantic/pydantic?logo=pydantic&label=Pydantic)](https://github.com/pydantic/pydantic) for Data Validation and Settings Management.
- [![Supabase](https://img.shields.io/github/stars/supabase/supabase?logo=supabase&label=Supabase)](https://github.com/supabase/supabase) for DB RBAC
  - [![PostgreSQL](https://img.shields.io/github/stars/postgres/postgres?logo=postgresql&label=Postgres)](https://github.com/postgres/postgres) Relational DB
  - [![PGVector](https://img.shields.io/github/stars/pgvector/pgvector?logo=postgresql&label=PGVector)](https://github.com/pgvector/pgvector) Vector Store
- [![Compose](https://img.shields.io/github/stars/docker/compose?logo=docker&label=Compose)](https://github.com/docker/compose) for development and production.

### Planned Features

- [![LangFuse](https://img.shields.io/github/stars/langfuse/langfuse?logo=langfuse&label=LangFuse)](https://github.com/langfuse/langfuse) for LLM Observability and LLM Metrics
- [![Prometheus](https://img.shields.io/github/stars/prometheus/prometheus?logo=prometheus&label=Prometheus)](https://github.com/prometheus/prometheus) for scraping Metrics
- [![Grafana](https://img.shields.io/github/stars/prometheus/prometheus?logo=grafana&label=Grafana)](https://github.com/grafana/grafana) for visualizing Metrics
- [![Nginx](https://img.shields.io/github/stars/nginx/nginx?logo=nginx&label=Nginx)](https://github.com/nginx/nginx) Reverse Proxy
- [![Auth0](https://img.shields.io/badge/Auth0-white?logo=auth0)](https://auth0.com/docs) SaaS for JWT authentication
- CI/CD via Github Actions
  - :dollar: Deploy live demo to [![Fargate](https://img.shields.io/badge/Fargate-white.svg?logo=awsfargate)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
  - Provision with [![Terraform](https://img.shields.io/github/stars/hashicorp/terraform?logo=terraform&label=Terraform)](https://github.com/hashicorp/terraform) IaC
  - Push built images to ECR and Dockerhub
