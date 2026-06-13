async function loadSummary() {
  const banner = document.getElementById('status-banner');
  const box = document.getElementById('summary-box');
  try {
    const response = await fetch('/api/summary');
    const payload = await response.json();
    banner.textContent = `Preview data loaded for ${payload.program}`;
    banner.classList.add('ready');
    box.textContent = JSON.stringify(payload, null, 2);
  } catch (err) {
    banner.textContent = 'Preview data unavailable';
    box.textContent = String(err);
  }
}
window.addEventListener('DOMContentLoaded', loadSummary);
