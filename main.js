async function fetchSignals() {
  const container = document.getElementById('signal-container');
  container.innerHTML = "🔄 Loading...";

  try {
    const response = await fetch("https://a5-early-pump.onrender.com/api/early-pump");
    const data = await response.json();

    container.innerHTML = "";
    data.signals.forEach(signal => {
      const div = document.createElement("div");
      div.className = "signal-card";
      div.innerHTML = `
        <strong>Coin:</strong> ${signal.coin} <br/>
        <strong>Price:</strong> $${signal.price} <br/>
        <strong>Change:</strong> ${signal.change}% <br/>
        <strong>Volume Spike:</strong> ${signal.volume}
      `;
      container.appendChild(div);
    });
  } catch (error) {
    container.innerHTML = "❌ Failed to load signals";
    console.error(error);
  }
}
