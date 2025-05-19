// Enhanced charts.js file

document.addEventListener("DOMContentLoaded", () => {
  // Get analysis data from localStorage
  const analysis = JSON.parse(localStorage.getItem("analysis"));
  
  if (!analysis) {
    alert("No analysis data found. Please input your expenses again.");
    window.location.href = "index.html";
    return;
  }
  
  const cluster = analysis.cluster;
  const tips = analysis.tips;
  const input = analysis.input;
  
  // Display cluster information
  document.getElementById("cluster-display").textContent = `Group ${cluster + 1}`;
  
  // Set cluster descriptions
  const clusterDescriptions = [
    "You're in the low-saver group. We'll help you boost your savings!",
    "You're in the balanced spender group. Let's optimize your finances!",
    "You're in the high-saver group. Great job managing your money!"
  ];
  document.getElementById("cluster-description").textContent = clusterDescriptions[cluster];
  
  // Display saving rate
  document.getElementById("saving-rate").textContent = input.saving_rate.toFixed(1);
  
  // Set health score based on cluster
  const healthScores = ["Needs Work", "Good", "Excellent"];
  document.getElementById("health-score").textContent = healthScores[cluster];
  
  // Calculate and set health description
  let healthDesc = "";
  if (cluster === 0) {
    healthDesc = "Focus on reducing discretionary spending";
  } else if (cluster === 1) {
    healthDesc = "Good balance, with room for improvement";
  } else {
    healthDesc = "Excellent savings habits";
  }
  document.getElementById("health-description").textContent = healthDesc;
  
  // Display tips
  const tipsContainer = document.getElementById("tips-container");
  tips.forEach((tip) => {
    const tipElement = document.createElement("div");
    tipElement.className = "tip-item";
    tipElement.innerHTML = `<i class="fas fa-check-circle" style="color: #4361EE; margin-right: 10px;"></i> ${tip}`;
    tipsContainer.appendChild(tipElement);
  });
  
  // Prepare data for charts
  const categoryLabels = ["Food", "Travel", "Shopping", "Bills", "Subscriptions", "Others"];
  const pieData = [
    input.food_pct,
    input.travel_pct,
    input.shopping_pct,
    input.bills_pct,
    input.subscriptions_pct,
    input.others_pct
  ];
  
  const expenseTypeLabels = ["Essential", "Recurring", "Discretionary"];
  const expenseTypeData = [
    input.essential_expense_ratio,
    input.recurring_expense_ratio,
    input.discretionary_expense_ratio
  ];
  
  // Create pie chart
  new Chart(document.getElementById("pieChart"), {
    type: "doughnut",
    data: {
      labels: categoryLabels,
      datasets: [{
        data: pieData,
        backgroundColor: [
          "#FF6384", // Food - Red
          "#36A2EB", // Travel - Blue
          "#FFCE56", // Shopping - Yellow
          "#4BC0C0", // Bills - Teal
          "#9966FF", // Subscriptions - Purple
          "#C9CBCF"  // Others - Gray
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'right',
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              return `${context.label}: ${context.raw.toFixed(1)}%`;
            }
          }
        }
      }
    }
  });
  
  // Create bar chart instead of line chart for better visualization
  new Chart(document.getElementById("lineChart"), {
    type: "bar",
    data: {
      labels: expenseTypeLabels,
      datasets: [{
        label: "Spending by Category (%)",
        data: expenseTypeData,
        backgroundColor: [
          "rgba(75, 192, 192, 0.7)",  // Essential - Teal
          "rgba(153, 102, 255, 0.7)", // Recurring - Purple
          "rgba(255, 159, 64, 0.7)"   // Discretionary - Orange
        ],
        borderColor: [
          "rgba(75, 192, 192, 1)",
          "rgba(153, 102, 255, 1)",
          "rgba(255, 159, 64, 1)"
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
          max: 100,
          title: {
            display: true,
            text: 'Percentage of Income'
          }
        }
      },
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              return `${context.dataset.label}: ${context.raw.toFixed(1)}%`;
            }
          }
        }
      }
    }
  });
});