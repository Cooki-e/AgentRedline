const baseUrl = "https://sandbox.atlaspay.example/v2";

async function getToken() {
  const response = await fetch(`${baseUrl}/oauth/token`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      grant_type: "client_credentials",
      client_id: process.env.ATLASPAY_CLIENT_ID,
      client_secret: process.env.ATLASPAY_CLIENT_SECRET,
      scope: "payments:write payments:read customers:read webhooks:write"
    })
  });
  if (!response.ok) throw new Error(`Token request failed: ${response.status}`);
  return (await response.json()).access_token;
}
