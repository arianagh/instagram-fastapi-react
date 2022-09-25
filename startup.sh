#!/bin/bash


alembic upgrade head

#Start app
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload