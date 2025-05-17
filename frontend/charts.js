// frontend/charts.js

document.addEventListener("DOMContentLoaded", () => {
    const analysis = JSON.parse(localStorage.getItem("analysis"));
  
    if (!analysis) {
      alert("No analysis data found. Please input your expenses again.");
      window.location.href = "index.html";
      return;
    }
  
    const cluster = analysis.cluster;
    const tips = analysis.tips;
    const input = analysis.input;
  
    document.getElementById("cluster").textContent = cluster;
    document.getElementById("saving-rate").textContent = input.saving_rate;
  
    const tipsList = document.getElementById("tips-list");
    tips.forEach((tip) => {
      const li = document.createElement("li");
      li.textContent = tip;
      tipsList.appendChild(li);
    });
  
    const categoryLabels = ["Food", "Travel", "Shopping", "Bills", "Subscriptions", "Others"];
    const pieData = [
      input.food_pct,
      input.travel_pct,
      input.shopping_pct,
      input.bills_pct,
      input.subscriptions_pct,
      input.others_pct
    ];
  
    const lineData = [
      input.essential_expense_ratio,
      input.recurring_expense_ratio,
      input.discretionary_expense_ratio
    ];
  
    const lineLabels = ["Essential", "Recurring", "Discretionary"];
  
    new Chart(document.getElementById("pieChart"), {
      type: "pie",
      data: {
        labels: categoryLabels,
        datasets: [{
          data: pieData,
          backgroundColor: [
            "#f39c12", "#3498db", "#9b59b6", "#e74c3c", "#1abc9c", "#95a5a6"
          ]
        }]
      }
    });
  
    new Chart(document.getElementById("lineChart"), {
      type: "line",
      data: {
        labels: lineLabels,
        datasets: [{
          label: "Spending Ratios (%)",
          data: lineData,
          fill: false,
          borderColor: "#2ecc71",
          tension: 0.1
        }]
      }
    });
  });