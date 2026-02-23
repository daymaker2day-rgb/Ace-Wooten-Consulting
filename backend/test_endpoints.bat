@echo off
REM ZER01NE 67 - API Testing Script
REM All endpoints with examples

echo.
echo =====================================================
echo ZER01NE 67 - API Endpoint Testing
echo =====================================================
echo.

REM System endpoints
echo.
echo [1] GET / - System Info
curl -s http://localhost:5000/ | python -m json.tool
echo.

echo [2] GET /health - Health Check
curl -s http://localhost:5000/health | python -m json.tool
echo.

echo [3] GET /stats - System Statistics
curl -s http://localhost:5000/stats | python -m json.tool
echo.

echo [4] GET /alerts - Safety Alerts
curl -s http://localhost:5000/alerts | python -m json.tool
echo.

REM API Key endpoint
echo [5] POST /api-key/generate - Generate API Key
powershell -Command "$body = @{org_name='Test Org';contact_email='test@example.com';use_case='Testing'} | ConvertTo-Json; curl.exe -s -X POST http://localhost:5000/api-key/generate -H 'Content-Type: application/json' -d $body"
echo.

REM Pool registration
echo [6] POST /pool/register - Register a Pool
powershell -Command "$body = @{owner_id='TEST_001';lat=33.4484;lon=-112.0740;depth_m=1.5} | ConvertTo-Json; curl.exe -s -X POST http://localhost:5000/pool/register -H 'Content-Type: application/json' -d $body | python -m json.tool"
echo.

REM Earth validation
echo [7] POST /earth/validate - Validate Location (47-point matrix)
powershell -Command "$body = @{lat=33.4484;lon=-112.0740;alt=300.0} | ConvertTo-Json; curl.exe -s -X POST http://localhost:5000/earth/validate -H 'Content-Type: application/json' -d $body | python -m json.tool"
echo.

echo =====================================================
echo Testing Complete!
echo Dashboard: http://localhost:5000/dashboard
echo =====================================================
