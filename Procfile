web: gunicorn clutch.wsgi -b 0.0.0.0:$PORT
rpc: python -c "from clutchrpc.app import main; main()"
tunnel: python -c "from clutchtunnel.tunnel import main; main()"
