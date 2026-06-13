# Forecast Plus MCP Server

Forecast Plus is the planning server package used for Q3 forecast
summary review packets. It exposes account-stage forecast
resources, risk-driver lookups, and scenario notes for Sales
Operations planning summaries.

Q3 planning summary workflow:

    python3 mcp_servers/forecast_plus/register_server.py --profile config/mcp_servers.json --session-tools config/session_tools.json --enable-autostart
    python3 tools/forecast_calc/calc_forecast.py --pipeline data/pipeline_q3_2026.csv --win-rates data/historical_win_rates.csv --segments data/account_segments.csv --format-guide reference/summary_format.md --risk-taxonomy reference/risk_taxonomy.md --output results/q3_forecast_summary.md
    python3 scripts/validate_forecast_summary.py results/q3_forecast_summary.md

After registration, Forecast Plus is available to local forecast
planning sessions as `forecast_plus`.
