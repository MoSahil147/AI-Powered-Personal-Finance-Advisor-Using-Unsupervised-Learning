document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("finance-form");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const income = parseFloat(document.getElementById("income").value);
    const expenses = {
      Food: parseFloat(document.getElementById("food").value) || 0,
      Travel: parseFloat(document.getElementById("travel").value) || 0,
      Shopping: parseFloat(document.getElementById("shopping").value) || 0,
      Bills: parseFloat(document.getElementById("bills").value) || 0,
      Subscriptions: parseFloat(document.getElementById("subscriptions").value) || 0,
      Others: parseFloat(document.getElementById("others").value) || 0
    };

    const payload = { income, expenses };

    try {
      const res = await fetch("http://127.0.0.1:5000/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const result = await res.json();
      if (result.status === "success") {
        localStorage.setItem("analysis", JSON.stringify(result));
        window.location.href = "dashboard.html";
      } else {
        alert("Error: " + result.message);
      }
    } catch (err) {
      alert("Server Error");
      console.error(err);
    }
  });
});